from textnode import TextNode, TextType, extract_markdown_images, extract_markdown_links
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
    

def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    lst = [] # for storing textnodes
    pattern = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)") # pattern for detecting image format
    # loop through old nodes 
    for node in old_nodes:
        parts = pattern.split(node.text) # split raw text and image pattern if found 
        for part in range(0, len(parts)):
            print(f"Part: {parts[part]}")
            if parts[part] == "":
                continue #empty string 
            elif parts[part] ==  extract_markdown_images(node.text)[0][0] and parts[part + 1] == extract_markdown_images(node.text)[0][1]:
                print("image found") 
                lst.append(TextNode(parts[part], TextType.IMAGE, parts[part + 1]))
                part += 2 
                if part > len(parts):
                    continue
                else:
                    break
            else:
                lst.append(TextNode(parts[part], TextType.TEXT))
    return lst

def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    lst = [] # for storing textnodes
    pattern = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)") # pattern for links
    # loop through old nodes 
    for node in old_nodes:
        parts = pattern.split(node.text) # split raw text and image pattern if found 
        for part in range(0, len(parts)):
            print(f"Part: {parts[part]}")
            if parts[part] == "":
                continue #empty string 
            elif parts[part] ==  extract_markdown_links(node.text)[0][0] and parts[part + 1] == extract_markdown_links(node.text)[0][1]:
                print("image found") 
                lst.append(TextNode(parts[part], TextType.LINK, parts[part + 1]))
                part += 2 
                if part > len(parts):
                    continue
                else:
                    break
            else:
                lst.append(TextNode(parts[part], TextType.TEXT))
    return lst



def main():
    node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
    # node = TextNode("This is text with no image", TextType.TEXT)
    print(f"result: \n\n\t{split_nodes_images([node])}")

if __name__ == "__main__":
    main()
