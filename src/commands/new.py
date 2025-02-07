import os
from util import file_util

class New:
    
    def __init__(self, project_name):
        self.project_name = project_name
    
    # Called to create the new project
    def new_project(self):
        # Create the project directory or notify that the directory already exists
        if not os.path.exists(self.project_name):  # Check if folder already exists
            os.makedirs(self.project_name)
            print(f"'{self.project_name}' directory has been created.")
            
            self._create_sub_directories()
            self._create_sub_files()
        else:
            print(f"'{self.project_name}' directory already exists.")

    # Creates the sub directories located within the project directory
    def _create_sub_directories(self):
        directory_names = ['assets', 'build', 'lib', 'src']
        assets_sub_directory_names = ['audio', 'maps', 'sprites']
        
        for directory_name in directory_names:
            project_directory_path = os.path.join(self.project_name, directory_name)
            os.makedirs(project_directory_path)
            print(f"'{project_directory_path}' directory has been created.")
            
            # Assets directory has sub directories that need to be generated
            if directory_name == directory_names[0]:
                for assets_sub_directory_name in assets_sub_directory_names:
                    project_sub_directory_path = os.path.join(project_directory_path, assets_sub_directory_name)
                    os.makedirs(project_sub_directory_path)
                    print(f"'{project_sub_directory_path}' directory has been created.")    
    
    # Creates the files (main.lua and config.lua) with in the project directory
    def _create_sub_files(self):
        source_files = ['main.txt', 'config.txt']
        destination_files = ['main.lua', 'config.lua']
        
        for source_file, destination_file in zip(source_files, destination_files):
            # Create a file inside the folder
            source_file_content = file_util.content(source_file)
            file_name = os.path.join(self.project_name, destination_file)
            with open(file_name, 'w') as dest:
                dest.write(source_file_content)
                print(f"'{file_name}' file has been created and content written.")