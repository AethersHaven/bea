# Imports
from tkinter import *
from tkinter.ttk import *
from tkinter import Button
from PIL import ImageTk
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import os

# Class
class Display:
    # Settings
    Title = "Vision Therapy Chart Generator"
    Width = 915
    Height = 825
    Font = "Arial"
    FontSize = 25
    EntryWidth = 15
    ImageUpdateTime = 2000

    # Variables
    Window = 0
    PageCountString = 0
    BoxSizeString = 0
    SpacingSizeString = 0
    BoxesWidthString = 0
    BoxesHeightString = 0
    LineWidthString = 0
    IconChanceString = 0
    NumberChanceString = 0
    LetterChanceString = 0
    RedBoxChanceString = 0
    GreenBoxChanceString = 0
    RedTextChanceString = 0
    GreenTextChanceString = 0
    MaxIconRepeatsString = 0
    MaxNumberRepeatsString = 0
    MaxLetterRepeatsString = 0
    LettersString = 0
    Canvas = 0
    ImageContext = 0
    Image = 0
    ErrorLabel = 0

    # Methods
    @classmethod
    def SetupEntry(this, name, defaultText, row, column):
        string = StringVar()
        label = Label(text=name, font=(this.Font, this.FontSize))
        entry = Entry(width=this.EntryWidth, textvariable=string, font=(this.Font, this.FontSize))
        entry.insert(0, defaultText)
        label.grid(row=row, column=column)
        entry.grid(row=row+1, column=column)
        return string

    @classmethod
    def DisplaySettings(this):
        # Setup Window
        this.Window = Tk()
        this.Window.title(this.Title)
        this.Window.geometry(str(this.Width)+"x"+str(this.Height))

        this.PageCountString = this.SetupEntry("ImageCount", PageGenerator.PageCount, 0, 0)
        this.BoxSizeString = this.SetupEntry("BoxSize", PageGenerator.BoxSize, 0, 1)
        this.SpacingSizeString = this.SetupEntry("SpacingSize", PageGenerator.SpacingSize, 0, 2)
        this.BoxesWidthString = this.SetupEntry("BoxesWidth", PageGenerator.BoxesWidth, 4, 0)
        this.BoxesHeightString = this.SetupEntry("BoxesHeight", PageGenerator.BoxesHeight, 4, 1)
        this.LineWidthString = this.SetupEntry("LineWidth", PageGenerator.LineWidth, 4, 2)
        this.IconChanceString = this.SetupEntry("IconChance", PageGenerator.IconChance, 7, 0)
        this.NumberChanceString = this.SetupEntry("NumberChance", PageGenerator.NumberChance, 7, 1)
        this.LetterChanceString = this.SetupEntry("LetterChance", PageGenerator.LetterChance, 7, 2)
        this.RedBoxChanceString = this.SetupEntry("RedBoxChance", PageGenerator.RedBoxChance, 10, 0)
        this.GreenBoxChanceString = this.SetupEntry("GreenBoxChance", PageGenerator.GreenBoxChance, 10, 1)
        this.RedTextChanceString = this.SetupEntry("RedTextChance", PageGenerator.RedTextChance, 13, 0)
        this.GreenTextChanceString = this.SetupEntry("GreenTextChance", PageGenerator.GreenTextChance, 13, 1)
        this.LettersString = this.SetupEntry("Letters", "".join(PageGenerator.Letters), 13, 2)
        this.MaxIconRepeatsString = this.SetupEntry("MaxIconRepeats", PageGenerator.MaxIconRepeats, 16, 0)
        this.MaxNumberRepeatsString = this.SetupEntry("MaxNumberRepeats", PageGenerator.MaxNumberRepeats, 16, 1)
        this.MaxLetterRepeatsString = this.SetupEntry("MaxLetterRepeats", PageGenerator.MaxLetterRepeats, 16, 2)

        # Submit button
        submitButton = Button(text="Generate/Save Images", command=this.SubmitSettings, width=20, height=5, bg='grey', font=(this.Font, 20))
        submitButton.grid(row=19, column=1)

        # Image example
        img = ImageTk.PhotoImage(PageGenerator.GeneratePage().resize((300, 300)))
        this.Canvas = Canvas(this.Window, width=300, height=300)  
        this.Canvas.grid(row=19, column=2)
        this.ImageContext = this.Canvas.create_image(2, 2, anchor="nw", image=img)

        # Error
        this.ErrorLabel = Label(text=PageGenerator.Error, font=(this.Font, 25))
        this.ErrorLabel.grid(row=19, column=0)
        
        # Run Window
        this.Window.after(this.ImageUpdateTime, this.UpdateImage)
        this.Window.mainloop()

    @classmethod
    def SubmitSettings(this):
        try:
            PageGenerator.PageCount = int(this.PageCountString.get())
            PageGenerator.BoxSize = int(this.BoxSizeString.get())
            PageGenerator.SpacingSize = int(this.SpacingSizeString.get())
            PageGenerator.BoxesWidth = int(this.BoxesWidthString.get())
            PageGenerator.BoxesHeight = int(this.BoxesHeightString.get())
            PageGenerator.LineWidth = int(this.LineWidthString.get())
            PageGenerator.IconChance = float(this.IconChanceString.get())
            PageGenerator.NumberChance = float(this.NumberChanceString.get())
            PageGenerator.LetterChance = float(this.LetterChanceString.get())
            PageGenerator.RedBoxChance = float(this.RedBoxChanceString.get())
            PageGenerator.GreenBoxChance = float(this.GreenBoxChanceString.get())
            PageGenerator.RedTextChance = float(this.RedTextChanceString.get())
            PageGenerator.GreenTextChance = float(this.GreenTextChanceString.get())
            PageGenerator.MaxIconRepeats = int(this.MaxIconRepeatsString.get())
            PageGenerator.MaxNumberRepeats = int(this.MaxNumberRepeatsString.get())
            PageGenerator.MaxLetterRepeats = int(this.MaxLetterRepeatsString.get())
            PageGenerator.Letters = list(this.LettersString.get())
            PageGenerator.LoadVariables()
            PageGenerator.GenerateAndSavePages()
            this.ErrorLabel.config(text = PageGenerator.Error)
            PageGenerator.Error = ""
        except:
            a = 0

    @classmethod
    def UpdateImage(this):
        try:
            PageGenerator.PageCount = int(this.PageCountString.get())
            PageGenerator.BoxSize = int(this.BoxSizeString.get())
            PageGenerator.SpacingSize = int(this.SpacingSizeString.get())
            PageGenerator.BoxesWidth = int(this.BoxesWidthString.get())
            PageGenerator.BoxesHeight = int(this.BoxesHeightString.get())
            PageGenerator.LineWidth = int(this.LineWidthString.get())
            PageGenerator.IconChance = float(this.IconChanceString.get())
            PageGenerator.NumberChance = float(this.NumberChanceString.get())
            PageGenerator.LetterChance = float(this.LetterChanceString.get())
            PageGenerator.RedBoxChance = float(this.RedBoxChanceString.get())
            PageGenerator.GreenBoxChance = float(this.GreenBoxChanceString.get())
            PageGenerator.RedTextChance = float(this.RedTextChanceString.get())
            PageGenerator.GreenTextChance = float(this.GreenTextChanceString.get())
            PageGenerator.MaxIconRepeats = int(this.MaxIconRepeatsString.get())
            PageGenerator.MaxNumberRepeats = int(this.MaxNumberRepeatsString.get())
            PageGenerator.MaxLetterRepeats = int(this.MaxLetterRepeatsString.get())
            PageGenerator.Letters = list(this.LettersString.get())
            PageGenerator.LoadVariables()
            if PageGenerator.BoxesWidth > 25 or PageGenerator.BoxesHeight > 25:
                this.Window.after(this.ImageUpdateTime, this.UpdateImage)
                return
            img = ImageTk.PhotoImage(PageGenerator.GeneratePage().resize((300, 300)))
            this.Canvas.itemconfig(this.ImageContext,image=img)
            this.Canvas.imgref = img
            this.ErrorLabel.config(text = PageGenerator.Error)
            PageGenerator.Error = ""
        except:
            a = 0
        this.Window.after(this.ImageUpdateTime, this.UpdateImage)

