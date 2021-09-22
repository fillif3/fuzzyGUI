import tkinter as tk
from tkinter import ttk
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
        frame.grid(column=0,row=len(universe_frames)+1,columnspan=3, sticky='nwse')


    t1_But = tk.Button(tab1,text='Add',command=add_universe)



    t1_Lab.grid(column=0,row=0)
    t1_entry.grid(column=1, row=0, sticky='nwse')
    t1_But.grid(column=2, row=0)
    tab1.grid_columnconfigure(1, weight=1)
    # Adding Rules
    ttk.Label(tab2,
              text="Lets dive into the\
              world of computers").grid(column=0,
                                        row=0,
                                        padx=30,
                                        pady=30)

    root.mainloop()