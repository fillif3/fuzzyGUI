import tkinter as tk
from tkinter import ttk
import json
import os

from Fuzzy import fuzzy_set
from Fuzzy.universe import Universe
from GUI.frame_universe import FrameUniverse, SimpleFrameUniverse, TRINGULAR, TRINGULAR_SYMMETRIC

def createWindow():
    root = tk.Tk()
    root.title("Tab Widget")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Create Universe')
    tabControl.add(tab2, text='Create Ruleset')
    tabControl.pack(expand=1, fill="both")

    ## Adding Universe (first tab)
    # Needed variables for the first tab
    universe_frames=[]

    # Acutal frame
    t1_Lab = ttk.Label(tab1,
              text="Add Universe with name")
    t1_entry = tk.Entry(tab1)

    def add_universe():
        frame = FrameUniverse(t1_entry.get(),master=tab1)
        universe_frames.append(frame)
        frame.grid(column=0,row=len(universe_frames)+1,columnspan=4, sticky='nwse')

    t1_But = tk.Button(tab1,text='Add',command=add_universe)

    def load_universe():
        frame = FrameUniverse(t1_entry.get(),master=tab1)
        universe_frames.append(frame)
        frame.grid(column=0,row=len(universe_frames)+1,columnspan=4, sticky='nwse')
        with open(t1_entry.get()+'.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
            frame.getDataFromJson(json_object)

    t1_But_load = tk.Button(tab1,text='Load',command=load_universe)



    t1_Lab.grid(column=0,row=0)
    t1_entry.grid(column=1, row=0, sticky='nwse')
    t1_But.grid(column=2, row=0)
    t1_But_load.grid(column=3, row=0)
    tab1.grid_columnconfigure(1, weight=1)


    # Adding Rules
    input_universe_frames = []
    output_universe_frame = []

    # Acutal frame
    def refresh():
        t2_cb['values']= [pos_json for pos_json in os.listdir(os.getcwd()) if pos_json.endswith('.json')]
        t2_cb.current(0)

    def getSimpleUniverseFrame(addational_text=''):
        with open(t2_cb.get(), 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        fuzzy_sets=[]
        for key in json_object:
            if json_object[key]['type']==TRINGULAR:
                fuzzy_sets.append(fuzzy_set.FuzzySetTringular(key,json_object[key]['points']))
            if json_object[key]['type'] == TRINGULAR_SYMMETRIC:
                fuzzy_sets.append(fuzzy_set.FuzzySetTringularSymetric(key, json_object[key]['points']))
        uni = Universe(fuzzy_sets,t2_cb.get())
        return SimpleFrameUniverse(uni,addational_text=addational_text, master=tab2)


    def addInput():
        frame = getSimpleUniverseFrame(addational_text=' (Input)')
        input_universe_frames.append(frame)
        frame.grid(column=0, row=len(input_universe_frames) + 2, columnspan=5, sticky='nwse')

    def addOutput():
        frame = getSimpleUniverseFrame(addational_text=' (Output)')
        output_universe_frame.append(frame)
        frame.grid(column=0, row=len(input_universe_frames) + 31, columnspan=5, sticky='nwse')

    def createRulesFrame():
        pass


    t2_ref_but = tk.Button(tab2,text='Refresh',command=refresh)
    t2_Lab = ttk.Label(tab2,
                       text="Choose a universe")
    t2_cb = ttk.Combobox(tab2)
    t2_but_input = tk.Button(tab2,text='Add Input',command=addInput)
    t2_but_output = tk.Button(tab2,text='Add Output',command=addOutput)
    tf2_but_create_Rule_table=tk.Button(tab2,text='Start creating rules',command=createRulesFrame)

    t2_ref_but.grid(column=0, row=0)
    t2_Lab.grid(column=1, row=0, sticky='nwse')
    t2_cb.grid(column=2, row=0)
    t2_but_input.grid(column=3, row=0)
    t2_but_output.grid(column=4, row=0)
    tf2_but_create_Rule_table.grid(column=5, row=0)
    tab1.grid_columnconfigure(1, weight=1)

    root.mainloop()