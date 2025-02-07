import os
import subprocess
from util import os_util

class Build:
    
    def __init__(self):
        pass
    
    def build_love_project(self):
        # Get the current working directory
        current_directory = os.getcwd()

        # Get the current directory name
        directory_name = os.path.basename(current_directory)
        
        os_util.compress_directory(current_directory, directory_name)