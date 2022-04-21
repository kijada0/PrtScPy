import os
path0 = path = "D:/Documents/PythonProject/PrtScPy/"

def folder_selector(p, list):
    for i in range(len(list)):
        if os.path.isdir(p+list[i]):
            print(i, "\t->\t", list[i])
    j = int(input("\nFolder number: "))
    return list[j]

def folder_in_dir(path):
    list = os.listdir(path)
    f = False
    for i in range(len(list)):
        if os.path.isdir(path+list[i]): f = True
    return f

def flip_text(text):
    old_text = str.split(text[:len(text)], "-")
    new_text = ""
    for j in reversed(range(len(old_text))): new_text = new_text + old_text[j] + "-"
    return(new_text[:-1])

while True:
    path = path0
    print(path)

    while folder_in_dir(path):
        path = path + folder_selector(path, os.listdir(path)) + "/"
        print(path)

    if input("Are you sure? (Y - yes): ") == "Y":
        object_list = os.listdir(path)
        for i in range(len(object_list)):
            file_name = str.split(object_list[i][:len(object_list[i])-4], "_")

            if len(file_name[2]) == 10:
                new_name = file_name[0] + "_" + file_name[2] + "_" + file_name[1] + ".png"
                #print(new_name)
                os.rename(path+object_list[i], path+new_name)
            elif len(file_name[1]) == 10:
                new_name = file_name[0] + "_" + flip_text(file_name[1]) + "_" + file_name[2] + ".png"
                #print(new_name)
                os.rename(path+object_list[i], path+new_name)
        print("Done")

    if not input("Run again? (Y - yes): ") == "Y": exit()