import unittest  
from block_types import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_block_to_blocktype(self):
        md = "## testing with hash"
        result = block_to_block_type(md) 
        self.assertEqual(result, "heading")

    def test_code_block(self):
        md = """```
This is a code block
```"""     
        result = block_to_block_type(md) 
        self.assertEqual(result, "code")

    def test_quote_block(self):
        md = "> This is a quote\n> Here is anothe one" 
        result = block_to_block_type(md) 
        self.assertEqual(result, "quote") 

    def test_unordered_list_block(self):
        md = "- list item 1\n- list item 2\n- list item 3"
        result = block_to_block_type(md) 
        self.assertEqual(result, "unordered_list")

    def test_ordered_list_block(self):
        md = "1. first list item\n2. second list item\n3. third list item"
        result = block_to_block_type(md)
        self.assertEqual(result, "ordered_list")

    def test_paragraph_block(self):
        md = "Here is a regular paragraph"
        result = block_to_block_type(md)
        self.assertEqual(result, "paragraph")


if __name__ == "__main__":
    unittest.main()