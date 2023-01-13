# import smtplib
#
#
#
# message = """
# Dear Mayor,
# Ang panget mo!
# HAHAHAHA
# Mang Spam ako ng mga ganito
# Taena mo
#
# """
#
# with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
#     connection.starttls() # Make sures that the connection is secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs='vincentlozano21@gmail.com', msg=message)
#


import smtplib
import random
import datetime as dt

my_email = 'johndungao0624@gmail.com'
password = 'gelygolulbnnrqwb'
now = dt.datetime.now()
with open('quotes.txt', 'r') as data:
    quotes_data = data.readlines()
    quotes = [quote for quote in quotes_data]

# quotes_of_the_day = random.choice(quotes)

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    day = now.strftime('%A')
    if day == 'Thursday':
        for _ in range(5):
            connection.sendmail(from_addr=my_email,
                                to_addrs='Mikebiron08@gmail.com',
                                msg=f"Subject: Quotes of the Day \n\n {random.choice(quotes)}")
            print("Email Sent")
