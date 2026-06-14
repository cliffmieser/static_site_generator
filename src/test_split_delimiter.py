from textnode import TextNode, TextType 
from htmlnode import HTMLNode, LeafNode, ParentNode  
from src.inline_markdown import split_nodes_delimiter, split_nodes_images, split_nodes_links
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

    # Test split nodes images/links 
    def test_split_on_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        result = split_nodes_images([node]) 
        self.assertEqual(str(result), "[TextNode(This is text with an , TextType.TEXT, None), TextNode(image, TextType.IMAGE, https://i.imgur.com/zjjcJKZ.png)]")

    def test_split_with_multiple_images(self):
        node = TextNode("This is text with multiple images, first ![image](https://i.imgur.com/zjjcJKZ.png) and second ![image](https://i.imgur.com/bkadNLM.png)", TextType.TEXT)

        result = split_nodes_images([node])
        self.assertEqual(str(result), "[TextNode(This is text with multiple images, first , TextType.TEXT, None), TextNode(image, TextType.IMAGE, https://i.imgur.com/zjjcJKZ.png), TextNode( and second , TextType.TEXT, None), TextNode(image, TextType.IMAGE, https://i.imgur.com/bkadNLM.png)]")


    def test_split_on_links(self):
        node = TextNode("Here is a link to [google](https://www.google.com)", TextType.TEXT)
        result = split_nodes_links([node])
        self.assertEqual(str(result), "[TextNode(Here is a link to , TextType.TEXT, None), TextNode(google, TextType.LINK, https://www.google.com)]")

if __name__ == "__main__":
    unittest.main()