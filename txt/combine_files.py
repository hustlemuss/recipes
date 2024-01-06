import os

def combine_files(input_folder, output_file):
    files = os.listdir(input_folder)
    files.sort(key=lambda f: len(open(os.path.join(input_folder, f), 'r', encoding='utf-8').readlines()))

    with open(output_file, 'w', encoding='utf-8') as result_file:
        for file_name in files:

            if file_name.endswith(".py"):
                continue

            file_path = os.path.join(input_folder, file_name)


            with open(file_path, 'r', encoding='utf-8') as current_file:
                content = current_file.readlines()
                num_lines = len(content)


            if num_lines == 0:
                continue


            result_file.write(f"{file_name}\n{num_lines}\n")


            result_file.writelines(line.rstrip() + '\n' for line in content)


            result_file.write('\n')

if __name__ == "__main__":
    input_folder_path = 'C:/Users/hake1/PycharmProjects/recept/txt'
    output_file_path = 'C:/Users/hake1/PycharmProjects/recept/txt/combineted.txt'

    combine_files(input_folder_path, output_file_path)












