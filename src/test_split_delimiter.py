from textnode import TextNode, TextType 
from htmlnode import HTMLNode, LeafNode, ParentNode  
from split_delimiter import split_nodes_delimiter
import unittest


class test_split_delimiter(unittest.TestCase):
    
    def test_plain_text(self):
        node = TextNode("This is plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "", TextType.TEXT)

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE) 
        self.assertTrue(new_nodes)

    def test_bold_delim(self):
        node = TextNode("This is text with a **bold block** word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD) # works for "*" and "**"
        self.assertTrue(new_nodes)
    
    def test_italic(self): 
        node = TextNode("This is _italic_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC) # works for "*" and "**"
        self.assertTrue(new_nodes)

    def test_multiple_delim(self):
        node = TextNode("This _text_ as two _italic_ words", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertTrue(new_nodes)

    def test_is_textnode(self):
        node = TextNode("this is a `code` block", TextType.CODE) 
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        is_text_node = [True for node in new_nodes if isinstance(node, TextNode)]
        is_text_node_check = True if False not in is_text_node else False 
        self.assertTrue(is_text_node_check)

    # ignore links and images for now 
if __name__ == "__main__":
    unittest.main()