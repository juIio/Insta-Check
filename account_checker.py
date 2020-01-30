import datetime
import requests
import smtplib
import time
import ssl
import bs4

not_available = True
target_username = 'banks'
target_site = 'https://instagram.com/' + target_username + "/"
email_from = 'email@gmail.com'
email_from_password = 'password'
email_to = 'sendto@gmail.com'
message_to_send = 'Username is available now, go get it!\n' + target_site + '\n'


def start_ig_loop():
    global not_available

    while not_available:
        try:
            session = requests.get(target_site)
            document = bs4.BeautifulSoup(session.content, 'html.parser')

            page_title = document.title.text

            if "Not Found" in page_title:
                send_email()
                not_available = False
                exit(1)
            else:
                print(datetime.datetime.now().strftime('[%m-%d-%y, %I:%M:%S %p]') + ' Not available yet')
                time.sleep(1)
        except Exception as e:
            print(e)


def send_email():
    smtp_server = 'smtp.gmail.com'
    port = 465

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email

    try:
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.ehlo()
        server.login(email_from, email_from_password)
        server.sendmail(email_from, email_to, message_to_send)
    except Exception as e:
        # Print any error messages to stdout
        print(e)


start_ig_loop()
