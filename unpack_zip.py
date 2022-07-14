import os, zipfile

dir_name = "source/"
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name):
    if item.endswith(extension) or item.endswith(".gz"): 
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall(dir_name)
        zip_ref.close() # close file