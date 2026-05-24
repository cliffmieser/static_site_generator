from enum import Enum 

class TextType(Enum):
	PLAIN = "plain text"
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

def main():
	textNode = TextNode("Anchor text", "[LINK]", "https://www.google.com") 

	print(textNode)

if __name__ == "__main__":
	main()