# def main():
#     myfile = open("textfile.txt", "r")    
#     if myfile.mode == 'r':
#         # contents = myfile.read()
#         # print(contents)
#         fl = myfile.readlines()
#         for x in fl:
#             print(x)

# if __name__ == "__main__":
#     main()

# # operating system shell
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("textfile.txt"):
        # get path to the file
        src = path.realpath("textfile.txt")

        # making backup copy of the file
        dst = src + ".bak"
        shutil.copy(src, dst)

        #rename the original file
        os.rename("textfile.txt", "newfile.txt")

        # put into ZIP
        root_dir, tail =path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        # more stuff on zip
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("newfile.txt")


if __name__ == "__main__":
    main()