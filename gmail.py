import smtplib
senderemail = "harshaasapu907@gmail.com"
recieveremail = "harshaontrade@gmail.com"
password = input(str("Please enter your password:"))
message = "Congratulations, you have won the lottery!."
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(senderemail,password)
print("------------Successfull login-------------")
server.sendmail(senderemail,recieveremail,message)
print("-----------Message has been delivered to",recieveremail)

