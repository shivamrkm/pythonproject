import requests
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
urls = ['http://example.com', 'http://another-example.com']
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
recipient_email = os.getenv('RECIPIENT_EMAIL')

def check_website_status(urls, sender_email=sender_email, sender_password=sender_password, recipient_email=recipient_email, smtp_server='smtp.gmail.com', smtp_port=587):
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code != 200:
                send_alert(sender_email, sender_password, recipient_email, url, smtp_server, smtp_port)
        except requests.exceptions.RequestException:
            send_alert(sender_email, sender_password, recipient_email, url, smtp_server, smtp_port)

def send_alert(sender_email, sender_password, recipient_email, url, smtp_server, smtp_port):
    msg = MIMEText(f'Website {url} is down.')
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Website Down Alert'
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f'Alert sent for {url}')
    except Exception as e:
        print(f'Error sending alert for {url}: {e}')
    finally:
        server.quit()


if __name__ == "__main__":

    check_website_status(urls, sender_email, sender_password, recipient_email)
