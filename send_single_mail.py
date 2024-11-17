import yagmail
import os

sender = 'from_mail@mail.com'
receiver = 'to_mail@mail.com'

subject = 'Automated mail - python script'

content = """
This is the automated mail, ran via python script
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, content=content)

print('Email Sent!')