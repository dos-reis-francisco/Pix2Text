# MainWindow.py
# Auteur : Francisco Dos Reis
# Date : 2025-02-19
# Modification : Traitement direct du PDF comme dans essai1.py

import tkinter as tk
from tkinter import ttk, messagebox
from FileSelector import PdfFileSelector
from PageRangeSelector import PageRangeSelector
from OcrWorker import OcrWorker
import os
import logging
import sys
import traceback

# Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pix2text_gui.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pix2Text GUI")
        self.geometry("600x400")
        
        # Composants
        self.fileSelector = PdfFileSelector(self)
        self.pageRangeSelector = PageRangeSelector(self, maxPages=100)
        self.runButton = ttk.Button(self, text="Exécuter", command=self.runProcess)
        self.progressBar = ttk.Progressbar(self, mode="determinate")
        self.statusLabel = ttk.Label(self, text="")
        
        # Layout
        self.fileSelector.pack(fill="x", padx=10, pady=5)
        self.pageRangeSelector.pack(fill="x", padx=10, pady=5)
        self.runButton.pack(pady=10)
        self.progressBar.pack(fill="x", padx=10)
        self.statusLabel.pack(pady=5)
        
    def updateProgress(self, current, total):
        progress = (current / total) * 100
        self.progressBar["value"] = progress
        self.statusLabel["text"] = f"Traitement de la page {current}/{total}"
        self.update()
        
    def handleError(self, error, context=""):
        error_msg = str(error)
        logging.error(f"Erreur dans {context}: {error_msg}")
        logging.error(traceback.format_exc())
        return error_msg
        
    def runProcess(self):
        self.runButton.config(state="disabled")
        self.progressBar["value"] = 0
        
        try:
            pdfPath = self.fileSelector.filePath.get()
            pageRange = self.pageRangeSelector.pageRange.get()
            
            if not pdfPath:
                raise ValueError("Veuillez sélectionner un fichier PDF")
            
            logging.info(f"Traitement du fichier: {pdfPath}")
            logging.info(f"Plage de pages: {pageRange}")
            
            # Traitement OCR
            worker = OcrWorker()
            pageNumbers = self.pageRangeSelector.parsePageRange(pageRange)
            total_pages = len(pageNumbers)
            
            # Traitement du PDF complet
            self.statusLabel["text"] = "Traitement en cours..."
            self.progressBar["value"] = 50
            self.update()
            
            doc = worker.p2t.recognize_pdf(pdfPath, page_numbers=pageNumbers)
            if doc is None:
                raise ValueError("Échec de la reconnaissance OCR")
            
            # Sauvegarde en Markdown
            output_dir = "output-md"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(pdfPath))[0] + ".md")
            
            doc.to_markdown(output_dir)
            
            self.progressBar["value"] = 100
            self.statusLabel["text"] = "Traitement terminé"
            self.update()
            
            messagebox.showinfo("Succès", f"Traitement terminé.\nFichier généré : {output_path}")
            
        except Exception as e:
            error_msg = self.handleError(e, "Processus principal")
            messagebox.showerror("Erreur", error_msg)
            
        finally:
            self.runButton.config(state="normal")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
