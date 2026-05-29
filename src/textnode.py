from enum import Enum 
from htmlnode import LeafNode

class TextType(Enum):
	TEXT = "plain text"
	BOLD = "bold text" 
	ITALIC = "italic text"
	CODE = "code text"
	LINK = "link text" 
	IMAGE = "image url"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text 
		self.text_type = text_type 
		self.url = url 

		

	def __eq__(self, other):
		return True if (self.text == other.text) and (self.text_type == other.text_type ) and (self.url == other.url) else False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
	if text_node.text_type not in TextType: 
		raise ValueError(f"Text Type: ({text_node.text_type}) is not a valid type.")
	elif text_node.text_type == TextType.TEXT: 
		pass 
	elif text_node.text_type == TextType.BOLD:
		pass 
	elif text_node.text_type == TextType.ITALIC:
		pass 
	elif text_node.text_type == TextType.CODE:
		pass 
	elif text_node.text_type == TextType.LINK:
		pass 
	elif text_node.text_type == TextType.IMAGE:
		pass  

def main():
	textNode = TextNode("Anchor text", "[LINK]", "https://www.google.com") 

	print(textNode)

if __name__ == "__main__":
	main()