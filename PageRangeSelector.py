# PageRangeSelector.py
# Auteur : Francisco Dos Reis
# Date : 2025-02-19
# Description : Widget de sélection de plage de pages PDF

import tkinter as tk
from tkinter import ttk

class PageRangeSelector(tk.Frame):
    def __init__(self, master, maxPages=100, **kwargs):
        super().__init__(master, **kwargs)
        self.maxPages = maxPages
        self.pageRange = tk.StringVar()
        
        # Widgets
        self.label = ttk.Label(self, text="Plage de pages :")
        self.entry = ttk.Entry(self, textvariable=self.pageRange, width=30)
        self.exampleLabel = ttk.Label(self, text="Ex: 1-5,7,9-12")
        
        # Layout
        self.label.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=1, column=0, padx=5, sticky="ew")
        self.exampleLabel.grid(row=1, column=1, padx=5)
        
        # Validation
        self.entry.configure(validate="focusout", validatecommand=self.validateInput)
    
    def validateInput(self):
        inputStr = self.pageRange.get().strip()
        if inputStr == "":
            return True
            
        try:
            pages = self.parsePageRange(inputStr)
            return len(pages) > 0 and max(pages) <= self.maxPages
        except ValueError:
            self.entry.config(foreground="red")
            return False
    
    def parsePageRange(self, inputStr):
        pages = set()
        for part in inputStr.split(','):
            part = part.strip()
            if '-' in part:
                start, end = map(int, part.split('-'))
                pages.update(range(start, end+1))
            else:
                pages.add(int(part))
        return sorted(pages)
