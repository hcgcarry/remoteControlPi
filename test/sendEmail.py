import smtplib

gmail_user = 'hcgcarry@gmail.com'  
gmail_password = ''

sent_from = gmail_user  
to = ['djjjimmyyy@gmail.com', 'hcgcarry@gmail.com']  
subject = 'OMG Super Important Message'  
body = 'Hey, whats up?\n\n- You'

email_text = 'door are open'

def send(pin):
	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()

		print 'Email sent!'
	except:  
		print 'Something went wrong...'
