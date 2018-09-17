import configparser
from fetchweather import *
from mail import *


def main():
    """
    Gets weather and sends it in an email

    This function uses fetchweather and mail to send an email based on the email settings
    and location in the weatherbot.ini file
    """
    # Get configuration file
    config = configparser.ConfigParser()
    config.read('weatherbot.ini')

    # Get weather info
    data = get_current_forecast(config['weather']['coordinates'])

    # Send an email if the info was fetched successfully
    if data != "Error":
        print(data)
        send_mail('sam.stifter@gmail.com', "Weather", data)


main()



