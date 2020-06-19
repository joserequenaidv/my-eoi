#Standard libraries
import datetime
import os
import shutil
import statistics
import sys
import zipfile

#External libraries
import arrow

path = input('What do you want to backup, sir?')
shutil.copy('*.py', )

def home_backup():
    file_extensions = ['*.py', '*.md', '*.pynb', '*.rst']
    config_files = ['*.zshrc', '*.gitconfig', '*.vimrc', '*.ipython']
    backup_file = zipfile.ZipFile('backup.zip', 'w')
    for file_name in os.listdir(path):
        file_root, file_ext  = os.path.splitext(file_name)
        if file_root in config_files:
            print (f'Saving {file_names}')
            backup_file.write(file_name)
    backup_file.close()

def user_os(path, file_extensions):
    if sys.platform.startswith('linux'):
        monday_backup(path, file_extensions)

# Execution
# Linux systems

#MacOS systems

#Windows systems

if __name__ == '__main__':

    file_extensions = ['.py', '.md', '.pynb', '.rst']
    file_names = ['.zshrc', '.gitconfig', '.vimrc', '.ipython']
    home_backup()
