import smtlib

S=smtplib.SMTP('smtp.gamil.com',587)
S.starttls()
S.login('ajith.astha@gmail.com','88676759014')
msg="hi"
msg=MIMEText('<a href="www.google.com">this is a link</a>','html')
S.sendmail("ajith.astha@gmail.com","ajith.astha@gamil.com",msg)
print("success")
S.quit()
