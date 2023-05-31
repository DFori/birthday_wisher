##################### Normal Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random
my_gmail = "alphaanimefori99@gmail.com"
password ="gpciimqxeazxbxof"

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    celebrant = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        real_content = content.replace("[NAME]", celebrant["name"])


    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs=celebrant["email"],
                            msg=f"Subject:Happy Birthday\n\n{real_content}")



