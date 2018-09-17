import configparser
import os.path
import fetchweather
import mail


def main():
    """
    Gets weather and sends it in an email

    This function uses fetchweather and mail to send an email based on the email settings
    and location in the weatherbot.ini file
    """
    # Get configuration file
    CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'weatherbot.ini')
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)

    # Get weather info
    data = fetchweather.get_current_forecast(config['weather']['coordinates'])

    # Send an email if the info was fetched successfully
    if data != "Error":
        print(data)
        mail.send_mail(config['email']['to'], config['email']['subject'], data)


main()



