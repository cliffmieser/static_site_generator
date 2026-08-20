import os 
import shutil


# recursive function to copy contents from source -> destination directory
# ie. static -> public
def get_copies_recursive(source_dir: str, dest_dir: str): 
    source_lst = os.listdir(source_dir)

    while len(source_lst) > 0:
        for x in source_lst:
            if os.path.isfile(y := os.path.join(source_dir, x)):
                shutil.copy(y, dest_dir)
                # delete the item from the source list
                source_lst.remove(x)


            elif os.path.isdir(y := os.path.join(source_dir, x)):
                # create the directory in the destination 
                new_dir = os.path.join(dest_dir, x)
                os.mkdir(new_dir) # the new directory
                # call the function again on the source and the NEW directory
                source_lst.remove(x)
                get_copies_recursive(y, new_dir)
    

def get_copies():
    dir_path_static = "./static"
    dir_path_public = "./public"
    if os.path.exists(dir_path_public): # check if public directory already exists
        # deletion step
        shutil.rmtree(dir_path_public)
        os.mkdir(dir_path_public) 

    get_copies_recursive(dir_path_static, dir_path_public)
    

