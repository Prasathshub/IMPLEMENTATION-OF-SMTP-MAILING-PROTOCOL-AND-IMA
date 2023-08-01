import smtplib
import os
from email import *
user=input("Enter mail\nsender: ")
password=input("Enter password\npassword:")
receiver=input("Enter a valid email to whom you want to send:")
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(user, password)
print("Login success\n")
subject=input('Enter the subject\n\n')
body=input('Enter body\n\n')
msg=f'Subject: {subject}\n\n{body}'
server.sendmail (user,receiver,msg)
print("Email has been sent\n")
print()
print("Do you want to send mail to any one else.IF YES give input as yes else no")
again=input("yes or no for resending:")
if again=='yes':
    receiver=input("Enter a valid email to whom you want to send\n receiver:")
    subject=input('Enter subject\n\n')
    body=input('Enter body\n\n')
    print("Email has been sent\n")
    msg=f'Subject: {subject}\n\n{body}'
    server.sendmail (user, receiver, msg)
    print()
import mimetypes
from bs4 import BeautifulSoup
import imaplib, email
print()
print('Now we are going to retrieve mails:\n')
con=imaplib.IMAP4_SSL("imap.gmail.com")
con.login(user, password)
print("We have successfully logged in to the account", user, "\t", password, "\t to retrieve mails")
print("Now you are seeing the list of mails in the inbox:")
print()
print(con.list())
print()
con.select("INBOX")
result,data=con.uid('search', None, "ALL")
print('the above numbers represent the unique id of mails')
print()
print(data)
print()

inboxlist=data[0].split()
print(inboxlist)
var='yes'
print()
while var=='yes':
    print()
    print("IF YOU WANT TO SEE ALL MAILS GIVE yes ELSE no:\n")
    yesorno=input("Enter YES or NO:")
    if yesorno=='yes':
        for item in inboxlist:
            result2,maildata=con.uid('fetch',item,'(RFC822)')
            print()
            print()
            rawmail=maildata[0][1].decode("utf-8")
            mailmessage=email.message_from_string(rawmail)
            print()
            print()
            print('To:',mailmessage['To'])
            print()
            print('From:',mailmessage['From'])
            print()
            print('Subject:',mailmessage['subject'])
            print()
            date=mailmessage['date']
            counter=1
            for part in mailmessage.walk():
                if part.get_content_maintype()=="multipart":
                    continue
                filename=part.get_filename()
                content_type=part.get_content_type()
                if not filename:
                    ext=mimetypes.guess_extension(content_type)
                    if not ext:
                        ext='.bin'
                filename='msg-part-%08d%s'%(counter,ext)
            counter+=1
            print(content_type)
            if "plain" in content_type:
                print(part.get_payload())
            elif "html" in content_type:
                html_=part.get_payload()
                soup=BeautifulSoup(html_,"html.parser")
                text=soup.get_text()
                print('Subject',mailmessage['subject'])
                print()
                print(text)
            else:
                print(content_type)
        else:
            print()
            print("Enter the no in the list which you want to retreive: PLZ ENTER THE NO IN THE DATA")
            print()
            item=input("enter no: ")
            result2,maildata=con.uid('fetch',item,'(RFC822)')
            print()
            print()
            rawmail=maildata[0][1].decode("utf-8")
            mailmessage=email.message_from_string(rawmail)
            print()
            print()
            print('To:',mailmessage['To'])
            print()
            print('From:',mailmessage['From'])
            print()
            print('Subject:',mailmessage['subject'])
            print()
            date=mailmessage['date']
            counter=1
            for part in mailmessage.walk():
                if part.get_content_maintype()=="multipart":
                    continue
                filename=part.get_filename()
                content_type=part.get_content_type()
                if not filename:
                    ext=mimetypes.guess_extension(content_type)
                    if not ext:
                          ext='.bin'
                          filename='msg-part-08d%s' %(counter,ext)
                counter += 1
                print(content_type)
                if "plain" in content_type:                    
                    print(part.get_payload())
                elif "html" in content_type:
                    html_=part.get_payload()
                    soup=BeautifulSoup(html_,"html.parser")
                    text=soup.get_text()
                    print('subject',mailmessage['subject'])
                    print()
                    print(text)
                else:
                    print(content_type)
                print()
                print("Do you want to still retrieve or do u want to quit ")
                print("IF YOU WANT TO CONTINUE ENTER YES")
                var=input("yesorno: ")
                if var=='no':
                    print("\n\n\n")
                    print("THANK YOU ALL")
                    break
        server.quit()
