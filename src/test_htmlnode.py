import unittest 
from htmlnode import HTMLNode, LeafNode

class test_htmlnode(unittest.TestCase):
    def test_eq(self):
        htmlnode = HTMLNode("<p>", "random text")
        htmlnode2 = HTMLNode("<p>", "random text")

        self.assertEqual(htmlnode.tag, "<p>")

    def test_is_htmlnode(self):
            htmlnode = HTMLNode("<a>", "random link text")

            self.assertIsInstance(htmlnode, HTMLNode)

    def test_is_not_none(self):
         htmlnode = HTMLNode("<href>", "https://google.com")
         self.assertIsNot(htmlnode.value, None)

    def test_leafnode_is_subclass(self):
          self.assertIsSubclass(LeafNode, HTMLNode)

    def test_leaf_to_html_p(self): # test if to_html works
        node = LeafNode("p", "Hello, world!")   
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")    

    def test_leaf_to_html_props(self): # test if to_html works with props
         node = LeafNode("p", "hello there", props={"color": "red"})
         self.assertEqual(node.to_html(), "<p color=red>hello there</p>")
if __name__ == "__main__":
    unittest.main()