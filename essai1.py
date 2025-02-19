from pix2text import Pix2Text

# Initialisation avec le processeur rapide
p2t = Pix2Text.from_config(use_fast=True)

# Traitement du PDF
img_fp = './docs/examples/test-doc.pdf'
doc = p2t.recognize_pdf(img_fp, page_numbers=[0, 1])
doc.to_markdown('output-md')  # Les informations Markdown exportées sont sauvegardées dans le répertoire output-md