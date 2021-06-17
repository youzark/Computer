import os.path
file_name_list = ['aim','count','date_report']

def convert_to_path(file_name_list):
    path_list = []
    for file_name in file_name_list:
        path = '../prompt/' + file_name + '.txt'
        path_list.append(path)
    return path_list

def main():
    path_list = convert_to_path(file_name_list)
    file_content_list = []
    for path in path_list:
        if os.path.isfile(path):
            file_instance = open(path,'r')
            file_content = file_instance.readlines()
            file_content_list.append(file_content)
            file_instance.close()

    promt_file = open("../prompt/prompt.txt","w")
    for file_content in file_content_list:
        promt_file.writelines(file_content)

    promt_file.flush()
    promt_file.close()

if __name__ == '__main__':
    main()
