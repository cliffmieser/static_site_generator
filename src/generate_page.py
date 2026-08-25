from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os 

# reference:
# generate_page("./content/index.md", "./template.html", "./public/index.html") 

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read markdown at from_path and store contents to variable 
    with open(from_path) as f:
        from_data = f.read() # the markdown file


    with open(template_path) as f: 
        template_data = f.read() # the html template file


    from_html_node = markdown_to_html_node(from_data) # convert the markdown to html_node
    from_html_string  = from_html_node.to_html() # turns the markdown html node into html

    # extract title
    title = extract_title(from_data) # from_data is the markdown before the conversion 

    from_html_converted= template_data.replace("{{ Title }}", title)
    content_html = from_html_converted.replace("{{ Content }}", from_html_string)  # the full page 

    content_html = content_html.replace('href="/', f'href="{basepath}')
    content_html = content_html.replace('src="/', f'src="{basepath}')

    
    # write to page 
    with open(dest_path, "w") as f:
        if os.path.exists(dest_path) is False:
            # path doesn't exists yet 
            os.makedirs(os.path.dirname(dest_path)) 
            f.write(content_html)
        else:
            f.write(content_html)


