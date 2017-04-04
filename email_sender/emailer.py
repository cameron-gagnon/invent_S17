#!/usr/bin/env python3.5

import sys
import os
from smtplib import SMTP
from email.mime.text import MIMEText

def get_options():
    """ Get the information from the user for the email to send. This includes
    the subject, body, and who to send it to """
    data = {}
    data['To'] = input("Who do you want to send this email to? ")
    data['Subject'] = input("What do you want the subject to be? ")
    data['Body'] = input("What do you want this email to say? ")
    print("Does this information look good?\n")
    for field, content  in data.items():
        print(field, ":", content)
    ans = input("\n[Y/n] Y to send, N to cancel: ")

    if ans.lower() == 'y':
        return data
    else:
        print("User canceled")
        sys.exit(0)

def create_email_content(data):
    """ Creates the email structure needed for the SMTP library """
    msg = MIMEText(data['Body'])
    msg['From'] = os.getenv('EMAIL_USER')
    msg['Subject'] = data['Subject']
    msg['To'] = data['To']
    return msg

def send_email(data, msg):
    """ Send the email using the SMTP library """
    try:
        smtp = SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
        smtp.sendmail(os.getenv('EMAIL_USER'), data['To'], msg.as_string())
        print("Success! Check your email inbox!")
    except Exception as e:
        print("Could not send email", e)

def generate_and_send_email():
    """ Perform all the steps necessary to send an email """
    data = get_options()
    # create the message
    msg = create_email_content(data)
    send_email(data, msg)

def check_environment_variables():
    """ In order to not leak sensitive data, it's usually best practice to have
    environment variables set on your computer. This function checks that those
    variables are set """
    if not os.getenv('EMAIL_USER') or not os.getenv('EMAIL_PASS'):
        print("Please run: export EMAIL_USER='YOUR_EMAIL_HERE@gmail.com'\n"
              "and: export EMAIL_USER='YOUR_EMAIL_PASSWORD_HERE'")
        sys.exit(1)

def main():
    check_environment_variables()
    generate_and_send_email()

if __name__ == "__main__":
    main()
