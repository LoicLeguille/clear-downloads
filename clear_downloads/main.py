import os
import shutil
import sys

def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def get_application_name():
    if getattr(sys, 'frozen', False):
        return os.path.basename(sys.executable)
    elif __file__:
        return os.path.basename(__file__)

for root, dirs, files in os.walk(get_download_path()):
    for f in files:
        if f != get_application_name():
            os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))
