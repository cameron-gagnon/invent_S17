#!/usr/bin/env python3.5

import sys
import os
from smtplib import SMTP
from email.mime.text import MIMEText


# PUT YOUR USERNAME AND PASSWORD FOR AN EMAIL ACCOUNT WITHIN THE STRINGS BELOW
EMAIL_USERNAME = ''
EMAIL_PASSWORD = ''


def get_email_information():
    """ Get the information from the user for the email to send. This includes
    the subject, body, and who to send it to """
    data = {}
    data['To'] = input("Who do you want to send this email to? ")
    data['Subject'] = input("What do you want the subject to be? ")
    data['Body'] = input("What do you want this email to say? ")
    print("Does this information look correct?\n")
    for field, content in data.items():
        print(field, ":", content)
    ans = input("\n[Y/n] Y to send, N to cancel: ")

    if ans.lower() == 'y':
        return data
    else:
        print("User canceled")
        sys.exit(0)

def create_email(data):
    """ Creates the email structure needed for the SMTP library """
    msg = MIMEText(data['Body'])
    msg['From'] = EMAIL_USERNAME
    msg['Subject'] = data['Subject']
    msg['To'] = data['To']
    return msg

def send_email(data, msg):
    """ Send the email using the SMTP library """
    try:
        smtp = SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_USERNAME, data['To'], msg.as_string())
        print("Success! Check your email inbox!")
    except Exception as e:
        print("Could not send email", e)

def generate_and_send_email():
    """ Perform all the steps necessary to send an email """
    data = get_email_information()
    # create the message
    msg = create_email(data)
    send_email(data, msg)

def check_variables():
    """ In order to not leak sensitive data, it's usually best practice to have
    environment variables set on your computer. This function checks that those
    variables are set """
    if not EMAIL_USERNAME or not EMAIL_PASSWORD:
        print("Please set your username and password within this file")
        sys.exit(1)

def main():
    check_variables()
    generate_and_send_email()

if __name__ == "__main__":
    main()
