from tkinter import *
root = Tk()
root.title("First Program");
myLabel = Label(root, text="Good Afternoon!");
myLabel.grid(row=0,column=0)
myLabel.pack();
Chkbtn = Checkbutton(root,text="are you sure?")
Chkbtn.grid(row=1,column=0)
Chkbtn.pack();
Button = Button(root, text="Button")
Button.pack();

root.mainloop();