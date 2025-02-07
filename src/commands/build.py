import os
import subprocess
from util import os_util

class Build:
    
    def __init__(self):
        pass
    
    def build_love_project(self):
        os_util.compress_directory(os.getcwd(), "test")