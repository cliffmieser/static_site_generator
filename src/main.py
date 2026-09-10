from get_copies import get_copies 
import sys
import os
# from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/" # first CLI argument if none given

    # run get_copies function
    get_copies() 

    # generate the page 
    if os.path.exists("./docs"):
        generate_pages_recursive("./content", "template.html", "./docs", basepath) 
    else:
        os.mkdir("./docs")
        generate_pages_recursive("./content", "template.html", "./docs", basepath) 



if __name__ == "__main__":
    main()