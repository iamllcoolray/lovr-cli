import os
import subprocess
from util import os_util

class Get:
    
    def __init__(self, library_name):
        self.library_name = library_name
        
    def get_third_party_library(self):
        git_path = os_util.find_application("git")
        
        print(git_path)