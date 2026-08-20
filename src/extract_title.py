# Helper module for extracting the title from markdown
def extract_title(markdown: str):
    """Splits a markdown file into lines (defined by newline) and extracts the title from a tag"""
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "): # a check to ensure the requried line has the hash, as it may not be the very first line
            title = line 
            return title[1:].strip() 
        else:
            continue 
    raise Exception("No title present.")
    


