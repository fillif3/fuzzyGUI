import tkinter as tk
from tkinter import ttk

TRINGULAR = 0
TRINGULAR_SYMMETRIC=1

class FrameUniverse(ttk.Frame):
    def __init__(self,label_name, **kw):
        super().__init__(**kw)
        # man frame info
        self.main_label = ttk.Label(self,text=label_name,font=('Helvatical bold',25))
        self['borderwidth'] = 5
        self['relief'] = 'sunken'
        self.destroy_button=tk.Button(self,text='destroy',command=self.destroy)

        # Add fuzzy set widgets
        self.label_add_fuzzy_set = tk.Label(self,text='Choose type of fuzzy set')
        self.cb_type_of_fuzzy_set = ttk.Combobox(self)
        self.cb_type_of_fuzzy_set['values'] = ['tringular','tringular symetric']
        self.cb_type_of_fuzzy_set['state']='readonly'
        self.cb_type_of_fuzzy_set.current(0)
        self.button_add_fuzzy_set= tk.Button(self,text='Add')


        # Place widgets
        self.main_label.grid(column=0,row=0)
        self.destroy_button.grid(column=12,row=0)
        self.label_add_fuzzy_set.grid(column=0,row=1)
        self.cb_type_of_fuzzy_set.grid(column=1,row=1)
        self.button_add_fuzzy_set.grid(column=2,row=1)



        self.grid_columnconfigure(10,weight=1)

    def addFuzzySet(self):
        if TRINGULAR

class FrameFuzzySet(ttk.Frame):
    def __init__(self,type, **kw):
        super().__init__(**kw)
