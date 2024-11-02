import os
import shutil
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import ImageGrab, Image
import pytesseract
import pyperclip

# 1. Mail Merge
def mail_merge(csv_file, email_template, sender_email, sender_password, smtp_server, smtp_port):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = row['email']
            msg['Subject'] = "Personalized Email"
            with open(email_template, 'r') as template:
                email_body = template.read().format(name=row['name'])
            msg.attach(MIMEText(email_body, 'plain'))
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, row['email'], msg.as_string())
            server.quit()

# 2. Auto Desktop Declutter Organizer
def declutter(folder_path, move_files=True):
    file_types = {}
    for item in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, item)):
            ext = item.split('.')[-1]
            if ext not in file_types:
                file_types[ext] = []
            file_types[ext].append(item)
    for ext, items in file_types.items():
        ext_folder = os.path.join(folder_path, ext.upper() + '_FILES')
        os.makedirs(ext_folder, exist_ok=True)
        for item in items:
            if move_files:
                shutil.move(os.path.join(folder_path, item), os.path.join(ext_folder, item))
            else:
                shutil.copy(os.path.join(folder_path, item), os.path.join(ext_folder, item))

# 3. Clipboard OCR
def clipboard_ocr():
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        text = pytesseract.image_to_string(image)
        pyperclip.copy(text)

# Example Usage:
# mail_merge('contacts.csv', 'email_template.txt', 'your_email@gmail.com', 'your_password', 'smtp.gmail.com', 587)
# declutter('/path/to/your/desktop', move_files=True)
# clipboard_ocr()
