from tkinter import *
from tkinter.ttk import *
from tkinter import Button
from PIL import ImageTk,Image
import cv2

window = 0

# Returns the verified information
def VerifyDisplay(image, info):
    global window
    window = Tk()
    window.title("Patient Info Verification")
    height, width = image.shape
    window.geometry(str(width) + "x" + str(height + 500))

    # Image
    cv2.imwrite("Document Example.png", image)
    canvas = Canvas(window, width=width, height=height)  
    canvas.pack() 
    img = ImageTk.PhotoImage(Image.open("Document Example.png"))  
    canvas.create_image(0, 0, anchor=NW, image=img)

    # Name
    nameString = StringVar()
    nameLabel = Label(text="Name", font=("Arial", 25))
    nameEntry = Entry(width=20, justify=CENTER, textvariable=nameString, font=("Arial", 25))
    nameEntry.insert(0, info[0])
    nameLabel.pack()
    nameEntry.pack()

    # ID
    idString = StringVar()
    idLabel = Label(text="ID", font=("Arial", 25))
    idEntry = Entry(width=20, justify=CENTER, textvariable=idString, font=("Arial", 25))
    idEntry.insert(0, info[1])
    idLabel.pack()
    idEntry.pack()

    # Date
    dateString = StringVar()
    dateLabel = Label(text="Date", font=("Arial", 25))
    dateEntry = Entry(width=20, justify=CENTER, textvariable=dateString, font=("Arial", 25))
    dateEntry.insert(0, info[2])
    dateLabel.pack()
    dateEntry.pack()

    # Document Type
    typeString = StringVar()
    typeLabel = Label(text="Document Type", font=("Arial", 25))
    typeEntry = Entry(width=20, justify=CENTER, textvariable=typeString, font=("Arial", 25))
    typeEntry.insert(0, info[3])
    typeLabel.pack()
    typeEntry.pack()

    # Submit Button
    submitButton = Button(text="Submit", command=HandleSubmitButtonPress, width=100, height=10, bg='white')
    submitButton.pack(pady=20)

    window.mainloop()

    return [nameString.get(), idString.get(), dateString.get(), typeString.get()]

def HandleSubmitButtonPress():
    global window
    window.destroy()