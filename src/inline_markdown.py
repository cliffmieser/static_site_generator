from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    lst = [] 
    for _ in old_nodes:
        if _.text_type != TextType.TEXT or delimiter == "": # add to list 
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
        if node.text_type != TextType.TEXT:
            lst.append(node)
            continue
        parts = pattern.split(node.text) # split raw text and image pattern if found 
        i = 0 

        while i < len(parts): # using i to determine if index is raw text or image block
            if parts[i] == "":
                i += 1
                continue #empty string 

            # Check if index of current item is a text segment [Text, alt, url, Text, alt, url, ...]
            elif i % 3 == 0: 
                lst.append(TextNode(parts[i], TextType.TEXT))
                i += 1 
            elif i % 3 == 1: # we've hit the alt text segment 
                alt = parts[i] 
                url = parts[i + 1] 
                lst.append(TextNode(alt, TextType.IMAGE, url))
                i += 2 # to skip the captured alt/url segment  
            else: 
                i += 1 # ensures don't get stuck on a url segment 
    return lst

def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    lst = [] # for storing textnodes
    pattern = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)") # pattern for links
    # loop through old nodes 
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            lst.append(node)
            continue
        parts = pattern.split(node.text) # split raw text and image pattern if found 
        i = 0
        while i < len(parts): 
            if parts[i] == "": # skip spaces
                i+=1
                continue 
            elif i % 3 == 0: # text segment 
                lst.append(TextNode(parts[i], TextType.TEXT))
                i+=1 
            elif i % 3 == 1: # alt text and link segment 
                alt = parts[i] 
                url = parts[i + 1]
                lst.append(TextNode(alt, TextType.LINK, url))
                i += 2 
            else: 
                i += 1
    return lst


def text_to_textnodes(text):
	nodes = [TextNode(text, TextType.TEXT)] 
	nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
	nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
	nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
	nodes = split_nodes_images(nodes)
	nodes = split_nodes_links(nodes) 


	return nodes


def main():
	txt = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
	#text_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
	#extract_markdown_links(text_link)
	print(text_to_textnodes(txt))

if __name__ == "__main__":
	main()