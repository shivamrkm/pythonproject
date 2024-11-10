import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))

def mail_merge(csv_file, email_template, image_path):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            msg = MIMEMultipart('related')
            msg['From'] = sender_email
            msg['To'] = row['email']
            msg['Subject'] = "Personalized Email"
            
            with open(email_template, 'r') as template:
                email_body = template.read().format(name=row['name'])
            msg.attach(MIMEText(email_body, 'html'))
            
            with open(image_path, 'rb') as img_file:
                img = MIMEImage(img_file.read())
                img.add_header('Content-ID', '<image1>')
                img.add_header('Content-Disposition', 'inline', filename=os.path.basename(image_path))
                msg.attach(img)
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, row['email'], msg.as_string())
                print(f'Email sent to {row["email"]}')
if __name__ == "__main__":
    csv_file = 'contacts.csv'
    email_template = 'email_template.html'
    image_path = 'jh.png'
    mail_merge(csv_file, email_template, image_path)
