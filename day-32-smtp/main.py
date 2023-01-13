##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import random
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day
MY_EMAIL = 'johndungao0624@gmail.com'
MY_PASSWORD = 'gelygolulbnnrqwb'
random_number = random.randint(1, 3)

# Open birthday file
df = pd.read_csv('birthdays.csv')
birthdays = df.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv
for person in birthdays:
    name = person['name']
    email = person['email']
    birthday_month = person['month']
    birthday_day = person['day']

    if birthday_month == month and birthday_day == day:
        # open random letters
        with open(f'./letter_templates/letter_{random_number}.txt') as template:
            letter_template = template.readlines()
            letter = ''.join(letter_template)
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            updated_letter = letter.replace('[NAME]', name)

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='maidenanne15@gmail.com',
                            msg=f'Subject: Happy Birthday! \n\n {updated_letter}')