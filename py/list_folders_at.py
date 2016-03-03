import os

def folders_at(place):
    result = set()
    for folder_path, folder_names, file_names in os.walk(place):
        result.add(str(folder_path)[2:])
    return result

def write(file, folder_list):
    with open(file, "w") as f:
        f.write("\n".join(folder_list))

if __name__ == '__main__':
    folders = folders_at(".")
    for i in folders:
        print(i)
    write("folder_list.txt", folders)
