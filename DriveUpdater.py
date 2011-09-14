import os
import sys
import ftplib
from Tkinter import *
from tkFileDialog import *
from xml.sax.saxutils import quoteattr as xml_quoteattr

# Settings

# FTP address, username, password
ftp = ''
username = ''
password = ''

# Directory on the FTP that stores all XML files
xml_directory = ''




x = 1
dirname = ""

class GUI(Frame):      
        
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        t = StringVar()
        self.entry = Entry(Frame(master), textvariable=t)
    
    def callback():
        print "callback"
    
    def openDirectory(self):
        global dirname 
        dirname = askdirectory(parent=root, title="TITLE") 
    
    def createWidgets(self):
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "Upload and Quit"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "bottom"})

        self.OPEN = Button(self)
        self.OPEN["text"] = 'Select drive to map'
        self.OPEN["command"] =  self.openDirectory
        self.OPEN.pack({"side": "top"})
        

    
def nodot(item): return item[0] != '.'

def DirXML(path):
            global x
        
            if x<2:
                result = '<item rel="drive" id="%(number)03d"> \n<content><name> %(pathname)s </name></content> \n' %{"number":x, "pathname":xml_quoteattr(os.path.basename(path))}
            else:
                result = '<item rel="folder" id="%(number)03d"> \n<content><name> %(pathname)s </name></content> \n' %{"number":x, "pathname":xml_quoteattr(os.path.basename(path))}
           
            for item in filter(nodot, os.listdir(path)):
                itempath = os.path.join(path, item)
                if os.path.isdir(itempath):
                    x = x + 1
                    result += '\n'.join('  ' + line for line in 
                        DirXML(os.path.join(path, item)).split('\n'))
                elif os.path.isfile(itempath):
                    x = x + 1
                    result += '<item rel="file" id="%(number)03d"> \n<content><name>%(pathname)s</name></content>\n</item>\n' %{"number":x, "pathname":xml_quoteattr(item)}    
            
            result += '</item> \n'
            output = result
            return output
       
        
if __name__ == '__main__':
    
    root = Tk() 
    root.geometry('250x100+500+200')
    root.title('Drive Map')
    app = GUI(root)
    root.mainloop()
    
    if len(dirname) != 0:
        outputname = (dirname + ".xml")
        a = open(outputname, "w")
        ftp = ftplib.FTP(ftp)
        ftp.login(user = username, passwd = password)
        ftp.cwd(xml_directory) 
        a.write('<root>\n' + DirXML(dirname) + '\n</root>')
        a.close()
        f=open(outputname,'rb')
        ftp.storbinary('STOR '+os.path.basename(outputname),f)
        f.close()
        ftp.quit()
    else:
        print "No Drive Selected"

