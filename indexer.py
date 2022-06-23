
from util import CONTENT_PATH, save_dict, cleanup_text, calc_vec_length, get_pdf_content_files
import pdfplumber
from multiprocessing import Pool, cpu_count
import typing

def index():
    pdf_files = get_pdf_content_files()

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