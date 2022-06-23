import sys

from indexer import index
from searcher import search

def main() -> int:
    # check input args
    print(sys.argv)
    if sys.argv[1] == '-index':
        print("Indexing files in the Content Folder")
        index()
    elif sys.argv[1] == '-search':
        query = sys.argv[2]
        print("Searching for " + query)
        search(query)
    else:
        print("Unknows command entered")

    return 0

if __name__ == '__main__':
    sys.exit(main())