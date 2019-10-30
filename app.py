import tkinter as tk
import os

LARGE_FONT = ("Verdana", 12)
CLASSES = ["English","Music","Programming"]

class ObjTkinter(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        mainFrame = tk.Frame(self)
        mainFrame.pack(side="top", fill="both", expand = True)

        mainFrame.grid_rowconfigure(0, weight=0)
        mainFrame.grid_columnconfigure(0, weight=0)

        self.frames = {}

        for F in (MainPage, AddClass_window):

            frame = F(mainFrame, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        #frame = MainPage(mainFrame, self)

        #self.frames[MainPage] = frame

        #frame.grid(row=0, column=0, sticky="nsew")

        # Delet this for new page ^

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainPage(tk.Frame):

    TEXTBOXHEIGHT = 3

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=400, height=200, bg="white")

        tk.Label(self, text="Monday", bg="white", fg="black").grid(row=2, column=1)
        tk.Label(self, text="Tuesday", bg="white", fg="black").grid(row=3, column=1)
        tk.Label(self, text="Wednsday", bg="white", fg="black").grid(row=4, column=1)
        tk.Label(self, text="Thursday", bg="white", fg="black").grid(row=5, column=1)
        tk.Label(self, text="Friday", bg="white", fg="black").grid(row=6, column=1)
        tk.Label(self, text="Saturday", bg="white", fg="black").grid(row=7, column=1)
        tk.Label(self, text="Sunday", bg="white", fg="black").grid(row=8, column=1)

        newTextBoxes = {}

        for i in range(len(CLASSES)):
            for x in range(7):
                newText = tk.Text(self, width=10, height=self.TEXTBOXHEIGHT, bg="white", fg="black")
                newTextBoxes[i,x] = newText


        for i in range(len(CLASSES)):
            for x in range(7):
                tk.Label(self, text=CLASSES[i], bg="white", fg="black").grid(row=1, column=i+2)
                newTextBoxes[i,x].grid(row=x+2, column=i+2)

        tk.Label(self, text=CLASSES[0], bg="white", fg="black").grid(row=1, column=2)

        text = self.read_homework(newTextBoxes)

        try:
            count = 0

            for i in range(len(CLASSES)):
                for x in range(7):
                    newTextBoxes[i,x].insert("1.0", text[count])
                    count = count + 1
        except IndexError:
            print("Need to save first")

        def AddClass():
            controller.show_frame(AddClass_window)

        def Save():
            
            text = ""
            
            for i in range(len(CLASSES)):
                for x in range(7):
                    text = text + newTextBoxes[i,x].get("1.0", "end-1c") + "|"

            file = open("Homework/Homework","w")
            file.write(text)
            file.close

        def Quit():
            quit()
        
        addClassButton = tk.Button(self, text="Add", bg="white", fg="black", command=AddClass)
        saveButton = tk.Button(self, text="Save", bg="white", fg="black", command=Save)
        quitButton = tk.Button(self, text="Quit", bg= "white", fg="black", command=Quit)
        
        addClassButton.grid(row=1, column=len(CLASSES)+2)
        saveButton.grid(row=9, column=2)
        quitButton.grid(row=9, column=4)

    def read_homework(self, TEXBOXES):
        file = open("Homework/Homework","r")
        text = file.read()
        file.close

        text = text.split("|")

        return text
        
class AddClass_window(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=400, height=200, bg="white")

        tk.Label(self,text="What class do you want to add?").grid(row=1,column=1)
        newClass = tk.Entry(self)

        def addClassToList():
            CLASSES.append(newClass.get())
            controller.show_frame(MainPage)

        addButton = tk.Button(self, text="Add", command=addClassToList)

        newClass.grid(row=2, column=1)
        addButton.grid(row=3, column=1)

app = ObjTkinter()
app.mainloop()