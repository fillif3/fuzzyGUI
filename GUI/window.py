import tkinter as tk
from tkinter import ttk
import json


from GUI.frame_universe import FrameUniverse

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
        with open(t1_entry.get(), 'r') as openfile:
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
    ttk.Label(tab2,
              text="Lets dive into the\
              world of computers").grid(column=0,
                                        row=0,
                                        padx=30,
                                        pady=30)

    root.mainloop()