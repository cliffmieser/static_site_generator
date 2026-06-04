from enum import Enum 
from htmlnode import LeafNode

class TextType(Enum):
	TEXT = ""
	BOLD = "b" 
	ITALIC = "i"
	CODE = "code"
	LINK = "a" 
	IMAGE = "img"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text 
		self.text_type = text_type # Text type given from class 
		self.url = url 

		

	def __eq__(self, other):
		return True if (self.text == other.text) and (self.text_type == other.text_type ) and (self.url == other.url) else False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode: # Returns HTMLNode
	if text_node.text_type not in TextType: 
		raise ValueError(f"Text Type: ({text_node.text_type}) is not a valid type.")
	elif text_node.text_type == TextType.TEXT: 
		return LeafNode(None, text_node.text)
	elif text_node.text_type == TextType.BOLD:
		return LeafNode("b", text_node.text)
	elif text_node.text_type == TextType.ITALIC:
		return LeafNode("i", text_node.text)
	elif text_node.text_type == TextType.CODE:
		return LeafNode("code", text_node.text)
	elif text_node.text_type == TextType.LINK:
		return LeafNode("a", text_node.text, {"href": None})
	elif text_node.text_type == TextType.IMAGE:
		return LeafNode("img", text_node.text, {"src": text_node.url, "alt": text_node.text})

	

def main():
	pass

if __name__ == "__main__":
	main()