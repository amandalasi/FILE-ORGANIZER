import shutil
from pathlib import Path

directory_to_organize = Path(r'C:\Users\Alicia\PycharmProjects\mix')

file_type_mapping = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Archives': ['.zip', '.tar', '.rar', '.gz', '.7z'],
    'Code': ['.py', '.java', '.c', '.cpp', '.js', '.html', '.css'],
    'Others': []
}


def create_folders(directory, file_types):
    for folder_name in file_types.keys():
        folder_path = directory / folder_name
        if not folder_path.exists():
            folder_path.mkdir()
            print(f'Created folder: {folder_path}')

def organize_files(directory, file_types):
    for file in directory.iterdir():
        if file.is_file():
            moved = False
            for folder_name, extensions in file_types.items():
                if file.suffix in extensions:
                    destination_folder = directory / folder_name
                    shutil.move(str(file), str(destination_folder / file.name))
                    print(f'Moved {file.name} to {destination_folder}')
                    moved = True
                    break
            if not moved:
                destination_folder = directory / 'Others'
                shutil.move(str(file), str(destination_folder / file.name))
                print(f'Moved {file.name} to {destination_folder}')


def main():
    create_folders(directory_to_organize, file_type_mapping)
    organize_files(directory_to_organize, file_type_mapping)
    print('File organization complete!')

if __name__ == '__main__':
    main()
