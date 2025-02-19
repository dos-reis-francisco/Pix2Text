# MdMerger.py
# Auteur : Francisco Dos Reis
# Date : 2025-02-19
# Description : Fusion des fragments Markdown

import os
import re

class MdMerger:
    def __init__(self, outputDir='output-md'):
        self.outputDir = outputDir
        os.makedirs(outputDir, exist_ok=True)
    
    def mergePages(self, pageContents, baseName='document'):
        outputPath = os.path.join(self.outputDir, f"{baseName}.md")
        sortedPages = sorted(pageContents.items())
        
        with open(outputPath, 'w', encoding='utf-8') as f:
            for pageNum, content in sortedPages:
                if content:
                    f.write(f"\n## Page {pageNum}\n\n")
                    f.write(content + "\n\n")
        
        return outputPath
