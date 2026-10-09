import os
from pathlib import Path
import shutil

class FileManager:
    def __init__(self) :
        self.current_path = Path.cwd()

    def show_current_directory(self):
      print(f'Current directory : {self.current_path}')
      items = list(self.current_path.iterdir())
      for index , item in enumerate(items,1):
        item_type = 'Folder' if item.is_dir() else "File"
        print(f'{index}.{item.name} ({item_type})')
        print('_'*40)

    def create_file(self,filename):
      file_path = self.current_path / filename
      try:
        file_path.touch()
        print(f"Success: File {filename} created")
      except Exception as e:
        print(f"Error  creating file: {e}")


    def create_folder(self,foldername):
      folder_path = self.current_path /foldername
      try :
        folder_path.mkdir(exist_ok = True)
        print(f"Success : Folder {foldername} created")
      except Exception as e:
        print(f"Error Creating folder : {e}")

    def delete_item(self,name):
      target_path = self.current_path / name
      if not target_path.exists():
        print(f'Error:{name} dosent exist')
        return
      try:
        if target_path.is_dir():
          shutil.rmtree(target_path)
          print(f'Success:Folder {name} deleted')
        else:
          target_path.unlink()
          print(f'Success: File {name} deleted')
      except Exception as e:
         print(f"Error deleting item:{e}")



if __name__ == "__main__":
  manager = FileManager()

  while True:
    manager.show_current_directory()
    print('Options:')
    print(" 1.Create file")
    print(" 2.Create folder")
    print(" 3.Delete")
    print(" 4.Exit")

    choice = input('Select an option : ').strip()

    if choice == '1':
      fname = input('Enter File name : ')
      manager.create_file(fname)

    elif choice == '2':
      dname = input('Enter folder name : ')
      manager.create_folder(dname)

    elif choice == '3':
      dname = input('Enter folder or file name to delete : ')
      manager.delete_item(dname)

    elif choice == '4':
      print('Existing File manager ')
      break
    else :
      print('Invalid option ')