import requests

# i = 14038
# while True:
	# addr = 'https://prvs.sindhpolice.gov.pk/verification/CheckCertificate?id='+str(i)
	# page = requests.get(addr)
	# re = page.text.find('ASIF')
	# print(re)
	# print(i)
	# if(i >14200):
		# print(i)
		# print(re)
		# break
	
	# i = i+1

i = 78600
while True:
	addr = 'https://prvs.sindhpolice.gov.pk/verification/CheckCertificate?id='+str(i)
	page = requests.get(addr)
	name = page.text[9074:9090]
	country =  page.text[10278:10320] 
	print(str(i)+','+name+','+country)
	if(i >14500):
		print(i)
		break
	
	i = i+1

