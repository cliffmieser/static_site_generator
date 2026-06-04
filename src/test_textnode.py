import unittest 
from textnode import TextNode, TextType 

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test if two nodes are equal 
        node = TextNode("This is a text node", TextType.BOLD) 
        node2 = TextNode("This is a text node", TextType.BOLD) 
        self.assertEqual(node,node2) 


    def test_in(self):
        # Test if test_type exists
        node  = TextNode("This is a text node", TextType.TEXT)
        TextTypeNames = [member for member,name in TextType.__members__.items()]
        self.assertIn(node.text_type.name, TextTypeNames, f"{node.text_type} is valid!")

    def test_not_eq(self):
        # Test if a certain type is not in TextType 
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_url_is_none(self):
        # Test if url is set to the default `None` 
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertIsNone(node.url)
if __name__ == "__main__":
    unittest.main()