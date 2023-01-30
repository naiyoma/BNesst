import os
import schedule
import time
import smtplib
import logging
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

logging.basicConfig(filename='email.log', level=logging.INFO)

def send_email():
    try:
        import pdb; pdb.set_trace()
        user = "Aurelia"
        password = "1234"
        sender = "aurelia@gmail.com"
        recipients = ["lankas.aurelia@gmail.com", "aurelianaiyoma3@gmail.com"]
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        message = "Hello, attached below is the annual reports"
        smtp_object.ehlo()
        smtp_object.starttls()
        smtp_object.ehlo()
        smtp_object.login('lankas.aurelia@gmail.com', 'wvjtvykjgegwxsjo')
        for receiver in recipients:
            import pdb; pdb.set_trace()
            message = MIMEMultipart("related")
            message["Subject"] = "Daily Report"
            message["from"] = sender
            message["To"] = receiver
            file_path = "/home/naiyoma/Documents/LankasB__CV.pdf"
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(file_path, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
            message.attach(part)
            smtp_object.sendmail(sender, receiver, message.as_string())
        smtp_object.quit()
    except Exception as e:
        logging.error(e)
    else:
        logging.info('Email sent to {}'.format(receiver))

schedule.every().day.at("18:55").do(send_email)


while True:
    import pdb; pdb.set_trace()
    schedule.run_pending()
    time.sleep(1)



