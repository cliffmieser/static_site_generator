from get_copies import get_copies 
import sys
# from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive


def main():
    # run get_copies function
    basepath = "/" if not sys.argv[1] else sys.argv[1] # first CLI arguments 

    get_copies() 

    # generate the page 
    generate_pages_recursive("./content", "template.html", "public") 



if __name__ == "__main__":
    main()