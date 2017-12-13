from tkinter import *
import pickle
from passdat import *
import random

db = {}

try:
    with open('passdb', 'rb') as file_obj:
        db = pickle.load(file_obj)
except:
    pass

class App(Frame):
    #Master Section
    def __init__(self, master, db):
        Frame.__init__(self)
        self.master.title("OpenSezMe")
        self._topFrame = Frame(master)
        self._topFrame.pack()
        self._bottomFrame = Frame(master)
        self._bottomFrame.pack()

        #Entry Variables
        self._siteVar = StringVar()
        self._userVar = StringVar()
        self._passVar = StringVar()
        self._lenVar = IntVar()
        self._alpVar = BooleanVar()
        self._numVar = BooleanVar()
        self._specVar = BooleanVar()
        self._showVar = BooleanVar()

        #Website Section
        self._siteLabel = Label(self._topFrame, text="Website")
        self._siteLabel.grid(row=1, column=0)
        self._siteEntry = Entry(self._topFrame,font=("Menlo", 14), textvariable=self._siteVar)
        self._siteEntry.grid(row=1, column=1, sticky=W)

        #Username Section
        self._userLabel = Label(self._topFrame, text = "Username")
        self._userLabel.grid(row=2, column=0)
        self._userEntry = Entry(self._topFrame, font=("Menlo", 14), textvariable=self._userVar)
        self._userEntry.grid(row=2, column=1, sticky = W)

        #Password Section
        self._passLabel = Label (self._topFrame, text='Password')
        self._passLabel.grid(row=3, column=0, padx=5)
        self._passEntry = Entry(self._topFrame, font=("Menlo", 14), textvariable=self._passVar)
        self._passEntry.grid(row=3, column=1, sticky=W)

        #Database Section
        self._yscroll = Scrollbar(self._bottomFrame, orient=VERTICAL)
        self._yscroll.grid(row=0, column=2, sticky= N+S)
        self._theList = Listbox(self._bottomFrame, width=22, height=8, selectmode=SINGLE,yscrollcommand=self._yscroll.set)
        self._theList.grid(row=0, column=1, sticky = N+S+E)
        self._yscroll['command'] = self._theList.yview
        self._theList.bind("<ButtonRelease-1>", self.activeEnt)
        for key in db.keys():
            self._theList.insert(END, key)

        #Button Section
        self._newButton = Button(self._topFrame, text="New", command = self.newEntry)
        self._newButton.grid(row=0, column=0)
        self._genButton = Button(self._bottomFrame, text="Generate Password", command = self.genPass)
        self._genButton.grid(row=3, column=2, sticky=W)
        self._saveButton = Button(self._topFrame, text='Save', command=self.saveEntry)
        self._saveButton.grid(row=0, column=2)
        self._delButton = Button(self._topFrame, text="Delete", command = self.delEnt)
        self._delButton.grid(row=0, column=1)
        
        #CheckBox Setion
        self._alpCk = Checkbutton(self._bottomFrame, text='Alph.', variable=self._alpVar)
        self._alpCk.grid(row=1, column=0)
        self._numCk = Checkbutton(self._bottomFrame, text='Num.', variable=self._numVar)
        self._numCk.grid(row=1, column=1)
        self._specCk = Checkbutton(self._bottomFrame, text='Spec.', variable = self._specVar)
        self._specCk.grid(row=1, column=2)
        self._showCk = Checkbutton(self._topFrame, text = 'Show', variable= self._showVar, command=self.switchShow)
        self._showCk.grid(row=3, column=2)

        #Length Section
        self._lenLabel = Label(self._bottomFrame, text='Length')
        self._lenLabel.grid(row=2, column=1)
        self._lenEntry = Entry(self._bottomFrame, font=("Menlo", 14), textvariable=self._lenVar)
        self._lenEntry.grid(row=3, column=1, sticky=E)

    def saveEntry(self):
        if self._passVar.get() == "********":
           self._passVar.set(db[self._siteVar.get()]._pass) 
               
        ent = PassEntry(self._siteVar.get(), self._userVar.get(), self._passVar.get())
        db[ent._site] = ent
        list_flag = False
        for i, list_box in enumerate(self._theList.get(0, END)):
            if ent._site == list_box:
                list_flag = True  

        if (ent._site != "") and (list_flag == False):
            self._passVar.set(db[ent._site]._pass)
            self._theList.insert(END, ent._site)
            
        self._passVar.set(db[ent._site]._pass)
        with open('passdb', 'wb') as file_obj:
            pickle.dump(db, file_obj)
        self._passVar.set("********")
          
                    
    def newEntry(self):
        self._siteVar.set('')
        self._userVar.set('')
        self._passVar.set('')
        
    def activeEnt(self, event):
        if self._theList.size() > 0:
            index = self._theList.curselection()[0]
            self._siteVar.set(self._theList.get(index))
            self._userVar.set(db[self._theList.get(index)]._user)
            if self._showVar.get() == False: 
                self._passVar.set("********")
            else:
                self._passVar.set(db[self._theList.get(index)]._pass)
                
                 
    
    def delEnt(self):
        tmp = ''
        if self._theList.size() > 0:
            index = self._theList.curselection()[0]
            tmp = db[self._theList.get(index)]._site
            db.pop(tmp)
            self._theList.delete(ACTIVE)
            self._siteVar.set('')
            self._userVar.set('')
            self._passVar.set('')
            
                        
    def switchShow(self):
       
        if self._showVar.get() == False: 
            self._passVar.set("********")
        else:
            self._passVar.set(db[self._siteVar.get()]._pass)
            
            
            
    def revealPass(self):
        if self._theList.size() > 0:
            index = self._theList.curselection()[0]        
            self._passVar.set(db[self._theList.get(index)]._pass)
        
            
    def genPass(self):
        count = 0
        passw = []
        if (self._specVar.get() is True) and (self._numVar.get() is False) and (self._alpVar.get() is True):
            while count <= self._lenVar.get():
                randl = random.randint(33, 122)
                if (randl < 58) and (randl > 47):
                    continue
                else:
                    passw.append(chr(randl))
                    count += 1
                    
        elif (self._specVar.get() is False) and (self._numVar.get() is True) and (self._alpVar.get() is True):
            while count <= self._lenVar.get():
                randl = random.randint(48, 122)
                if (randl > 57) and (randl < 65):
                    continue
                elif (randl > 90) and (randl < 97):
                    continue
                else:
                    passw.append(chr(randl))
                    count += 1
                    
        elif (self._specVar.get() is True) and (self._numVar.get() is True) and (self._alpVar.get() is False):
            while count <= self._lenVar.get():
                randl = random.randint(33, 64)

                passw.append(chr(randl))
                count += 1

        elif (self._specVar.get() is True) and (self._numVar.get() is False) and (self._alpVar.get() is False):
            while count <= self._lenVar.get():
                randl = random.randint(33, 64)
                if (randl < 58) and (randl > 47):
                    continue
                else:
                    passw.append(chr(randl))
                    count += 1

        elif (self._specVar.get() is False) and (self._numVar.get() is True) and (self._alpVar.get() is False):
            while count <= self._lenVar.get():
                randl = random.randint(48, 57)
                passw.append(chr(randl))
                count += 1

        elif (self._specVar.get() is False) and (self._numVar.get() is False) and (self._alpVar.get() is True):
            while count <= self._lenVar.get():
                randl = random.randint(65, 122)
                if (randl > 90) and (randl < 97):
                    continue
                passw.append(chr(randl))
                count += 1

        elif (self._specVar.get() is True) and (self._numVar.get() is True) and (self._alpVar.get() is True):
            while count <= self._lenVar.get():
                randl = random.randint(33, 125)
                passw.append(chr(randl))
                count += 1
                
        passw = str(''.join(passw))
        self._passVar.set(passw)
            

root = Tk()
app = App(root, db)
root.mainloop()
