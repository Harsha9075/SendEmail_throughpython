#Importing smtlib library for transactions between E-mails.
import smtplib

#Sender Email
senderemail = "harshaasapu907@gmail.com"
#Reciever Email
recieveremail = "harshaontrade@gmail.com"

password = input(str("Please enter your password:"))    #Enter your password here.

message = "Congratulations, you have won the lottery!."   #This message displays in the recievers inbox.

server = smtplib.SMTP('smtp.gmail.com',587) #Connection with the server
server.starttls()

#Enter your credentials
server.login(senderemail,password)
print("------------Successfull login-------------")

#Finally,Sending the mail 
server.sendmail(senderemail,recieveremail,message)
print("-----------Message has been delivered to",recieveremail)

