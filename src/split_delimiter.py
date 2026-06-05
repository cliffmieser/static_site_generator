from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    lst = [] 
    for _ in old_nodes:
        if _.text_type != TextType.TEXT or delimiter == "":           # add to list 
            lst.append(_)
            continue
        # if matching closing delimiter isn't found, raise exception 
        # get delimiters
        is_match = None 
        txt = _.text.split(delimiter)
        is_match = len(txt) % 2 == 0 # to determine if matching delims exist
        if is_match: # if True, raise error (unmatched delimiter)
            raise BaseException(f"Invalid markdown.\nAfter splitting text: {txt}")
        elif is_match == None:
            raise ValueError(f"is_match cannot be ({is_match}) type")
        else: # if False (odd), contents are wrapped by a (matching) delimiter
            # find the delimiters and create nodes 
            for i in range(len(txt)):
                if txt[i] == "":
                    continue 

                if i % 2 == 0: #even index 
                    lst.append(TextNode(txt[i], TextType.TEXT))
                else: # odd index 
                    lst.append(TextNode(txt[i],  text_type))
             
    return lst 
    

def split_nodes_images():
    pass 

def split_nodes_links():
    pass


def main():
    pass

if __name__ == "__main__":
    main()
