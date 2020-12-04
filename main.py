#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

from googlesearch import search
import webbrowser

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_widgets()
        self.init_events()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(True, True)
        self.title('Google Search Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Window Events / Keyboard Shorcuts
    #-------------------------------------------
    def init_events(self):
        self.listbox.bind('<<ListboxSelect>>', self.open_link)

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        self.searchform = ttk.Frame(self)
        self.searchform.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.weblinks = ttk.Frame(self)
        self.weblinks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.fieldset1 = ttk.LabelFrame(self.searchform, text='Search')
        self.fieldset1.pack(side=tk.TOP, expand=True, padx=10, pady=10, fill=tk.BOTH)

        self.fieldset2 = ttk.LabelFrame(self.weblinks, text='Available Links')
        self.fieldset2.pack(side=tk.TOP, expand=True, padx=(0, 10), pady=10, fill=tk.BOTH)

        label = ttk.Label(self.fieldset1, text='Keyword')
        label.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10, pady=(10, 0))

        self.query = tk.StringVar()
        self.query.set('virama')
        entry = ttk.Entry(self.fieldset1, width=50, textvariable=self.query)
        entry.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10)

        label = ttk.Label(self.fieldset1, text='Number of Results')
        label.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10, pady=(10, 0))

        self.num = tk.IntVar()
        self.num.set(10)
        spinbox = ttk.Spinbox(self.fieldset1, from_=0, to=100, textvariable=self.num)
        spinbox.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10)

        label = ttk.Label(self.fieldset1, text='Last Result to Retrieve')
        label.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10, pady=(10, 0))

        self.stop = tk.IntVar()
        self.stop.set(20)
        spinbox = ttk.Spinbox(self.fieldset1, from_=0, to=100, textvariable=self.stop)
        spinbox.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10)

        label = ttk.Label(self.fieldset1, text='Pause')
        label.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10, pady=(10, 0))

        self.pause = tk.IntVar()
        self.pause.set(4)
        spinbox = ttk.Spinbox(self.fieldset1, from_=0, to=100, textvariable=self.pause)
        spinbox.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10)

        self.button = ttk.Button(self.fieldset1, text='Go', command=self.search_links)
        self.button.pack(side=tk.RIGHT, anchor=tk.W, padx=(0, 10), pady=10)

        # -------------------------------------------
        self.listbox = tk.Listbox(self.fieldset2, width=100)
        self.fieldset2.pack_forget()

    # -------------------------------------------
    def search_links(self):
        self.button.config(state=tk.DISABLED)
        self.listbox.delete(0, tk.END)  #clear listbox
        self.fieldset2.pack(side=tk.TOP, expand=True, padx=(0, 10), pady=10, fill=tk.BOTH)

        for link in search(query=self.query.get(), num=self.num.get(), stop=self.stop.get(), pause=self.pause.get()):
            self.listbox.insert(tk.END, link)

        self.listbox.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.button.config(state=tk.NORMAL)

    def open_link(self, *args):
        index = self.listbox.curselection()[0]
        item = self.listbox.get(index)

        if 'https://' in item:
            webbrowser.open_new(item)

#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()