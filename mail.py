import smtplib
import configparser
import os.path
from email.mime.text import MIMEText


def send_mail(to_address, subject, message_body):
    """Sends the specified mail

    Uses the given information as well as information in a configuration file to send an
    email.
    Args:
        to_address (str): the email address to send the message to
        subject (str): the subject of the message
        message_body (str): The content of the message to be sent
    """
    # Get configuration file
    CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'weatherbot.ini')
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)

    # Construct the message
    msg = MIMEText(message_body)

    # Add the appropriate headers
    msg['Subject'] = subject
    msg['From'] = config['email']['from']
    msg['To'] = to_address

    # Send the message
    smtp = smtplib.SMTP(config['email']['server'], config['email']['port'])
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config['email']['user'], config['email']['password'])
    smtp.sendmail(config['email']['user'], to_address, msg.as_string())
    smtp.quit()
