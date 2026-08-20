from get_copies import get_copies 
# from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive


def main():
    # run get_copies function
    get_copies() 

    # generate the page 
    generate_pages_recursive("./content", "template.html", "public") 



if __name__ == "__main__":
    main()