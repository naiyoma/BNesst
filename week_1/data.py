import os
import ftplib
import shutil
from ftplib import FTP



local_directory = '/home/naiyoma/Documents/ftp_org/'

def process_data():
    # import pdb; pdb.set_trace()
    ftp = FTP("ftp.pureftpd.org")
    ftp.login()
    files = ftp.nlst()
    print(files)
    # import pdb; pdb.set_trace()
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)
    for file in files:
        try:
            ftp.cwd(file)
            print(file, "is a directory.")
        except ftplib.error_perm as e:
            if "550" in str(e):
                ftp.retrbinary("RETR " + file, open(local_directory + file, 'wb').write)
            else:
                print(file + ": An error occured:", e)
    ftp.quit()
    for file in files:
        shutil.move(local_directory + file, internal_directory + file)

process_data()