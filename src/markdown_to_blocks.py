
# Takes a full markdown string representing an entire document 
def markdown_to_blocks(markdown: str): 
    blocks = [] 
    md = markdown.split("\n\n")
    for string in md:
        cleaned = string.strip() 
        if cleaned == "":
            continue 
        else: 
            blocks.append(cleaned)
    return blocks 


