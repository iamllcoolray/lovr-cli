import os
from util import file_util

class New:
    
    def __init__(self, project_name):
        self.project_name = project_name
    
    def new_project(self):
        # Create a folder (directory)
        if not os.path.exists(self.project_name):  # Check if folder already exists
            os.makedirs(self.project_name)
            print(f"'{self.project_name}' directory has been created.")
            
            self.create_sub_directories()
            self.create_sub_files()
        else:
            print(f"'{self.project_name}' directory already exists.")

    def create_sub_directories(self):
        directory_names = ['assets', 'build', 'lib', 'src']
        assets_sub_directory_names = ['audio', 'maps', 'sprites']
        
        for directory_name in directory_names:
            project_directory_path = os.path.join(self.project_name, directory_name)
            os.makedirs(project_directory_path)
            print(f"'{project_directory_path}' directory has been created.")
            
            if directory_name == directory_names[0]:
                for assets_sub_directory_name in assets_sub_directory_names:
                    project_sub_directory_path = os.path.join(project_directory_path, assets_sub_directory_name)
                    os.makedirs(project_sub_directory_path)
                    print(f"'{project_sub_directory_path}' directory has been created.")    
    
    def create_sub_files(self):
        source_files = ['main.txt', 'config.txt']
        destination_files = ['main.lua', 'config.lua']
        
        for source_file, destination_file in zip(source_files, destination_files):
            # Create a file inside the folder
            source_file_content = file_util.content(source_file)
            file_name = os.path.join(self.project_name, destination_file)
            with open(file_name, 'w') as dest:
                dest.write(source_file_content)
                print(f"'{file_name}' file has been created and content written.")