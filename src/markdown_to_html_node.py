from markdown_to_blocks import markdown_to_blocks
from block_types import block_to_block_type, BlockType 
from htmlnode import HTMLNode, ParentNode, LeafNode

def markdown_to_html_node(markdown: str):
    """ Converts an entire document into a single HTMLNode"""
    blocks = markdown_to_blocks(markdown) # splits inline into blocks (based on double newline '\n\n')
    print(blocks)
    
    for block in blocks:
        block_type = block_to_block_type(block) # gets the inline-block "type" ie. code, italic, ect
        print(block_type) 
        # based on code block create HTMLNode with proper data 
        match (block_type):
            case "paragraph":
                cleaned = remove_p_newlines(block)
                leaf_node = HTMLNode("p", cleaned)
                
            case "heading":
                pass 
            case "code":
                pass 
            case "quote":
                pass 
            case "unordered_list":
                pass 
            case "ordered_list":
                pass 

def remove_p_newlines(markdown: str):
    "Takes a markdown string and remove the new lines"
    string = markdown.split("\n")
    cleaned_string = []
    for s in string: 
        cleaned_string.append(s.strip())
    return " ".join(cleaned_string)



