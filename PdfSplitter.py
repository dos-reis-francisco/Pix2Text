# PdfSplitter.py
# Auteur : Francisco Dos Reis
# Date : 2025-02-19
# Description : Découpage d'un PDF en pages individuelles

import os
import shutil
import tempfile
from PyPDF2 import PdfReader, PdfWriter

class PdfSplitter:
    def __init__(self, pdfPath):
        if not os.path.isfile(pdfPath):
            raise FileNotFoundError(f"Fichier PDF introuvable : {pdfPath}")
        
        self.pdfPath = pdfPath
        self.tempDir = tempfile.mkdtemp(prefix="pix2text_split_")
        
    def splitPages(self, pageNumbers):
        """
        Découpe le PDF en pages individuelles
        :param pageNumbers: Liste triée des numéros de pages (commençant à 1)
        :return: Dossier temporaire contenant les pages découpées
        """
        try:
            with open(self.pdfPath, "rb") as f:
                reader = PdfReader(f)
                totalPages = len(reader.pages)
                
                for pageNum in pageNumbers:
                    if pageNum < 1 or pageNum > totalPages:
                        raise ValueError(f"Numéro de page invalide : {pageNum}")
                    
                    writer = PdfWriter()
                    writer.add_page(reader.pages[pageNum-1])
                    
                    outputPath = os.path.join(self.tempDir, f"page_{pageNum:04d}.pdf")
                    with open(outputPath, "wb") as outputFile:
                        writer.write(outputFile)
            
            return self.tempDir
        
        except Exception as e:
            self.cleanup()
            raise
    
    def cleanup(self):
        """Nettoie le dossier temporaire"""
        if os.path.exists(self.tempDir):
            shutil.rmtree(self.tempDir)
