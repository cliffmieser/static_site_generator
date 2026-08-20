from markdown_to_blocks import markdown_to_blocks
from block_types import block_to_block_type
from htmlnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from inline_markdown import text_to_textnodes
import textwrap

def print_textNode(textnode: TextNode): 
    print(f"Text: {textnode.text}\nType: {textnode.text_type}")


def markdown_to_html_node(markdown: str):
    """ Converts an entire document into a single HTMLNode"""
    blocks = markdown_to_blocks(markdown) # splits inline into blocks (based on double newline '\n\n')
    block_nodes = []# should hold list of htmlnodes

    for block in blocks:
        block_type = block_to_block_type(block) # gets the inline-block "type" ie. code, italic, ect

        if block_type == "code":
            lines = block.split("\n")
            inner_lines = lines[1:-1]  # drop the opening/closing ``` fence lines
            code_content = textwrap.dedent("\n".join(inner_lines)) + "\n"
            code_text_node = TextNode(code_content, TextType.TEXT)
            code_child = text_node_to_html_node(code_text_node)
            block_nodes.append(ParentNode("pre", [ParentNode("code", [code_child])]))
            continue

        cleaned = remove_newlines(block) # remove newlines and whitespace 
        text_nodes = text_to_textnodes(cleaned) # get list of text nodes for the current block 
        children = convert_textnodes(text_nodes) # returns any child textnodes for the block


        # based on code block create HTMLNode with proper data 
        match block_type:
            case "paragraph":
                block_nodes.append(ParentNode("p", children))
            case "heading":
                level = len(block) - len(block.lstrip("#")) # holes the number of hashtags 

                cleaned_hash = block[level:].strip() 
                hash_nodes = text_to_textnodes(cleaned_hash)
                hash_children = convert_textnodes(hash_nodes)


                
                block_nodes.append(ParentNode(f"h{level}", hash_children))

            case "quote":
                quote_lst = block.split("\n") # split up the quotes on newlines

                # clean up each quote line
                for i in range(0, len(quote_lst)):
                    if quote_lst[i].startswith("> "):
                        quote_lst[i] = quote_lst[i][1:].strip()
                    elif quote_lst[i].startswith(">"):
                        quote_lst[i] = quote_lst[i][1:]
            
                # join quotes into single line and convert to textnodes
                joined_quotes = " ".join(quote_lst)
                quotes_textnodes = text_to_textnodes(joined_quotes) # converts to textnodes
                quotes_children = convert_textnodes(quotes_textnodes)

                block_nodes.append(ParentNode("blockquote", quotes_children))
            case "unordered_list":
                items = [ParentNode("li", convert_textnodes(text_to_textnodes(line[2:]))) for line in block.split("\n")]
                block_nodes.append(ParentNode("ul", items))
            case "ordered_list":
                items = [ParentNode("li", convert_textnodes(text_to_textnodes(line[3:]))) for line in block.split("\n")]
                block_nodes.append(ParentNode("ol", items))

    return ParentNode("div", block_nodes)

def remove_newlines(markdown: str):
    "Takes a markdown string and remove the new lines and spaces"
    string = markdown.split("\n")
    cleaned_string = []
    for s in string: 
        cleaned_string.append(s.strip())
    return " ".join(cleaned_string)
 
def convert_textnodes(textnodes: list): 
    # helper function that takes list of text nodes and converts them to htmlnode based on text type 
    htmlnodes = []
    for node in textnodes:
        htmlnode = text_node_to_html_node(node)
        htmlnodes.append(htmlnode)

    return htmlnodes



