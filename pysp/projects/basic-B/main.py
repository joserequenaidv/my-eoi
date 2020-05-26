import os
import sys
import zipfile

#Linux systems
if sys.platform.startswith('linux'):

    zf = zipfile.ZipFile('files.zip', 'w')
    path = "/home/joserequenaidv/"

    for file_name in os.listdir('joserequenaidv'):
        _, ext = os.path.splitext(file_name)

        if ext == '.zshrc':
            print(f"Guardando {file_name}")
            zf.write(file_name)

    zf.close()

#MacOS systems

#Windows systems
