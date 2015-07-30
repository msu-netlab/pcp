import urllib2, urllib
def main():
  print ".----------------------------------------------------."
  print " .--------------.  .--------------.  .--------------. "
  print " |   ______     |  |     ______   |  |   ______     | "
  print " |  |_   __ \   |  |   .' ___  |  |  |  |_   __ \   | "
  print " |    | |__) |  |  |  / .'   \_|  |  |    | |__) |  | "
  print " |    |  ___/   |  |  | |         |  |    |  ___/   | "
  print " |   _| |_      |  |  \ `.___.'\  |  |   _| |_      | "
  print " |  |_____|     |  |   `._____.'  |  |  |_____|     | "
  print " |              |  |              |  |              | "
  print " '--------------'  '--------------'  '--------------' "
  print "'----------------------------------------------------' \n"

  print "Welcome to pcp\nINPUT: 2 valid IP addresses\nOUTPUT: Estimated latency between the IP addresses.\nFor questions please see the README.txt file\n"
  while True:
    #TODO: Insert code to check if pcp_daemon is running
    ip1 = raw_input("Please enter the first IP: ")
    ip2 = raw_input("Please enter the second IP: ")

    full_url = "http://nl.cs.montana.edu/pcp/pcp.php?ip1="+ip1+"&ip2="+ip2;
    data = urllib2.urlopen(full_url)
    print str(data.read())+"\n"
  

if __name__ == '__main__': main()
