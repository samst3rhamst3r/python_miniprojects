import pathlib, os

path = input("Welcome! Please input a path, or leave empty to denote the current working directory: ")

while True:
    try:
        if len(path) == 0:
            path = pathlib.Path(".")
        else:
            path = pathlib.Path(path)
        break
    except:
        print("Sorry. That path wasn't valid. Try again.")

jpg_file_paths = []
max_depth = 2
for root, dirs, files in os.walk(path):

    max_depth -= 1
    if max_depth < 0:
        continue
    
    for file in files:
        if file.endswith(".jpg"):
            jpg_file_paths.append(pathlib.Path(root).absolute() / file)
    
    max_depth += 1

for file in jpg_file_paths: print(file)