# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:47:08 2019
cmd convertion: pyinstaller.exe --onefile --icon=myicon.ico main.py
@author: Ani Verzivolli
"""


##******************************
## import and setup
from tkinter import *
import os
import tkinter.messagebox
import comtypes.client
from tkinter import ttk



##******************************
## getting working directory
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)# for the moment gives C:\users\c.r.c
#scriptpath = os.path.realpath(__file__)#not working since it goes directly to cmd
#print("Script path is : " + os.path.dirname(os.path.realpath(__file__)))

## Word document location
Word_VBA_path = r"F:\Dropbox\TENDERA\Dokumente Standarde Tenderi\Dokumentet Stadarde të procedurës së hapur shërbime\Automation approach\Dokumentet Stadarde te procedures se hapur sherbime\Assets\Shtojcat\Shtojca - template - Copy.docm"
Word_VBA_macro = "mainSub"
OutputFolder = r"F:\Dropbox\TENDERA\Dokumente Standarde Tenderi\Dokumentet Stadarde të procedurës së hapur shërbime\Automation approach"

## defining program variables/constants
## defining dst list for radio
DST_list = [["Procedurë e kufizuar pune", None],
            ["Procedurë e hapur pune", None],
            ["Neg pa shpallje pune", None],
            ["Neg me shpallje pune", None],
            ["Kërkesë për propozim pune", None],
            
            ["Procedurë e kufizuar mallra", None],
            ["Procedurë e hapur mallra", None],
            ["Neg pa shpallje mallra", None],
            ["Neg me shpallje mallra", None],
            ["Kërkesë për propozim mallra", None],
            
            ["Neg pa shpallje shërbime", None],
            ["Neg me shpallje shërbime", None],
            ["Procedurë e kufizuar shërbime", None],
            ["Kërkesë për propozim shërbime", None],
            ["Procedurë e hapur shërbime", r"F:\Dropbox\TENDERA\Dokumente Standarde Tenderi\Dokumentet Stadarde të procedurës së hapur shërbime\Automation approach\Dokumentet Stadarde te procedures se hapur sherbime\Assets\Shtojcat\Shtojca - template - Copy.docm"],
            
            ["Shërbim konsulence", None],
            ["Konkurs projektimi", None]]
## Defining list of input variables Enty widgets
entries = [['Autoriteti kontraktor:','Autoriteti kontraktor; shembull: Bashkia Tiranë'],
           ['Objekti:','Objekti'],
           ['Fondi limit:','Fondi limit; shembull: 190,000.00 Lekë Pa TVSH'],
           ['Data e zhvillimit të prokurimit:','Data e zhvillimit të prokurimit; shembull1: 25.01.2020; shembull2: 25 Janar 2020'],
           ['Ora e zhvillimit të prokurimit:','Ora e zhvillimit të prokurimit; shembull: 11:25 (formati i preferuar)']]
entryLabelsColumn = 0
entryLabelsColumnspan = 2
entryColumn = 2
entryColumnspan = 5
##******************************
## Tkinter
## Setting options
root = Tk()
root.title('UTS-01 Sh.p.k. Dokumenta tenderi')
#root.columnconfigure(0, weight = 1)
#root.columnconfigure(1, weight = 1)
##******************************
## defining functions

class ToggledFrame(Frame):

    def __init__(self, parent, text="", *args, **options):
        Frame.__init__(self, parent, *args, **options)

        self.show = IntVar()
        self.show.set(0)
        self.text = StringVar()

        self.title_frame = Frame(self)
        self.title_frame.pack(fill="x", expand=1)

        self.title_label = Label(self.title_frame, textvariable=self.text).pack(side="left", fill="x", expand=1)
        self.text.set(text)
        
        self.toggle_button = ttk.Checkbutton(self.title_frame, width=10, text='+', command=self.toggle,
                                            variable=self.show, style='Toolbutton')
        self.toggle_button.pack(side="right", ipadx = 9)

        self.sub_frame = Frame(self, relief="sunken", borderwidth=1)

    def toggle(self):
        if bool(self.show.get()):
            self.sub_frame.pack(fill="x", expand=1)
            self.toggle_button.configure(text='-')
        else:
            self.sub_frame.forget()
            self.toggle_button.configure(text='+')
    
    def changeText(self, new_text):
        self.text.set(new_text)
      
def createLabel( text, row, col, rowspan = 1, colspan = 1, sticky =  'e'):
    tmp_label_holder = Label(root, text = text)
    tmp_label_holder.grid(row = row, column = col, rowspan = rowspan, columnspan = colspan, sticky = sticky)
    return tmp_label_holder

def createEntryWithPlaceholder( textHolder, row, col, rowspan = 1, colspan = 1, width = 20):
    tmp_entry_holder = EntryWithPlaceholder(root, placeholder = textHolder, width = width)
    tmp_entry_holder.grid(row = row, column = col, rowspan = rowspan, columnspan = colspan)
    return tmp_entry_holder

class EntryWithPlaceholder(Entry):
    def __init__(self, master = None, placeholder = "PLACEHOLDER", width = 20, color = 'grey'):
        super().__init__(master, width = width)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

def evaluateEach(entry):
    if entry.get() == entry.placeholder or len(entry.get().strip()) == 0:
        return None
    else:
        return entry.get().strip()

def evaluate():
    root.focus()
    results = []
    for entry in entry_widgets:
        results.append(evaluateEach(entry))
    return results

def run():
    results = evaluate()
    if None in results:
        tkinter.messagebox.showinfo("Info", "Të paktën njëra nga fushat rezulton e paplotësuar")
        return
    runVBACode( path = Word_VBA_path,
               macro = Word_VBA_macro,
               ak = results[0],
               obj = results[1],
               fl = results[2],
               data = results[3],
               ora = results[4],
               outputFolder = OutputFolder)
        #print(result)

def runVBACode(path, macro, ak, obj, fl, data, ora, outputFolder):
    word=comtypes.client.CreateObject("Word.Application")
    docm=word.Documents.Open(path, ReadOnly=1)
    try:
        docm=word.Application.Run(macro, ak, obj, fl, data, ora, outputFolder)
    except:
        pass
    #word.Application.Run(macro, ak, obj, fl, data, ora)
    word.Documents(1).Close(SaveChanges=False)
    word.Application.Quit()
    tkinter.messagebox.showinfo("Info", "File pdf u krijua me sukses")
#    print("last line of runVBACode")
    
def DSTRadioClick():
    global t
    t.changeText(DST_list[v.get()][0])

##******************************
## adding widgets
entry_labels = []
entry_widgets = []
for index, entry in enumerate(entries):
    row = index
    
    temp_entry_holder = createEntryWithPlaceholder(textHolder = entry[1], row = row, col = entryColumn, width = 75, colspan = entryColumnspan)
    global entry_widgets
    entry_widgets.append(temp_entry_holder)
    
    temp_label_holder = createLabel( text = entry[0], row = row, col = entryLabelsColumn, colspan = entryLabelsColumnspan)
    global entry_labels
    entry_labels.append(temp_label_holder)

t = ToggledFrame(root, text='Procedurë e hapur shërbime', relief="raised", borderwidth=1)
t.grid(row = 6, column = 0, columnspan = 7, sticky = 'we')

v = IntVar()
DST_radio = []
for index, DST in enumerate(DST_list):
    radio = ttk.Radiobutton(t.sub_frame, text=DST[0], variable=v, value=index, command = DSTRadioClick).pack(anchor = 'w')
v.set('Procedurë e hapur shërbime')
#Label(t.sub_frame, text='Rotation [deg]:').pack(side="left", fill="x", expand=1)
#Entry(t.sub_frame).pack(side="left")
#radio = Radiobutton(root, text=DST[0][0], variable=v, value=index).pack()

#v = IntVar()    
#for index, DST in enumerate(DST_list):
#    Radiobutton(root, text=DST[0], variable=v, value=index).grid(row = DST[1], column = DST[2])
run_btn = Button(root, text = 'Ekzekuto', command = lambda:run())
run_btn.grid(row = 8, column = 0, rowspan = 1, columnspan = 7)

#cbutton = Checkbutton(root, text = 'Remember password')
#cbutton.grid(columnspan = 2)
##******************************

root.mainloop()
