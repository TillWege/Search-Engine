import json
from os.path import isfile, join
from os import remove
import re
import typing

CONTENT_PATH = './content/'

def is_pdf_file(pFilename: str) -> bool:
    parts = pFilename.split('.')
    return parts[-1] == 'pdf'
        
def is_valid_file(pPotentialFile: str) -> bool:
    
    # check if the path is a File
    if not isfile(join(CONTENT_PATH, pPotentialFile)):
       return False
   
    # check if the file is a PDF-File
    return is_pdf_file(pPotentialFile)

def save_dict(pDict: typing.Dict[str, int], pFileName):
    file_path = join(CONTENT_PATH, pFileName)
    if isfile(file_path):
        remove(file_path)
    
    file = open(file_path, 'w')
    json.dump(pDict, file, ensure_ascii=False)
    
def cleanup_text(pText: str) -> str:
    pText = re.sub(r'\W+', ' ', pText)
    
    return pText.lower()
        
        