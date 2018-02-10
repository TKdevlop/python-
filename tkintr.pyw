from tkinter import *
from PIL import Image,ImageTk
# its part of standard library to create windows
#  * for import everthing

class Window(Frame): # Frame is passing through tkinter module
    def __init__(self,master): #is not necsseary to use "self"
        Frame.__init__(self,master) # master is our main windows 

        self.master= master # main windows

        self.init_window()  # inner intilisation
    def init_window(self): # intialisation the window

        self.master.title("GUI") # to set the title of window
        self.pack(fill=BOTH, expand=1) # filling up thw window and adujust dimension as need

        #quitButton=Button(self,text="quit", command=self.client_exit) # Button is funtion within tkinter 
       # quitButton.place(x=0,y=0) # we name the button quit  # nameing the button

        menu=Menu(self.master) # Menu is refernce to something build in tkinter
        self.master.config(menu=menu) # we are configuring menu=menu

        file=Menu(menu) #
        file.add_command(label="Exit",command=self.client_exit)#we are adding what we want to writee in  the command button and givin it exit client command
        menu.add_cascade(label="File",menu=file)


        edit=Menu(menu)
        edit.add_command(label="Show Image", command=self.showImg)
        edit.add_command(label="Show Image", command=self.showTxt)
        menu.add_cascade(label="Edit",menu=edit)
        
        
        def showImg(self):
            load=Image.open("pic.png")
            render= ImageTk.PhotoImage(load)
            img=Label(self, image=render)
            img.image=render
            img.place(x=0,y=0)

        def showTxt(self):
             text=Label(self, text="HELLO MOTHER FUCKER THIS IS INSSANE")
             text.pack()



        #quit # place is where we get button placed x and y are axis
    def client_exit(self):#you can refernce the funtion before its defined but
    #you cannot call it in python
        exit() # exit is build funtion to exit
        
        

root=Tk() # importing Tk from tkinterits our root window
root.geometry("400x300") #to specify dimension of the window 
app= Window(root) # referencing for Window class

root.mainloop() # genrate window for us
        
    
