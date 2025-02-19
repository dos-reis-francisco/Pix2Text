# ParallelProcessor.py
# Auteur : Francisco Dos Reis
# Date : 2025-02-19
# Description : Traitement parallèle des pages PDF

import os
import concurrent.futures
from OcrWorker import OcrWorker

class ParallelProcessor:
    def __init__(self, maxWorkers=4):
        self.maxWorkers = maxWorkers
    
    def processPages(self, tempDir):
        pageFiles = sorted([os.path.join(tempDir, f) for f in os.listdir(tempDir) if f.endswith('.pdf')])
        results = {}
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.maxWorkers) as executor:
            futures = {executor.submit(self.processSinglePage, pageFile): pageFile for pageFile in pageFiles}
            
            for future in concurrent.futures.as_completed(futures):
                pageFile = futures[future]
                try:
                    result = future.result()
                    pageNum = int(os.path.basename(pageFile).split('_')[1].split('.')[0])
                    results[pageNum] = result
                except Exception as e:
                    print(f"Erreur sur {pageFile}: {str(e)}")
        
        return results
    
    def processSinglePage(self, pageFile):
        worker = OcrWorker()
        return worker.processPage(pageFile)
