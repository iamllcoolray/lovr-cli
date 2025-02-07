import os
import subprocess
import sys
import shutil

def compress_directory(directory_path, output_zip_file):
    output_zip_path = os.path.join(os.getcwd(), 'build')
    full_output_zip_path = os.path.join(output_zip_path, output_zip_file)
    
    # Compress the directory into a zip file
    shutil.make_archive(full_output_zip_path, 'zip', directory_path)
    print(f"Directory '{directory_path}' has been compressed into '{full_output_zip_path}.zip'")
    _rename_zip_to_love(full_output_zip_path+".zip")
    
def _rename_zip_to_love(zip_file_path):
    # Check if the file exists
    if os.path.exists(zip_file_path):
        # Create the new path with .love extension
        love_file_path = os.path.splitext(zip_file_path)[0] + '.love'
        
        # Rename the file
        os.rename(zip_file_path, love_file_path)
        print(f"File renamed to {love_file_path}")
    else:
        print(f"File '{zip_file_path}' does not exist.")

def find_application(app_name: str) -> str:
    if sys.platform == "win32":
        return _find_application_on_windows(app_name)
    elif sys.platform == "darwin":  # macOS
        return _find_application_on_mac(app_name)
    elif sys.platform.startswith("linux"):  # Linux
        return _find_application_on_linux(app_name)
    else:
        return "Unsupported OS."

def _find_application_on_windows(app_name: str) -> str:
    try:
        result = subprocess.run(['where', app_name], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"{app_name} not found in PATH."
    except Exception as e:
        return str(e)

def _find_application_on_mac(app_name: str) -> str:
    try:
        result = subprocess.run(['which', app_name], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            app_path = f'/Applications/{app_name}.app'
            if os.path.exists(app_path):
                return app_path
            else:
                return f"{app_name} not found in PATH or /Applications."
    except Exception as e:
        return str(e)

def _find_application_on_linux(app_name: str) -> str:
    try:
        result = subprocess.run(['which', app_name], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"{app_name} not found in PATH."
    except Exception as e:
        return str(e)