#!/usr/bin/env python
import pathlib
from pathlib import Path

file_path = Path(__file__)
absolute_path = file_path.absolute()
parent_dir = absolute_path.parent
dir_relative_to = absolute_path.relative_to(parent_dir)
 
print("#"*100)
print()
print(file_path)
print(absolute_path)
print(parent_dir)
print(dir_relative_to)

# existance
print("#"*100)
print()
print(absolute_path.exists())
print(absolute_path.is_dir())
print(absolute_path.is_file())
print(dir_relative_to.exists())

# modifiable file or not
print("#"*100)
print()
pure_path = pathlib.PurePath(__file__)
operatable_path = pathlib.Path(__file__)

# task path apart
print("#"*100)
print()
print(pure_path.parts)
print(pure_path.parts[-1])

# get parents
print("#"*100)
print()
print(pure_path.parent)
print(pure_path.parents[1])
print(pure_path.parents[2])

# join path
print("#"*100)
print()
data_folder = pathlib.Path(__file__).parents[0].joinpath("data")
print(data_folder)


# create file and directory
print("#"*100)
print()
if not data_folder.exists():
    data_folder.mkdir()

new_file_name = data_folder.joinpath("test_file.txt")
new_file_name.touch(exist_ok=True)


# iterating through a folder
print("#"*100)
print()
print("Iterating folder:")
for file_obj in parent_dir.iterdir():
    print("*"*100)
    print(file_obj)
    print("if directory?" + str(file_obj.is_dir())) 
    print("if file?" + str(file_obj.is_file())) 
    print("File name:" + str(file_obj.name)) 
    print("File suffix:" + str(file_obj.suffix)) 


# grab the current working directory
print("#"*100)
print()
print(str(pathlib.Path.cwd()))
print(str(pathlib.Path.home()))


# resolve
print("#"*100)
print()
print(pathlib.Path("hyx/../path.py").resolve())



