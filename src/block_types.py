from enum import Enum 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code" 
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list" 


def block_to_block_type(markdown: str): 
    lines = markdown.split('\n')

    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING.value
    elif markdown.startswith("```\n") and (markdown.endswith("\n```") or markdown.endswith("```")):
        return BlockType.CODE.value 
    elif markdown.startswith(">"):
        return BlockType.QUOTE.value
    elif lines[0].startswith("- "):
        for line in lines:
            if line.startswith("- "):
                continue 
            else: 
                return False 
        return BlockType.UNORDERED_LIST.value 
    elif lines[0].startswith("1. "):
        for i in range(0, len(lines)):
            if i == 0:
                continue 
            elif (int(lines[i][0]) == int(lines[i - 1][0])) + 1 and (lines[i].startswith(f"{lines[i][0]}. ")):
                continue
            else:
                return False
        return BlockType.ORDERED_LIST.value
    else:  
        return BlockType.PARAGRAPH.value