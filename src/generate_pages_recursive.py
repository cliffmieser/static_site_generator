import os 
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node
import shutil
from pathlib import Path 
from generate_page import generate_page
#crawling "content" directory and writting to "public"

def generate_pages_recursive(src_dir_path, template_path, dest_dir_path, basepath): 
  """
       Crawls every entry in content directory
       For each markdown file:
        - generate new .html file using the same template.html
          (Generated pages are written to public dir in same structure)
    """
  dir_list = os.listdir(src_dir_path) # list of directory contents

  # Directory Branch
  for i in range(0, len(dir_list)): # for every item in the list (directories and files)
    current_path = os.path.join(src_dir_path, dir_list[i])
    dest_path =  os.path.join(dest_dir_path, dir_list[i])

    if  os.path.isdir(current_path):
      if os.path.exists(dest_path):
        #directory exists in dest
        # call function again to check for .md files 
        generate_pages_recursive(current_path, template_path, dest_path, basepath)
      else:
        # Path does not exists, create it and recurse into it 
        os.mkdir(dest_path)
        generate_pages_recursive(current_path, template_path, dest_path, basepath)
    # Markdown file branch
    elif is_md := dir_list[i].endswith(".md"): # check if a regular file 
      # seperate the filename stem and extension
      # append html to filename
      file, ext = os.path.splitext(dir_list[i])
      file += ".html" 
      dst_path = os.path.join(dest_dir_path, file)

      generate_page(current_path, template_path, dst_path, basepath)

      # pass to generate_page function

      # try: 
      #   with open(current_path, "r") as f:
      #     markdown_data = f.read() # markdown file
      #     print(f"Read markdown file: {dir_list[i]}")  
      # except Exception as e:
      #   print(f"Failed to convert {dir_list[i]}: {e}")

      # with open(template_path) as f:
      #   template_data = f.read() # html template file 
      #   print(f"Read template file: {template_path}")

      # # create html node from markdown, then turn to hmtl string
      # markdown_data_htmlnode = markdown_to_html_node(markdown_data)
      # markdown_html_string = markdown_data_htmlnode.to_html()

      # # extract title
      # title = extract_title(markdown_data) 
      
      # # replace {Tile} and {Content} placeholders
      # markdown_data_converted = template_data.replace("{{ Title }}", title)
      # # create full page 
      # content_html = markdown_data_converted.replace("{{ Content }}", markdown_html_string)

      # # write to page in destination path
      # with open(dst_path, "w") as f:
      #   if os.path.exists(dest_dir_path):
      #     # path doesn't exists yet, make directory and write 
      #     # print(f"Creating directory, Writing {dir_list[item]} from {src_dir_path} to {dest_dir_path}")
      #     f.write(content_html)
      #   else:
      #     # print(f"Writing {dir_list[item]} from {src_dir_path} to {dest_dir_path}")
      #     f.write(content_html)
    else: # not a markdown file or directory exists, skip
      continue


# generate_pages_recursive("./content", "template.html", "public" )

