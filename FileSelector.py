# FileSelector.py
# Auteur : Francisco Dos Reis
# Date : 2025-02-19
# Description : Widget de sélection de fichier PDF avec validation

import tkinter as tk
from tkinter import filedialog

class PdfFileSelector(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(padx=10, pady=10)
        
        # Variables
        self.filePath = tk.StringVar()
        
        # Widgets
        self.label = tk.Label(self, text="Fichier PDF :")
        self.entry = tk.Entry(self, textvariable=self.filePath, width=40)
        self.browseButton = tk.Button(self, text="Parcourir", command=self.browseFile)
        
        # Layout
        self.label.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=1, column=0, sticky="ew")
        self.browseButton.grid(row=1, column=1, padx=5)
        
        # Validation
        self.entry.configure(validate="focusout", validatecommand=self.validatePdf)
    
    def browseFile(self):
        filePath = filedialog.askopenfilename(
            title="Sélectionner un PDF",
            filetypes=[("Fichiers PDF", "*.pdf")]
        )
        if filePath:
            self.filePath.set(filePath)
            self.validatePdf()
    
    def validatePdf(self):
        path = self.filePath.get()
        if path.lower().endswith('.pdf'):
            return True
        self.entry.config(foreground="red")
        return False
