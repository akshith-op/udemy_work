import smtplib

my_email = "python.lib123@gmail.com"
password = "udemy123$"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="ashwath12.isola@gmail.com",
    msg="Subject:test\n\nThis is Akshith",
)
connection.close()
