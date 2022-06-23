from math import sqrt
from typing import Tuple
from util import calc_vec_length, cleanup_text, get_pdf_content_files, is_valid_json_file, load_dict

def search(pQuery: str):
    pdf_files = get_pdf_content_files()
    
    highest_dot_product: Tuple[str, float] = ('', 0)
    for file in pdf_files:
        dot_prod = calculate_dot_product(file, pQuery)
        print(str(dot_prod) + ' for file ' + file)
        if dot_prod > highest_dot_product[1]:
            highest_dot_product = (file, dot_prod)
            
    print('most similar Document is ' + str(highest_dot_product[1]) + ' with a dot product of ' + highest_dot_product[0])
    
    
def calculate_dot_product(pFilePath: str, pQuery: str) -> float:
    
    # load index of file
    FilePathParts = pFilePath.split('.')
    FilePathParts[-1] = 'json'
    JSONFilePath = '.'.join(FilePathParts)
    
    if not is_valid_json_file(JSONFilePath):
        return -1.0
    
    file_index = load_dict(JSONFilePath)
    
    # index the search query
    query_index = {}
    clean_query = cleanup_text(pQuery)
    
    for word in clean_query.split(' '):
        if word in query_index:
            query_index[word] += 1
        else:
            query_index[word] = 1
            
    vec_len = calc_vec_length(query_index)

    query_index['vec_len'] = vec_len
    
    # calculate doc product between the two indices
    sum = 0
    
    keys = list(query_index.keys()) + list(file_index.keys())
    # the keys act as our dimensions
    for key in keys:
        
        # length of the vector should not be compared directly
        if key == 'vec_len':
            continue
        
        # if the key is not in both dicts the result would be 0 anyway so we can just skip it
        if (key in query_index) and (key in file_index):
            sum += query_index[key] * file_index[key]
            
    dot_prod = sqrt(sum)
    
    # calculate similarty (angle between the vectors)
    similarity = dot_prod / (query_index['vec_len'] * file_index['vec_len'])
    
    return similarity