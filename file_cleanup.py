import os

folder = '/users/kjdav/desktop'

entries = os.scandir(folder)

for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory', entry.name)