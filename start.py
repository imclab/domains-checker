#!/usr/bin/python3

import whois
import time
import datetime
import random

def wait():
	time.sleep(random.randint(5,8))

def skipDomain(domain):
	print(domain.rstrip('\n'), 'is paid for 1 year more\n')
	wait()

def addDomainToTxtFile(domain):
	domains_result.write(domain)
	print(domain.rstrip('\n'), ' is free, write to the file!\n')
	wait()

domains = open("source.txt", "r").readlines()
domains_result = open("free_domains.txt", "w")
for domain in domains:
	try:
		print('Begin to watch ', domain.rstrip('\n'))
		result = whois.query(domain)
		now_date = datetime.date.today()
		if result.free_date.year != now_date.year:
			skipDomain(domain)
		else:
			addDomainToTxtFile(domain)
	except AttributeError:
		addDomainToTxtFile(domain)
	finally:
		pass
		
print("Done.")
