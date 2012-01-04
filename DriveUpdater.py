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
        
        # Only two buttons in the program Select Drive (for uploading) and Upload and Quit (which actually triggers the script to send the file to the ftp
        self.QUIT = Button(self)
        self.QUIT["text"] = "Upload and Quit"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "bottom"})

        self.OPEN = Button(self)
        self.OPEN["text"] = 'Select drive to map'
        self.OPEN["command"] =  self.openDirectory
        self.OPEN.pack({"side": "top"})
        

# Does not return items that have a period as the first character (used to ignore OS X hidden files)
def nodot(item): return item[0] != '.'

def DirXML(path):
            global x
        
            # If x<2 there are no nodes higher so this folder is classified as a "drive"        
            if x<2:
                result = '<item rel="drive" id="%(number)03d"> \n<content><name> %(pathname)s </name></content> \n' %{"number":x, "pathname":xml_quoteattr(os.path.basename(path))}
            # Anything with nodes below it and above it is then classified as a "folder"
            else:
                result = '<item rel="folder" id="%(number)03d"> \n<content><name> %(pathname)s </name></content> \n' %{"number":x, "pathname":xml_quoteattr(os.path.basename(path))}
           
            for item in filter(nodot, os.listdir(path)):
                itempath = os.path.join(path, item)
                # If the program comes across another subdirectory it restarts the script and continues down the tree
                if os.path.isdir(itempath):
                    x = x + 1
                    result += '\n'.join('  ' + line for line in 
                        DirXML(os.path.join(path, item)).split('\n'))
                # If the program comes across a file it uses the file's path to pull out the file name and give it a "file" classification
                elif os.path.isfile(itempath):
                    x = x + 1
                    result += '<item rel="file" id="%(number)03d"> \n<content><name>%(pathname)s</name></content>\n</item>\n' %{"number":x, "pathname":xml_quoteattr(item)}    
            
            #Adds closing markup after the loop
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
        # Creates the XML file with the same name as the drive for easy identification
        outputname = (dirname + ".xml")
        a = open(outputname, "w")
        ftp = ftplib.FTP(ftp)
        # Logs into FTP
        ftp.login(user = username, passwd = password)
        ftp.cwd(xml_directory) 
        # Writes root markup along with the file tree
        a.write('<root>\n' + DirXML(dirname) + '\n</root>')
        a.close()
        f=open(outputname,'rb')
        ftp.storbinary('STOR '+os.path.basename(outputname),f)
        f.close()
        ftp.quit()
    else:
        print "No Drive Selected"

