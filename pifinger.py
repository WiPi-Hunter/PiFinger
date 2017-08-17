# coding=utf-8
from termcolor import colored
import netifaces
import commands
import socket
from time import gmtime, strftime
import os, sys


banner = """
 _______   _   ________  _                                  
|_   __ \ (_) |_   __  |(_)                                 
  | |__) |__    | |_ \_|__   _ .--.   .--./) .---.  _ .--.  
  |  ___/[  |   |  _|  [  | [ `.-. | / /'`\;/ /__\\[ `/'`\] 
 _| |_    | |  _| |_    | |  | | | | \ \._//| \__., | |     
|_____|  [___]|_____|  [___][___||__].',__`  '.__.'[___]    
                                    ( ( __))    

 [---]   Just for fun and security @octosec    [---]
 [---]   W:besimaltinok.com | T:altnokbesim    [---]
 [---]                G:besimaltnok            [---]
 ---------------------------------------------------
    """

def wifi_score_logging(timelog, mac, ssid, score, is_pineapple):
	log = timelog, mac, ssid, score, is_pineapple
	with open("/var/log/wifi_scores.log", "a") as f:
		f.write(str(log)+"\n")
		f.flush()
		f.close()
	

def previous_wifi():
	open_wifi = []
	wifi = os.listdir("/etc/NetworkManager/system-connections/")
	for w in wifi:
		data = open("/etc/NetworkManager/system-connections/"+w).read()
		if "wifi-security" not in data:
			open_wifi.append(w)
			print "[=] ", w
	return open_wifi
			 

def default_port(gateway):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(3)
	result = sock.connect_ex((gateway, 1471))
	sock.close()
	if result == 0:
		return 1
	else:
		return 0


def default_hostname(gateway):
    hostname = commands.getoutput("nslookup " + gateway +" | grep 'name = ' | awk '{print $4}'")
    if "Pineapple.lan." in hostname:
        return 1
    else:
		return 0

def manufacturer_mac(manufmac, interface):
    output = commands.getoutput("iwconfig " + interface + " | awk '/Access Point:/ {print $6}'")
    m = output[0:8]
    for i in manufmac:
	   if i == output[0:8]:
		   return 1
	   else:
		   return 0


if __name__ == "__main__":
	is_pineapple = False
	timelog = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	manufmac = ["00:C0:CA", "00:13:37"]
	print banner
	ifaces = netifaces.interfaces()
	print "[*] Available interfaces: ", ifaces
	interface = raw_input("[*] Please select the wireless interface you wish to use: ")
	print "-----------------------------------------------------\n"
	if interface in ifaces:
		internet = commands.getoutput("iwconfig " + interface + "| awk '/Access Point:/ {print $4}'")
		if internet != "Not-Associated" and "no wireless extensions" not in internet:
		   gateway = commands.getoutput("ip route show default | grep " + interface + "| awk '/default/ {print $3}'")
		   ssid = commands.getoutput("iwconfig "+ interface +"| awk '/ESSID:/ {print $4}' | awk -F: '{print $2}'")
		   ssid = ssid.split("ESSID")[-1][1:-1]
		   mac  = commands.getoutput("iwconfig " + interface + " | awk '/Access Point:/ {print $6}'")
		   port = default_port(gateway)
		   manuf = manufacturer_mac(manufmac, interface)
		   hostname = default_hostname(gateway)
		   print "\033[1m[--] Access Point:\t", mac
		   print "\033[1m[--] SSID:\t\t", ssid
		   print "\033[1m[--] --------------------------------\n"
		   print "\033[1m[###] Previous Connected WiFi - OPN:\n"
		   open_w = previous_wifi()
		   score = port + manuf + hostname + len(open_w)
		   print colored("\n\033[1mCalculate risk score for your network:\n", "green")
		   print "[*] Manufacturer:\t", manuf
		   print "[*] Port:\t\t", port
		   print "[*] Nslookup:\t\t", hostname
		   print "[*] OPN Network count:\t", len(open_w)
		   print colored("\n\033[1m[?] Your wifi score: " + str(score), "green")
		   if score > 2 and 1 in (port, hostname, manuf):
			   is_pineapple = True
			   print colored("\033[1m[-*-] You can fall into the trap - Fake access points", "yellow")
			   print colored("\033[1m[!!!] This network can be dangerous - WiFi-Pineapple", "red")
			   wifi_score_logging(timelog, mac, ssid, score, is_pineapple)
		   elif score > 2:
			   print colored("\033[1m[-*-] You can fall into the trap - Fake access points", "yellow")
			   wifi_score_logging(timelog, mac, ssid, score, is_pineapple)
			  
		else:
		   print "[!!] \033[1mNot-Associated with any wireless network"
	else:
		print "[!!] Please select available interfaces"
