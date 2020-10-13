import sys
import imaplib
import email
import email.header
import getpass
import datetime
from email.utils import parseaddr

EMAIL_ACCOUNT = "myemail@yahoo.com"

mail = imaplib.IMAP4_SSL('imap.yahoo.com')
mail.login(EMAIL_ACCOUNT, 'mypassword')
mail.list()

mail.select("inbox") #Connect to inbox

result, data = mail.uid('search', None, '(HEADER Subject "New Zelle Payment Received")') #search email given subject
body = data[0][1]
