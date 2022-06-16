# Suchmaschine Mathe 
## Deutsch
### Projekt
Bei diesem Projekt handelt es sich um eine simple Suchmaschiene welche PDF-Dokumente durchsucht. Für eine Übergebene Zeichenkette wird das Dokument zurückgegeben welches am ähnlichsten ist.
### Verwendung
1. Python installieren (wenn noch nicht vorhanden)
2. Die benötigten Python Packete mit `pip install -r requirements.txt` installieren
3. Die zu durchsuchenden Dateien als PDF-Dateien im Ordner *content* ablegen
4. Alle Dateien Indizieren lassen `python main.py -index`
5. Mithilfe des Skriptes suchen `python main.py "hier die suchanfrage eingeben"` (die anführungsstriche sind nicht optional)
### Quellen für den Beispiel-Content
Alle in diesem Repository abgelegten Bücher sind von http://www.digbib.org/
## English
### Project
This project is supposed to be a simple searchengine which can scan through a set of PDF-Documents. For a given String it returns the Document which it deems to be the most related
### How to Use
1. Install Python (if not yet installed)
2. Install the required packages with `pip install -r requirements.txt`
3. Place the PDF-Files which are to be searched in the *content* folder
4. Index all files with `python main.py -index`
5. Search by using `python main.py "enter search query"` (the quotes around the query are not optional)
### Source for the example content
All Books which are included in this repository are from http://www.digbib.org/