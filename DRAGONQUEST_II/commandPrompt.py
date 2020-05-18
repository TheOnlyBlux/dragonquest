from tkinter import *
    
promptWindow = Tk()

Label(promptWindow, text="DRAGONQUEST").pack()

promptEntry = Entry(promptWindow)
promptEntry.pack()
def inputPrompt():
    global query
    global promptEntry
    query = promptEntry.get()

Button(promptWindow, text="enter", cursor="arrow", command=inputPrompt).pack()
    
promptWindow.mainloop()