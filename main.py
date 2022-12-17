import os


def merging_files(file_list, work_dir):
    file_dict = {}
    for file in file_list:
        with open(os.path.join(work_dir, file), "r", encoding="utf-8") as f:
            result = f.readlines()
            file_dict[file] = (result, len(result))
    sorted_dict = dict(sorted(file_dict.items(), key=lambda item: item[1][1]))
    with open("sorted_dict.txt", "a", encoding="utf-8") as file:
        for key, value in sorted_dict.items():
            file.writelines(f"Файл {key}\nКоличество строк {value[1]}\n")
            file.writelines(value[0])
            file.writelines("\n\n")


if __name__ == "__main__":
    current = os.getcwd()
    folder = "sorted"
    full_path = os.path.join(current, folder)
    all_txt = [files for files in os.listdir(full_path) if files.endswith(".txt")]
    merging_files(all_txt, full_path)
