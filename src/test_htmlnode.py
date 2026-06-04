import unittest
from split_delimiter import split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class test_htmlnode(unittest.TestCase):
    def test_eq(self):
        htmlnode = HTMLNode("<p>", "random text")
        htmlnode2 = HTMLNode("<p>", "random text")

        self.assertEqual(htmlnode.tag, "<p>")

    def test_is_htmlnode(self):
            htmlnode = HTMLNode("<a>", "random link text")

            self.assertIsInstance(htmlnode, HTMLNode)

    # def test_is_not_none(self):
    #      htmlnode = HTMLNode("<href>", "https://google.com")
    #      self.assertIsNot(htmlnode.value, None)

    #Leaf Nodes
    def test_leafnode_is_subclass(self):
          self.assertIsSubclass(LeafNode, HTMLNode)

    def test_leaf_to_html_p(self): # test if to_html works
        node = LeafNode("p", "Hello, world!")   
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")    

    def test_leaf_to_html_props(self): # test if to_html works with props
         node = LeafNode("p", "hello there", props={"color": "red"})
         self.assertEqual(node.to_html(), "<p color=red>hello there</p>")

    
    #Parent nodes 
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_to_html_with_parentNodes(self):
         child_node = LeafNode("span", "span leaf node")
         parentnode1 = ParentNode("p", [child_node])
         parentnode2 = ParentNode("div", [parentnode1])
         self.assertEqual( 
              parentnode2.to_html(), 
              "<div><p><span>span leaf node</span></p></div>"
         )

    def test_is_sub_class_htmlnode(self):
        subclasses = [ParentNode, LeafNode]
        for _cls in subclasses:
             self.assertIsSubclass(_cls, HTMLNode)
        
    def test_multiple_children(self):
         _leafnode1 = LeafNode("span", "span leaf node")
         _leafnode2 = LeafNode("b", "bold leaf node")
         parentNode = ParentNode("div", [_leafnode1, _leafnode2])
         self.assertEqual(parentNode.to_html(), 
                          "<div><span>span leaf node</span><b>bold leaf node</b></div>") 
         
    # Testing ENUM values 
    def test_text(self):
         node = TextNode("Text node", TextType.TEXT)
         html_node = text_node_to_html_node(node)
         self.assertEqual(html_node.tag, None)
         self.assertEqual(html_node.value, "Text node")

    def test_image_tag(self):
        node = TextNode("img", TextType.IMAGE, "https://google.com" )
        html_node = text_node_to_html_node(node)

        # print(isinstance(html_node, LeafNode)) 
        self.assertEqual(html_node.props["src"], "https://google.com")
if __name__ == "__main__":
    unittest.main()