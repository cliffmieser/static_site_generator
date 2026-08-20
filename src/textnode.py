from enum import Enum 
from htmlnode import LeafNode
import re


# set of symbolic names (members) bound to unqique values 
# helps determine the type of html block is passed
class TextType(Enum):
	TEXT = "text"
	BOLD = "bold" 
	ITALIC = "italic"
	CODE = "code"
	LINK = "link" 
	IMAGE = "image"

def extract_markdown_images(text):
	""" Takes raw text and returns a list of tuples with each item having 
		1. the alt text 
		2. the url (of the image)
	"""
	lst = []
	
	# compile regexp 
	pattern = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)")
	pattern_obj = pattern.findall(text) # returns list of tuples
	lst.extend(pattern_obj)
	return lst

	

def extract_markdown_links(text):
	""" Takes raw text and returns a list of tuples with each item having 
		1. the anchor text 
		2. the url (hyperlink)
	"""
	lst = [] 

	# compile regexp
	pattern = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")
	pattern_obj = pattern.findall(text)  # returns list of tuples 
	lst.extend(pattern_obj)
	return lst 


""" Textnodes: represents inline text"""
class TextNode: # A pythonic representation of text that can be converted into HTMLndoes
	def __init__(self, text, text_type, url=None):
		self.text = text 
		self.text_type = text_type # Text type given from class 
		self.url = url 

		

	def __eq__(self, other):
		return True if (self.text == other.text) and (self.text_type == other.text_type ) and (self.url == other.url) else False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode: # Returns HTMLNode (LeafNode)
	if not isinstance(text_node.text_type, TextType):
		raise ValueError(f"Text Type: ({text_node.text_type}) is not a valid type.")
	elif text_node.text_type == TextType.TEXT: # just text without any tag vale
		return LeafNode(None, text_node.text)
	elif text_node.text_type == TextType.BOLD:
		return LeafNode("b", text_node.text)
	elif text_node.text_type == TextType.ITALIC:
		return LeafNode("i", text_node.text)
	elif text_node.text_type == TextType.CODE:
		return LeafNode("code", text_node.text)
	elif text_node.text_type == TextType.LINK:
		return LeafNode("a", text_node.text, {"href": text_node.url})
	elif text_node.text_type == TextType.IMAGE:
		return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

	


