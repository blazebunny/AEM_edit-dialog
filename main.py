from xml.dom import minidom 
from tkinter import * 
from tkinter.ttk import *

from tkinterhtml import HtmlFrame

from PIL import ImageTk, Image

import os  

def rootFunction():

    root = minidom.Document() 

    xml = root.createElement('jcr:root')  
    #  xmlns:sling="http://sling.apache.org/jcr/sling/1.0" xmlns:cq="http://www.day.com/jcr/cq/1.0" xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:nt="http://www.jcp.org/jcr/nt/1.0"
    xml.setAttribute('xmlns:sling', 'http://sling.apache.org/jcr/sling/1.0')
    xml.setAttribute('xmlns:cq', 'http://www.day.com/jcr/cq/1.0')
    xml.setAttribute('xmlns:jcr', 'http://www.jcp.org/jcr/1.0')
    xml.setAttribute('xmlns:nt', 'http://www.jcp.org/nt/1.0')
    xml.setAttribute('jcr:primaryType', 'nt:unstructured')
    xml.setAttribute('jcr:title', 'Image')
    xml.setAttribute('sling:resourceType', 'cq/gui/components/authoring/dialog')
    root.appendChild(xml) 
    
    productchild = root.createElement('content') 
    productchild.setAttribute('jcr:primaryType', 'nt:unstructured')
    productchild.setAttribute('sling:resourceType', 'granite/ui/components/coral/foundation/container')
    
    xml.appendChild(productchild) 
    
    xml_str = root.toprettyxml(indent ="\t")  
    
    save_path_file = "test.xml"
    
    with open(save_path_file, "w") as f: 
        f.write(xml_str)  

def displayhtml():
    
    global fram1
    frame = HtmlFrame(fram1, horizontal_scrollbar="true")
    frame.grid(sticky=NSEW)
    file_read = open("dialog.html", "r")
    frame.set_content(file_read.read())

def sidelist():
        
    Lb1 = Listbox()
    Lb1.insert(1, "Python")
    Lb1.insert(2, "Perl")
    Lb1.insert(3, "C")
    Lb1.insert(4, "PHP")
    Lb1.insert(5, "JSP")
    Lb1.insert(6, "Ruby")

    Lb1.pack()
    
def sideButton():
    Lb1 = Listbox()
    Lb1.insert(1, "Python")
    Lb1.insert(2, "Perl")
    Lb1.insert(3, "C")
    Lb1.insert(4, "PHP")
    Lb1.insert(5, "JSP")
    Lb1.insert(6, "Ruby")

    mylist = ['item1', 'item2', 'item3']
    for item in mylist:
        button = Button(root, text=item)
        button.grid(row=mylist.index(item) +1 ,column=12)
    

    Button1 = Button(root,text="Button1")
    Button2 = Button(root,text="Button2")
    Button3 = Button(root,text="Button3")
    Label1 = Label(root,text="Label1")
    Label2 = Label(root,text="Label2")
    Label3 = Label(root,text="Label3")

    Button1.grid(row=0,column=0,columnspan=2)
    Button2.grid(row=0,column=2)
    Label1.grid(row=1,column=0)
    Label2.grid(row=1,column=1)
    Label3.grid(row=1,column=2)

def separateFrame():
    global fram1, fram2
    #Create Panedwindow  
    panedwindow=Panedwindow(root, orient=HORIZONTAL)  
    panedwindow.pack(fill=BOTH, expand=True)
    #Create Frams  
    fram1=Frame(panedwindow,width=1080,height=1440, relief=SUNKEN)  
    fram2=Frame(panedwindow,width=1080,height=480, relief=SUNKEN)  
    
    
    mylist = ['item1', 'item2', 'item3']
    for item in mylist:
        button = Button(fram2, text=item)
        button.pack(side=RIGHT)
        button.bind("<B1-Motion>", movefunction)
        # button.grid(row=mylist.index(item) +1 ,column=12)
    
    panedwindow.add(fram1, weight=1)  
    panedwindow.add(fram2, weight=4)

def movefunction(event):
    print ('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

    winX = event.x - root.canvas.canvasx(0)
    winY = event.y - root.canvas.canvasy(0)
    root.dragInfo["Widget"] = root.canvas.find_closest(event.x, event.y, halo = 5)[0]

    # reset the starting point for the next move
    root.dragInfo["xCoord"] = winX
    root.dragInfo["yCoord"] = winY

# Variables
fram1 = None
fram2 = None 
# Functions
root = Tk(className= "Edit Dialog")
root.geometry("1080x1920")
separateFrame()
displayhtml()
mainloop() 