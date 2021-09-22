import json

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt


from Fuzzy.fuzzy_set import FuzzySetTringular,FuzzySetTringularSymetric
from Fuzzy.universe import Universe

TRINGULAR = 0
TRINGULAR_SYMMETRIC=1

class FrameUniverse(ttk.Frame):
    def __init__(self,label_name, **kw):
        super().__init__(**kw)
        # man frame info
        self.main_label = ttk.Label(self,text=label_name,font=('Helvatical bold',25))
        self['borderwidth'] = 5
        self['relief'] = 'sunken'
        self.destroy_button=tk.Button(self,text='destroy universe',command=self.destroy)
        self.fuzzy_sets_frames=[]
        self.figure=plt.figure('label_name')

        # Add fuzzy set widgets
        self.label_of_fuzzy_set = tk.Label(self, text='Type label:')
        self.entry_label = tk.Entry(self)
        self.label_add_fuzzy_set = tk.Label(self,text='Choose type of fuzzy set:')
        self.cb_type_of_fuzzy_set = ttk.Combobox(self)
        self.cb_type_of_fuzzy_set['values'] = ['tringular (normal)','tringular symetric']
        self.cb_type_of_fuzzy_set['state']='readonly'
        self.cb_type_of_fuzzy_set.current(0)
        self.button_add_fuzzy_set= tk.Button(self,text='Add',command=self.addFuzzySet)
        self.button_draw= tk.Button(self,text='Draw/Update Universe',command=self.draw)
        self.button_save = tk.Button(self,text='Save',command=self.save)


        # Place widgets
        self.main_label.grid(column=0,row=0)
        self.destroy_button.grid(column=12,row=0)
        self.label_of_fuzzy_set.grid(column=0, row=1)
        self.entry_label.grid(column=1, row=1)
        self.label_add_fuzzy_set.grid(column=2,row=1)
        self.cb_type_of_fuzzy_set.grid(column=3,row=1)
        self.button_add_fuzzy_set.grid(column=4,row=1)
        self.button_draw.grid(column=0, row=2)
        self.button_save.grid(column=1, row=2)


        self.grid_columnconfigure(10,weight=1)

    def draw(self):
        if len(self.fuzzy_sets_frames)==0:
            return None
        fuzzy_sets=[]
        for fsf in self.fuzzy_sets_frames:
            try:
                if fsf.type == TRINGULAR:
                    fuzzy_sets.append(FuzzySetTringular(fsf.label_name['text'],fsf.getPoints()))
                elif fsf.type == TRINGULAR_SYMMETRIC:
                    fuzzy_sets.append(FuzzySetTringularSymetric(fsf.label_name['text'], fsf.getPoints()))
            except:
                pass
        uni = Universe(fuzzy_sets,self.main_label['text'])
        uni.draw(self.figure)
        plt.show()

    def save(self):
        dictionary={}
        if len(self.fuzzy_sets_frames)==0:
            return None
        for fsf in self.fuzzy_sets_frames:
            dictionary[fsf.label_name['text']]={
                'type':fsf.type,
                'points':fsf.getPoints()
            }
        json_object = json.dumps(dictionary, indent=4)
        with open(self.main_label['text'], "w") as outfile:
            outfile.write(json_object)

    def getDataFromJson(self,json):
        for key in json:
            self.addFuzzySet(name=key,type=json[key]['type'],points=json[key]['points'])

    def addFuzzySet(self,name=None,type=None,points=None):
        if name is None:
            name=self.entry_label.get()
        if type is None:
            type=self.cb_type_of_fuzzy_set.current()
        new_frame= FrameFuzzySet(name,type,master=self,
                                 highlightbackground="blue", highlightthickness=3)
        if points is not None:
            new_frame.setPoints(points)
        self.fuzzy_sets_frames.append(new_frame)
        new_frame.grid(column=0,row=len(self.fuzzy_sets_frames)+2,columnspan=13,sticky='nwse')

class FrameFuzzySet(tk.Frame):
    def __init__(self,name,type, **kw):
        super().__init__(**kw)
        self.label_name = tk.Label(self,text=name,font=('Helvatical bold',20))
        self.type=type
        self.entries_for_fuzzy_set=[]
        self.destroy_button = tk.Button(self, text='destroy set', command=self.destroy)
        if type==TRINGULAR:
            self.generateInputs(['Left vertex:','Middle vertex:','Right vertex:'])
        elif type==TRINGULAR_SYMMETRIC:
            self.generateInputs(['Left vertex:','Right vertex:'])
        self.label_name.grid(column=0,row=0)
        self.destroy_button.grid(column=11,row=0)
        self.grid_columnconfigure(10, weight=1)

    def generateInputs(self,string_labels):
        for i,sl in enumerate(string_labels):
            tk.Label(self,text=sl).grid(row=1,column=i*2)
            e = tk.Entry(self)
            self.entries_for_fuzzy_set.append(e)
            e.grid(row=1,column=i*2+1)

    def getPoints(self):
        out=[]
        for e in self.entries_for_fuzzy_set:
            out.append(float(e.get()))
        return out

    def setPoints(self,points):
        for e,p in zip(self.entries_for_fuzzy_set,points):
            e.insert(0,str(p))
