import os
import time

def remove_duplicates_from_file(file_path):
    # Read lines from file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove duplicates
    unique_lines = list(set(lines))
    
    # Write unique lines back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)

    return len(lines) - len(unique_lines)

def remove_duplicates_from_folder(folder_path):
    # Iterate through files in folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if file is a txt file
        if file_path.endswith('.txt'):
            print(f'Removing duplicates from {file_path}')
            duplicates_removed = remove_duplicates_from_file(file_path)
            print(f'{duplicates_removed} duplicate lines removed\n')
        else:
            print(f'{file_path} is not a txt file\n')

if __name__ == '__main__':
    folder_path = r'folder path'
    remove_duplicates_from_folder(folder_path)
