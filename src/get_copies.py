import os 
import shutil


# recursive function to copy contents from source -> destination directory
# ie. static -> public
def get_copies_recursive(source_dir: str, dest_dir: str): 
    source_lst = os.listdir(source_dir)


    for x in source_lst:
        if os.path.isfile(y := os.path.join(source_dir, x)):
            shutil.copy(y, dest_dir)
            # delete the item from the source list
            # source_lst.remove(x)
            continue


        elif os.path.isdir(y := os.path.join(source_dir, x)):
            # create the directory in the destination 
            new_dir = os.path.join(dest_dir, x)
            os.mkdir(new_dir) # the new directory
            # call the function again on the source and the NEW directory
            # source_lst.remove(x)
            get_copies_recursive(y, new_dir)
    

def get_copies():
    dir_path_src = "./static"
    dir_path_target = "./docs"
    if os.path.exists(z := dir_path_target): # check if target directory already exists
        # deletion step
        shutil.rmtree(z)

    os.mkdir(dir_path_target) 
    get_copies_recursive(dir_path_src, dir_path_target)
    

