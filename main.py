from datetime import datetime
import pandas
import random
import smtplib
today_date=datetime.now()
today_tuple=(today_date.month,today_date.day)
data=pandas.read_csv("birthdays.csv")
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (inex,data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    file_path=f"letter_templates\letter_{random.randint(1,3)}.txt"
    birthday_person=birthdays_dict[today_tuple]
    with open(file_path) as templates:
        t=templates.read()
        mod_t= t.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user="wasifsyed02@yahoo.com",password="ztrxlwlldzavlxxw")
        connection.sendmail(from_addr="wasifsyed02@yahoo.com",to_addrs=birthday_person["email"],msg=f"Subject:Happy birthday\n\n{mod_t}")




