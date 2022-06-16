from math import sqrt
import sys
import typing
import pdfplumber


from os import listdir
from util import CONTENT_PATH, is_valid_file, save_dict, cleanup_text
from multiprocessing import Pool, cpu_count
    
def main() -> int:
    # check input args
    print(sys.argv)
    if sys.argv[1] == '-index':
        print("Indexing files in the Content Folder")
        index()
    elif sys.argv[1] == '-search':
        query = sys.argv[2]
        print("Searching for " + query)
    else:
        print("Unknows command entered")

    return 0

def index():
    all_files = listdir(CONTENT_PATH)
    pdf_files = [file for file in all_files if is_valid_file(file)]

    with Pool(cpu_count() - 2) as threads:
        threads.map(index_file, pdf_files)
        
def index_file(file_path):
    index: typing.Dict[str, int] = {}
        
    pdf =  pdfplumber.open(CONTENT_PATH + file_path)
    pdf_text = ''
    for page in pdf.pages:
        pdf_text += page.extract_text()

    pdf_text = cleanup_text(pdf_text)
    
    words = pdf_text.split(' ')
    for word in words:
        if word in index:
            index[word] += 1
        else:
            index[word] = 1

    vec_len = calc_vec_length(index)

    index['vec_len'] = vec_len

    test = ''.join(file_path.split('.')[:-1])
    save_dict(index, test + '.json')
    
def calc_vec_length(index: typing.Dict[str, int]) -> int:
    sum = 0
    for val in index.values():
        sum += val * val
        
    return sqrt(sum)


if __name__ == '__main__':
    sys.exit(main())