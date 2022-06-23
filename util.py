import json
from os.path import isfile, join
from os import remove, listdir
import re
import typing
from math import sqrt

CONTENT_PATH = './content/'

def is_pdf_file(pFilename: str) -> bool:
    parts = pFilename.split('.')
    return parts[-1] == 'pdf'

def is_json_file(pFilename: str) -> bool:
    parts = pFilename.split('.')
    return parts[-1] == 'json'
        
def is_valid_pdf_file(pPotentialFile: str) -> bool:
        # check if the path is a File
    if not isfile(join(CONTENT_PATH, pPotentialFile)):
       return False
   
    # check if the file is a PDF-File
    return is_pdf_file(pPotentialFile)

def is_valid_json_file(pPotentialFile: str) -> bool:
    # check if the path is a File
    if not isfile(join(CONTENT_PATH, pPotentialFile)):
       return False
   
    # check if the file is a JSON-File
    return is_json_file(pPotentialFile)
    

def save_dict(pDict: typing.Dict[str, int], pFileName):
    file_path = join(CONTENT_PATH, pFileName)
    if isfile(file_path):
        remove(file_path)
    
    file = open(file_path, 'w')
    json.dump(pDict, file, ensure_ascii=False, indent=4)
    
def load_dict(pFileName: str) -> typing.Dict:
    file_path = join(CONTENT_PATH, pFileName)
    file = open(file_path, 'r')

    return json.load(file)
        
def cleanup_text(pText: str) -> str:
    pText = re.sub(r'\W+', ' ', pText)
    
    return pText.lower()
        
def calc_vec_length(index: typing.Dict[str, int]) -> int:
    sum = 0
    for val in index.values():
        sum += val * val
        
    return sqrt(sum)

def get_pdf_content_files():
    all_files = listdir(CONTENT_PATH)
    pdf_files = [file for file in all_files if is_valid_pdf_file(file)]
    return pdf_files