#!/usr/bin/env python
#pcp tool
#Sniffs only the source and destination addresses of tcp packets
#written and tested on linux in python version: 2.7.6
#Last modified by Samuel Micka 2015-07-17
 
import socket, sys, os, fcntl, struct, getpass, urllib2, urllib

# Function that returns True if the IP address is a CDN from a known company, False otherwise
def check_for_cdn(addr):
	akamai = "akamaitechnologies.com"
	amazon = "cloudfront.net"
	softlayer = "reverse.softlayer.com"
	facebook = "fbcdn.net"
	level3 = "footprint.net"
	limelight = "llnw.com"
	host = os.popen('host '+addr).read()
	#print host
	if host.find(akamai) != -1 or host.find(amazon) != -1 or host.find(softlayer) != -1 or host.find(facebook) != -1 or host.find(level3) != -1 or host.find(limelight) != -1:
		#print host
		return True
	else:
		return False

def main():
  #local_ip_and_interface = get_ip_and_interface()
  #local_ip = local_ip_and_interface[0]
  #local_interface = local_ip_and_interface[1]
  print "We require that you choose a network interface and ip for the tshark to monitor \n"
  ifconfig = raw_input("Run 'ifconfig' to identify valid network interface and ip? (y/n)")
  if ifconfig == "y":
    print os.popen("ifconfig").read()
  local_ip = raw_input("Enter IP: ")
  local_interface = raw_input("Enter Network Interface: ")
  tshark_command = "sudo tshark -Y 'ip.dst=="+local_ip+" and tcp.analysis.ack_rtt > 0.0' -Tfields -E header=n -e ip.src -e ip.dst -e tcp.analysis.ack_rtt -i "+local_interface+" -c 100"
  print tshark_command
  sudo_pass = getpass.getpass()
  while True:
    try:
      tshark_value = os.popen('echo %s|sudo -S %s' % (sudo_pass, tshark_command)).read()
      print "\n\n\n"
      tshark_value = tshark_value.split("\n")
      
      for l in tshark_value:
        if l == "":
          break
        split_l = l.split("\t")
        s_addr = split_l[0]
        d_addr = split_l[1] #our address
        rtt = split_l[2]
        if check_for_cdn(s_addr):
          full_url = "http://nl.cs.montana.edu/pcp/save_measurements.php?user_ip="+d_addr+"&cdn_ip="+s_addr+"&rtt="+rtt
          data = urllib2.urlopen(full_url)
          print data.read()
          print "CDN FOUND: "+str(s_addr)+" with latency: "+str(rtt)+" and stored in Database"
      print "\n\n\n"
		  #if check_for_cdn(s_addr):
			#  #send the addresses and rtt to our server
      #  print "SUCCESS: "
    except Exception,e:
      print "Something went wrong: "+str(e)
		 




if __name__ == '__main__':main()
