from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    lst = [] 
    for _ in old_nodes:
        if _.text_type != TextType.TEXT:           # add to list 
            lst.extend(_)
        # if matching closing delimiter isn't found, raise exception 
        # get delimiters
        is_match = None 
        txt = _.text.split(delimiter)
        is_match = len(txt) % 2 == 0
        if is_match: # if True, raise error (unmatched delimiter)
            raise BaseException(f"Invalid markdown.\nAfter splitting text: {txt}")
        elif is_match == None:
            raise ValueError(f"is_match cannot be ({is_match}) type")
        else: # if False (odd), contents are wrapped by a (matching) delimiter
            # get the text enclosed in delimiters 
            matched = list(filter(lambda x: x if " " not in x else None, txt))
            print(f"valid: {txt}\n{matched}")
            

def main():
    node = TextNode("This is text with a code `block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE) 

if __name__ == "__main__":
    main()
