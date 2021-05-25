import smtplib
import json 
class mailApp():
	def __init__(self):
		with open("mail.json","r") as mailStr:
			self.mail=json.load(mailStr)
	def sendMail(self):
		mail=self.mail
		gmailaddress=mail["sender"]
		gmailpassword=mail["password"]
		mailto=mail["receiver"]
		print(gmailaddress,gmailpassword,mailto,flush=True)
		mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
		mailServer.ehlo()
		mailServer.starttls()
		mailServer.ehlo()
		mailServer.login(gmailaddress , gmailpassword)
		msg=mail["message"]
		for receiver in mailto:
			print(receiver,flush=True)
			mailServer.sendmail(gmailaddress, mailto , msg)
		print("data sendet")
		mailServer.quit()

def main():
	mail=mailApp()
	mail.sendMail()
if __name__ == '__main__':
	main()
