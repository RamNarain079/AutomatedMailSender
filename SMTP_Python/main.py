import datetime as dt
import smtplib

my_email = 'your-email@gmail.com' # your email account
password = '*' * 16 # 16-letter app password

connection = smtplib.SMTP('smtp.gmail.com')

today = dt.datetime.now()
with (connection):
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(from_addr=my_email, to_addrs='*****@gmail.com',msg=f"Subject: Played around with SMTP on \n\n{today}")



