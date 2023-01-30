import os
import ftplib
import shutil
import schedule
import time
import logging
from ftplib import FTP


local_directory = '/home/naiyoma/Documents/ftp_org/'

logging.basicConfig(filename='data_transfer.log', level=logging.INFO)

def process_data():
    ftp = FTP("ftp.pureftpd.org")
    ftp.login()
    files = ftp.nlst()
    print(files)
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
        try:
            shutil.move(local_directory + file, local_directory + file)
            logging.info(f"{file} is a directory.")
        except ftplib.error_perm as e:
            logging.info(f"{file} successfullt transfered.")

schedule.every().day.at("09:00").do(process_data)

while True:
    schedule.run_pending()
    time.sleep(1)