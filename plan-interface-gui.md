# Plan d'implémentation de l'interface GUI parallèle

## Objectifs
- basé sur le modèle de départ "essai1.py"
- Interface graphique avec sélection de fichier PDF
- Traitement parallèle page par page
- Reconstruction automatisée du Markdown final

## Composants principaux

### 1. Interface Graphique (TKinter)
- `FileSelector.py` : Widget de sélection de fichier PDF
- `PageRangeSelector.py` : Sélection de plage de pages (spinbox)
- `ProgressLogger.py` : Affichage de la progression et logs

### 2. Gestion du PDF
- `PdfSplitter.py` : Découpage du PDF en pages individuelles
- `MdMerger.py` : Reconstruction du Markdown final

### 3. Traitement parallèle
- `ParallelProcessor.py` : Pool de workers avec `concurrent.futures`
- `OcrWorker.py` : Worker de traitement Pix2Text par page

## Étapes détaillées

### Phase 1 : Interface Utilisateur (2 jours)
1. Fenêtre principale avec grille responsive
2. Widgets de sélection PDF + validation
3. Bouton d'exécution avec gestion d'état

### Phase 2 : Traitement Parallèle (3 jours)
1. Découpage du PDF en pages temporaires
2. Pool de threads pour le traitement OCR
3. Gestion des exceptions par page

### Phase 3 : Reconstruction (1 jour)
1. Fusion des fragments Markdown
2. Nettoyage des fichiers temporaires
3. Génération du fichier final

## Journal de version
| Date       | Auteur              | Modification          |
|------------|---------------------|-----------------------|
| 2025-02-19 | Francisco Dos Reis | Création du plan initial |