class PageGenerator:
    # Settings
    PageCount = 5
    BoxSize = 200
    SpacingSize = 50
    BoxesWidth = 6
    BoxesHeight = 6
    LineWidth = 5
    IconChance = 0.5
    NumberChance = 0.25
    LetterChance = 0.25
    RedBoxChance = 0.02
    GreenBoxChance = 0.02
    RedTextChance = 0.02
    GreenTextChance = 0.02
    MaxIconRepeats = 1
    MaxNumberRepeats = 1
    MaxLetterRepeats = 2
    Letters = ["H", "O", "T", "V", "A", "C", "E", "Z"]
    BackgroundColor = (255, 255, 255)
    LineColor = (0, 0, 0)
    NumberColor = (0, 0, 0)
    LetterColor = (0, 0, 0)

    # Variables
    FileFormats = {".bmp", ".dds", ".dib", ".eps", ".gif", ".icns", ".ico", ".im", ".jpeg", ".jpg", ".msp", ".pcx", ".png", ".ppm", ".sgi", ".spi", ".tga", ".tiff", ".webp", ".xbm"}
    Icons = []
    Numbers = []
    BoxCount = BoxesWidth * BoxesHeight
    IconSize = int(BoxSize-SpacingSize*2)
    Font = ImageFont.truetype('font.ttf', size=int(IconSize*0.8))
    IconRepeats = []
    NumberRepeats = []
    LetterRepeats = []
    
    Error = ""

    # Methods
    @classmethod
    def GetValidElement(this, arr, repeats, max):
        index = int(random.random()*len(arr))
        count = 0
        while repeats[index] >= max:
            index = int(random.random()*len(arr))
            count += 1
            if count > 256:
                this.Error = "Max repeat limited"
                break
        repeats[index] += 1
        return arr[index]

    @classmethod
    def GetTextColor(this, hasBox):
        if hasBox == True:
            return (0, 0, 0)
        colorChance = random.random()
        if colorChance < this.RedTextChance:
            return (255, 0,  0)
        elif colorChance < this.RedTextChance + this.GreenTextChance:
            return (0, 255, 0)
        return (0, 0, 0)

    @classmethod
    def Initialize(this):
        # Load icons
        iconFiles = []
        for file in os.listdir(os.path.join(os.getcwd(), "images")):
            for extension in this.FileFormats:
                if file.endswith(extension) and not "export" in file:
                    iconFiles.append(file)
                    break
        this.Icons = []
        for iconFile in iconFiles:
            this.Icons.append(Image.open(os.path.join("images", iconFile)).convert("RGBA").resize((this.IconSize, this.IconSize)))
            
        # Load up the numbers
        for i in range(1, 100):
            this.Numbers.append(i)

        # Set up the repeats
        for i in range(len(this.Icons)):
            this.IconRepeats.append(0)
        for i in range(len(this.Numbers)):
            this.NumberRepeats.append(0)
        for i in range(len(this.Letters)):
            this.LetterRepeats.append(0)

    @classmethod
    def LoadVariables(this):
        this.BoxCount = this.BoxesWidth * this.BoxesHeight
        this.IconSize = int(this.BoxSize-this.SpacingSize*2)
        this.Font = ImageFont.truetype('font.ttf', size=int(this.IconSize*0.8))

    @classmethod
    def GeneratePage(this):
        # Reset repeats
        for i in range(len(this.IconRepeats)):
            this.IconRepeats[i] = 0
        for i in range(len(this.NumberRepeats)):
            this.NumberRepeats[i] = 0
        for i in range(len(this.LetterRepeats)):
            this.LetterRepeats[i] = 0

        # Generate page
        page = Image.new("RGB", (this.BoxSize*this.BoxesWidth, this.BoxSize*this.BoxesHeight), this.BackgroundColor)

        # Generate images to paste
        horizontalLine = Image.new("RGB", (this.BoxSize*this.BoxesWidth, this.LineWidth), this.LineColor)
        verticalLine = Image.new("RGB", (this.LineWidth, this.BoxSize*this.BoxesHeight), this.LineColor)
        redBox = Image.new("RGB", (this.BoxSize-this.LineWidth, this.BoxSize-this.LineWidth), (255, 0, 0))
        greenBox = Image.new("RGB", (this.BoxSize-this.LineWidth, this.BoxSize-this.LineWidth), (0, 255, 0))

        # Paste icons and boxes
        for x in range(this.BoxesWidth):
            for y in range(this.BoxesHeight):
                # Boxes
                hasBox = False
                boxLocation = (int(x*this.BoxSize+this.LineWidth), int(y*this.BoxSize+this.LineWidth))
                boxChance = random.random()
                if boxChance < this.RedBoxChance:
                    hasBox = True
                    page.paste(redBox, boxLocation)
                elif boxChance < this.RedBoxChance + this.GreenBoxChance:
                    hasBox = True
                    page.paste(greenBox, boxLocation)

                # Box contents
                contentLocation = (int(x*this.BoxSize+this.SpacingSize), int(y*this.BoxSize+this.SpacingSize))
                contentChance = random.random()
                if contentChance < this.IconChance and hasBox == False: # Icon
                    icon = this.GetValidElement(this.Icons, this.IconRepeats, this.MaxIconRepeats)
                    page.paste(icon, contentLocation, mask=icon)
                elif contentChance < this.IconChance + this.NumberChance: # Number
                    number = this.GetValidElement(this.Numbers, this.NumberRepeats, this.MaxNumberRepeats)
                    color = this.GetTextColor(hasBox)
                    if number < 10:
                        number = " "+str(number)
                    ImageDraw.Draw(page).text(contentLocation, str(number), font=this.Font, fill=color)
                else: # Letter
                    letter = " "+this.GetValidElement(this.Letters, this.LetterRepeats, this.MaxLetterRepeats)
                    color = this.GetTextColor(hasBox)
                    ImageDraw.Draw(page).text(contentLocation, letter, font=this.Font, fill=color)

        # Paste lines
        for j in range(this.BoxesHeight):
            page.paste(horizontalLine, (0, int(j*this.BoxSize)))
        page.paste(horizontalLine, (0, this.BoxSize*this.BoxesHeight-this.LineWidth))
        for j in range(this.BoxesWidth):
            page.paste(verticalLine, (int(j*this.BoxSize), 0))
        page.paste(verticalLine, (this.BoxSize*this.BoxesWidth-this.LineWidth, 0))

        return page

    @classmethod
    def GenerateAndSavePages(this):
        exports_path = os.path.join(os.getcwd(), "exports")
        os.makedirs(exports_path, exist_ok=True)

        # Clear out old pages
        for fileName in os.listdir(exports_path):
            if fileName.startswith("export-") and fileName.endswith(".jpg"):
                os.remove(os.path.join(exports_path, fileName))

        # Generate and save new pages
        for pageIndex in range(this.PageCount):
            page_path = os.path.join(exports_path, f"export-{pageIndex}.jpg")
            PageGenerator.GeneratePage().save(page_path, quality=300)

def main():
    PageGenerator.Initialize()
    Display.DisplaySettings()

if __name__ == "__main__":
    main()
