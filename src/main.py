from get_copies import get_copies 
import sys
# from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive


def main():
    # run get_copies function
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/" # first CLI argument if none given


    get_copies() 

    # generate the page 
    generate_pages_recursive("./content", "template.html", "./public", basepath) 



if __name__ == "__main__":
    main()