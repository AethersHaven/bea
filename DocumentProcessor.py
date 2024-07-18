from Scanner import *
from GUI import *

def main():
    image = GetImage("Document Example.pdf")
    info = ProcessPatientInfo(image)

    verifiedInfo = VerifyDisplay(image, info)
    print(verifiedInfo)
    print(verifiedInfo == info)

if __name__ == "__main__":
    main()