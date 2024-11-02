import requests
import smtplib
from email.mime.text import MIMEText

def check_website_status(urls, sender_email, sender_password, recipient_email, smtp_server, smtp_port):
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
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

# Example Usage:
# urls = ['http://example.com', 'http://another-example.com']
# check_website_status(urls, 'your_email@gmail.com', 'your_password', 'recipient_email@gmail.com', 'smtp.gmail.com', 587)
