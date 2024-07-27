from pathlib import Path
from re import match
from time import time
from sys import argv


class Patient:
    file: Path
    name: str | None
    id: int | None
    info: str | None
    extension: str | None


    def __init__(self, file: Path) -> None:
        self.file = file
        try:
            id_index = next((i for i, c in enumerate(file.name) if c.isdigit()), -1)
            self.name = file.name[:id_index].strip()
            self.id = int(file.name[id_index:].strip().split(" ")[0])
            other = file.name[
                file.name.index(str(self.id)) + len(str(self.id)) :
            ].split(".")
            self.info = other[0].strip()
            self.extension = other[1].strip()
        except Exception:
            self.name = None


    def is_valid(self) -> bool:
        if (
            self.name is None
            or self.id is None
            or self.info is None
            or self.extension is None
        ):
            return False
        name_pattern = r"([A-Za-z']+((-[A-Za-z']+)|(\s[A-Za-z']+))?)"
        if not match(f"^{name_pattern}\s{name_pattern}$", self.name):
            return False
        if self.id > 99999:
            return False
        if "py" in self.extension or "exe" in self.extension:
            return False
        return True


    def capitalize_name(self) -> None:
        previous_char = " "
        for i in range(len(self.name)):
            if previous_char in (" ", "-"):
                self.name = self.name[:i] + self.name[i].upper() + self.name[i + 1 :]
            previous_char = self.name[i]
    
    
    def sort(self, is_prod: bool = True) -> None:
        first_letter, second_letter = self.name[0].upper(), self.name[1].upper()
        letter_folder = Path().cwd().parent / first_letter
        if first_letter == "S":
            return letter_folder / ("SA to SL" if second_letter <= "L" else "SM to SZ")
        elif first_letter == "M":
            return letter_folder / ("Ma to Mh" if second_letter <= "H" else "Mi to Mz")
        
        patient_folder = (letter_folder / f"{self.name} {self.id}").resolve()
        patient_file = (
            patient_folder / f"{self.name} {self.id} {self.info}.{self.extension}"
        ).resolve()

        if is_prod:
            patient_folder.mkdir(exist_ok=True)
        else:
            print(f"mkdir -p \"{patient_folder}\"")
        
        if patient_file.exists():
            time_ms = int(time() * 1000)
            patient_file = (
                patient_folder / f"{self.name} {self.id} {self.info}_{time_ms}.{self.extension}"
            ).resolve()
        
        if is_prod:
            self.file.rename(patient_file)
        else:
            print(f"mv \"{self.file}\" \"{patient_file}\"")

    def __str__(self) -> str:
        return f"Name: {self.name}, ID: {self.id}, Info: {self.info}, Extension: {self.extension}"


if __name__ == "__main__":
    is_prod = not (len(argv) > 1 and argv[1] == "dev")
    for file in Path().cwd().iterdir():
        if file.is_file():
            patient = Patient(file)
            if patient.is_valid():
                patient.capitalize_name()
                patient.sort(is_prod)
