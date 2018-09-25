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
    weather_data = fetchweather.get_current_forecast(config['weather']['coordinates'])

    # Send an email if the info was fetched successfully
    if weather_data != "Error":
        print(weather_data)

        # Split the list of emails
        email_list = config['email']['to'].split(',')

        # Send to each address in the list
        for email in email_list:
            mail.send_mail(email, config['email']['subject'], weather_data)


main()



