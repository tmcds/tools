import os
import csv
import hashlib

def add_file_to_baseline(base_line_files_path, target_file_path):
    try:
        if not os.path.exists(base_line_files_path):
            raise FileNotFoundError(f"{base_line_files_path} not found")
        if not os.path.exists(target_file_path):
            raise FileNotFoundError(f"{target_file_path} not found")
        if not base_line_files_path.endswith(".csv"):
            raise ValueError(f"{base_line_files_path} should be a .csv file")
        
        with open(base_line_files_path, 'r') as file:
            current_baseline = list(csv.reader(file))
        
        base_line_files = [file[0] for file in current_baseline]
        
        if target_file_path in base_line_files:
            print(f"{target_file_path} File path detected already")
            while True:
                overwrite = input("Path already exists, Would you like to overwrite [y/n]? ").lower()
                if overwrite in ['y', 'yes']:
                    print("File path will be overwritten")
                    current_baseline = [file for file in current_baseline if file[0] != target_file_path]
                    with open(base_line_files_path, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(current_baseline)
                    
                    with open(target_file_path, 'rb') as file:
                        hash_value = hashlib.sha256(file.read()).hexdigest()
                    
                    with open(base_line_files_path, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([target_file_path, hash_value])
                    print("Entry successfully added into baseline")
                    break
                elif overwrite in ['n', 'no']:
                    print("File path will not be overwritten")
                    break
                else:
                    print("Invalid Entry, Try again")
        else:
            with open(target_file_path, 'rb') as file:
                hash_value = hashlib.sha256(file.read()).hexdigest()
            
            with open(base_line_files_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([target_file_path, hash_value])
            print(f"{target_file_path} successfully added into baseline")
            
        with open(base_line_files_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(current_baseline)
    except Exception as e:
        print("Error:", str(e))

def verify_baseline(base_line_files_path):
    try:
        if not os.path.exists(base_line_files_path):
            raise FileNotFoundError(f"{base_line_files_path} not found")
        if not base_line_files_path.endswith(".csv"):
            raise ValueError(f"{base_line_files_path} should be a .csv file")
        
        with open(base_line_files_path, 'r') as file:
            baseline_files = list(csv.reader(file))
        
        for file in baseline_files:
            file_path = file[0]
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    current_hash = hashlib.sha256(f.read()).hexdigest()
                if current_hash == file[1]:
                    print(f"{file_path} has not changed")
                else:
                    print(f"{file_path} hash is different, Something has changed")
            else:
                print(f"{file_path} is not found")
    except Exception as e:
        print("Error:", str(e))

def create_baseline(base_line_files_path):
    try:
        if os.path.exists(base_line_files_path):
            raise FileExistsError(f"{base_line_files_path} already exists with this name")
        if not base_line_files_path.endswith(".csv"):
            raise ValueError(f"{base_line_files_path} should be a .csv file")
        
        with open(base_line_files_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["path", "hash"])
        print("Baseline created successfully")
    except Exception as e:
        print("Error:", str(e))

print("Watcher Version 1.00")
base_line_files_path = ""
while True:
    print("Please Select one of the following options or enter q or quit to exit")
    print(f"1. Set baseline file; Current set baseline {base_line_files_path}")
    print("2. Add a file to the baseline")
    print("3. Check file against the baseline")
    print("4. Create a new baseline with emails")
    print("5. Create a new baseline")

    entry = input("Please enter a selection: ")

    if entry == "1":
        base_line_files_path = input("Enter the baseline file path: ")
        if os.path.exists(base_line_files_path):
            if not base_line_files_path.endswith(".csv"):
                base_line_files_path = ""
                print("Invalid file. Support only .csv files")
        else:
            base_line_files_path = ""
            print("Invalid baseline file path")
    elif entry == "2":
        target_file_path = input("Enter the path of file you want to monitor: ")
        if os.path.exists(target_file_path):
            add_file_to_baseline(base_line_files_path, target_file_path)
        else:
            print("Invalid target file path")
    elif entry == "3":
        verify_baseline(base_line_files_path)
    elif entry == "4":
        print("Coming Soon ...")
    elif entry == "5":
        new_baseline_file_path = input("Enter path for a new baseline file: ")
        create_baseline(new_baseline_file_path)
    elif entry.lower() in ['q', 'quit']:
        break
    else:
        print("Invalid Entry")
