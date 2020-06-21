import os, sys


os.system ("figlet -f mono12 Apt-Get47 | lolcat -a")
print ("\033[32m")
print ('creat by J4YH33\n')
print ('Tool for Apt-Get47\n')
print ('youtube : APT-GET47\n')
print (" \033[34m ")

print ('[1] METASEC-kali\n')
print ('[2] NEBULA-kali\n')
print ('[3] METASEC-Termux\n')
print ('[4] NEBULA-Termux\n')
print ('[5] XTRACK-Termux\n')
print ('[0] exit\n')

A = input("เลือก :")

if A == "1" or A == "01":
   os.system ("clear")
   os.system ("git clone https://github.com/MALW4R3/METASEC-kali")
   os.system ("mv METASEC-kali /$HOME")
   os.system ("cd METASEC-kali")
   os.system ("sh setup.sh")
   os.system ("clear")
   os.system ("python tool.py")
elif A == "2" or A == "02":
   os.system ("clear")
   os.system ("git clone https://github.com/MALW4R3/NEBULA-kali")
   os.system ("mv NEBULA-kali /$HOME")
   os.system ("cd NEBULA-kali")
   os.system ("sh setup.sh")
   os.system ("clear")
   os.system ("python tool.py")
elif A == "3" or A == "03":
   os.system ("clear")
   os.system ("git clone https://github.com/MALW4R3/METASEC")
   os.system ("mv METASEC /$HOME")
   os.system ("cd METASEC")
   os.system ("sh setup.sh")
   os.system ("clear")
   os.system ("python tool.py")
elif A == "4" or A == "04":
   os.system ("clear")
   os.system ("git clone https://github.com/MALW4R3/NEBULA")
   os.system ("mv NEBULA /$HOME")
   os.system ("cd NEBULA")
   os.system ("sh setup.sh")
   os.system ("clear")
   os.system ("python tool.py")
elif A == "5" or A == "05":
   os.system ("clear")
   os.system ("git clone https://github.com/MALW4R3/XTRACK")
   os.system ("mv XTRACK /$HOME")
   os.system ("cd XTRACK")
   os.system ("sh setup.sh")
   os.system ("clear")
   os.system ("python tool.py")
elif A == "00" or A == "0":
   os.system("cd /$HOME")

