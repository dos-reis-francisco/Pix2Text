# OcrWorker.py
# Auteur : Francisco Dos Reis
# Date : 2025-02-19
# Modification : Utilisation de recognize_pdf comme dans essai1.py

import logging
import sys
import os
import traceback
from pix2text import Pix2Text

class OcrWorker:
    def __init__(self):
        self.p2t = Pix2Text.from_config(use_fast=True)
        
        # Configuration du logging pour la console
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        self.logger = logging.getLogger('OcrWorker')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        
        logging.basicConfig(
            filename='ocr_processing.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def initializeModel(self):
        pass
    
    def processPage(self, pagePath):
        try:
            self.logger.info(f"Début traitement : {pagePath}")
            
            # Vérification du fichier
            if not os.path.exists(pagePath):
                self.logger.error(f"Fichier non trouvé : {pagePath}")
                return None
            
            # Reconnaissance OCR avec recognize_pdf
            self.logger.info("Lancement de la reconnaissance OCR...")
            doc = self.p2t.recognize_pdf(pagePath, page_numbers=[0])  # On traite une seule page
            
            if doc is None:
                self.logger.error(f"Échec de reconnaissance : {pagePath}")
                return None
            
            # Conversion en Markdown
            self.logger.info("Conversion en Markdown...")
            markdown = doc.to_markdown()
            
            if not markdown or not markdown.strip():
                self.logger.warning(f"Markdown vide généré : {pagePath}")
                return None
            
            self.logger.info(f"Traitement réussi : {pagePath}")
            return markdown
            
        except Exception as e:
            self.logger.error(f"Erreur lors du traitement : {str(e)}")
            self.logger.error(traceback.format_exc())
            return None
