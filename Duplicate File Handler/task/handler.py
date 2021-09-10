import os
import sys
import hashlib


def get_hash(file):
    with open(file, "rb") as binary_file:
        hash = hashlib.md5()
        while True:
            chunk = binary_file.read(4096)
            if not chunk:
                break
            hash.update(chunk)
        return hash.hexdigest()


def get_file_format():
    print("Enter file format:")
    return input()


def get_file_numbers():
    print("Enter file numbers to delete:")
    result = input()
    return result.split(" ")

def get_yes_or_no(question):
    while True:
        print(question)
        answer = input().lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        print("Wrong option")

def check_file_delete(duplicates_to_del):
    files_to_del = get_file_numbers()
    for number in files_to_del:
        try:
            if int(number) < 1:
                print("Wrong format {0} {1}".format(files_to_del, duplicates_to_del))
                return None
        except ValueError:
            print("Wrong format {0} {1}".format(files_to_del, duplicates_to_del))
            return None
    return files_to_del

def get_sorting():
    print("Size sorting options:")
    print("1. Descending")
    print("2. Ascending")
    while True:
        print("Enter a sorting option:")
        sorting = input()
        if sorting == "1":
            return True
        elif sorting == "2":
            return False
        else:
            print("Wrong option\n")


duplicates = {}
debug = []

if len(sys.argv) < 2:
    print("Directory is not specified")
else:
    file_format = get_file_format()
    sorting = get_sorting()
    #print(file_format)
    root_dir = sys.argv[1]
    os.chdir(root_dir)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            size = os.path.getsize(os.path.join(root, name))
            filename_parts = os.path.splitext(os.path.join(root, name))
            debug.append([name, size, filename_parts[-1]])
            if file_format == "" or filename_parts[-1] == file_format or filename_parts[-1] == ".{0}".format(file_format):
                if size in duplicates:
                    duplicates[size].append(os.path.join(root, name))
                else:
                    duplicates[size] = [os.path.join(root, name)]

    got_duplicates = False
    for size, files in sorted(duplicates.items(), reverse=sorting):
        if len(files) > 1:
            got_duplicates = True
            print("{} bytes".format(str(size)))
            for file in files:
                print(file)
            print()

    #if not got_duplicates:
    #    sys.exit(0)

    show_duplicates = get_yes_or_no("Check for duplicates?")
    duplicates_to_del = {}
    if show_duplicates:
        next_number = 1
        for size, files in sorted(duplicates.items(), reverse=sorting):
            if len(files) > 1:
                hash_dict = {}
                print()
                print("{} bytes".format(str(size)))
                for file in files:
                    hash = get_hash(file)
                    if hash in hash_dict:
                        hash_dict[hash].append(file)
                    else:
                        hash_dict[hash] = [file]
                for hash, files in hash_dict.items():
                    if len(files) > 1:
                        print("Hash: {0}".format(hash))
                        for file in files:
                            #if file.startswith("module/root_folder"):
                            #    file = file[18:]
                            #if file.startswith("."):
                            #    file = file[1:]
                            print("{0}. {1}".format(next_number, file))
                            duplicates_to_del[str(next_number)] = [file, size]
                            next_number += 1

        delete_files = get_yes_or_no("Delete files?")
        if len(duplicates_to_del) == 0:
            print(duplicates)
            print(debug)
        if delete_files:
            print(duplicates_to_del)
            files_to_delete = None
            while not files_to_delete:
                files_to_delete = check_file_delete(duplicates_to_del)
            freed_space = 0
            for file_number in files_to_delete:
                if file_number in duplicates_to_del:
                    os.remove(duplicates_to_del[file_number][0])
                    freed_space += duplicates_to_del[file_number][1]

            print("Total freed up space: {0} bytes".format(freed_space))



