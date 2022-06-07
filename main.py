from tkinter import Tk
from tkinter import Button
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import *
import webbrowser
import os
import Update_Launcher

current_directory = os.getcwd()
print(current_directory)

dir = os.path.join("outputs")
if not os.path.exists(dir):
    os.mkdir(dir)

def supercede_plist():
    # Open plist to search
    with open(filename, 'r') as fh:
        plist_lines = [str(line) for line in fh]

    with open(filename1, 'r') as fh:
        patlist = [str(line).strip('\n') for line in fh]

    search_enabled = False
    plist_length = len(plist_lines)
    full_pattern_list = []
    plists = plist.get().replace(" ", "").split(",")
    plist_to_search = plists
    keep_pat = var1.get()

    # loop for individual search
    for plist_search in plist_to_search:
        for line_i in range(plist_length):
            # Grabbing current line as string
            current_line = plist_lines[line_i]

            if (plist_search in current_line) and ('{' in current_line):
                search_enabled = True
            elif '}' in current_line:
                search_enabled = False
            elif search_enabled:
                if keep_pat == 1:
                    if 'Pat ' in current_line and current_line.replace('Pat ',' ').replace(';','').strip().upper() in patlist:
                        print('keeping: ', current_line)
                    elif 'Pat ' in current_line:
                        plist_lines[line_i] = current_line.replace('Pat ', '#Pat ')
                        pattern_to_add = current_line.replace('Pat ',' ').replace(';','').strip().upper()
                        full_pattern_list.append(pattern_to_add)
                elif keep_pat == 0:
                    if  'Pat ' in current_line and current_line.replace('Pat ',' ').replace(';','').strip().upper() in patlist:
                        plist_lines[line_i] = current_line.replace('Pat ', '#Pat ')
                        pattern_to_add = current_line.replace('Pat ',' ').replace(';','').strip().upper()
                        full_pattern_list.append(pattern_to_add)
                    elif 'Pat ' in current_line:
                        print('keeping: ', current_line)


    with open(current_directory + "//outputs//supercede_plist.plist", 'w') as file:
        for line in plist_lines:
            print(line, end="", file=file)

def select_file():
    global filename
    filetypes = (
        ('text files', '*.plist'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

def select_file1():
    global filename1
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename1 = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename1
    )


### Main Root
root = Tk()
root.title('Need4Seed v1.00 [Beta]')

tab_parent = ttk.Notebook(root)

tab1 = ttk.Frame(tab_parent, padding="20 30 20 50")
tab2 = ttk.Frame(tab_parent, padding="60 50 60 50")

tab_parent.add(tab1, text='Pattern Removal Supersede Plist')
tab_parent.add(tab2, text='Coming Soon')
tab_parent.grid(sticky=('news'))

def callback(url):
    webbrowser.open_new(url)

link1 = Label(tab1, text="Wiki: https://goto/need4seed", fg="blue", cursor="hand2")
link1.grid(row = 0,column = 0, sticky=W, columnspan = 2)
link1.bind("<Button-1>", lambda e: callback("https://gitlab.devtools.intel.com/ianimash/supercpg/-/wikis/Need4Seed"))

link2 = Label(tab1, text="IT support contact: sean.paul.gill@intel.com or idriss.animashaun@intel.com", fg="blue", cursor="hand2")
link2.grid(row = 1,column = 0, sticky=W, columnspan = 2)
link2.bind("<Button-1>", lambda e: callback("https://outlook.com"))

#### Tab 1
open_button = Button(
    tab1,
    text='Select plist file to modify',
    command=select_file,
    bg = 'brown', fg = 'white', font = '-family "SF Espresso Shack" -size 12'
)

open_button.grid(row = 2, column = 0)

open_button_1 = Button(
    tab1,
    text='Select list of patterns to edit',
    command=select_file1,
    bg = 'blue', fg = 'white', font = '-family "SF Espresso Shack" -size 12'
)

open_button_1.grid(row = 3, column = 0)

var1 = IntVar(value=1)
Checkbutton(tab1, text="Keep these patterns", variable=var1).grid(row=3, column = 1, sticky=W)

plist = Entry(tab1, width=35, relief = FLAT)
plist.insert(4,"Enter Nested plists to Modify")
plist.grid(row = 4, column = 0)

button_0 = Button(tab1, text="Generate Supercede plist", height = 1, width = 20, command = supercede_plist, bg = 'green', fg = 'white', font = '-family "SF Espresso Shack" -size 12')
button_0.grid(row = 5, column = 0, rowspan = 2 )


# #### Tab 2

### Main loop
root.mainloop()