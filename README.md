# File Manager

A simple command-line file manager written in Python. It allows you to view the current working directory, create files and folders, and delete files or folders interactively.

## Features

- Display the current working directory
- List files and folders with their type
- Create empty files
- Create folders
- Delete files or folders recursively
- Interactive menu-based interface

## Requirements

- Python 3.6 or later

The project uses only Python standard-library modules:

- `os`
- `pathlib`
- `shutil`

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/pythoner-145/filemanager.git
cd filemanager
```

### 2. Run the program

```bash
python file_mngr.py
```

On some systems, you may need to use:

```bash
python3 file_mngr.py
```

## Usage

When the program starts, it displays the current working directory and its contents. You can then select one of the available options:

```text
1. Create file
2. Create folder
3. Delete
4. Exit
```

### Create a file

Choose option `1`, then enter the file name. An empty file will be created in the current directory.

### Create a folder

Choose option `2`, then enter the folder name. A new folder will be created in the current directory.

### Delete an item

Choose option `3`, then enter the name of a file or folder. Files are deleted directly, while folders and their contents are removed recursively.

### Exit

Choose option `4` to close the file manager.

## Example

```text
Current directory : /path/to/filemanager
1.file_mngr.py (File)
________________________________________
Options:
 1.Create file
 2.Create folder
 3.Delete
 4.Exit
Select an option :
```

## Important Notes

- All operations are performed in the directory where the program is started.
- Deleting a folder also deletes everything inside it.
- Make sure you enter the correct file or folder name before deleting it.
- The program does not currently support changing directories.

## Project Structure

```text
filemanager/
├── file_mngr.py
└── README.md
```

## License

No license has been specified for this project yet.
