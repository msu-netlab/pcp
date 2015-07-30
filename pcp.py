import urllib2, urllib, os

def check_for_daemon():
  with open("/tmp/pcp_daemon.txt", "r") as f:
    pid = int(f.readline())
  try:
    os.kill(pid, 0)
  except Exception:
    return False
  return True

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

    if not check_for_daemon():
      print "Please start the pcp daemon to help us provide better accuracy"
      print "Start the process by running 'python pcp_daemon.py' in your terminal"

    ip1 = raw_input("Please enter the first IP: ")
    ip2 = raw_input("Please enter the second IP: ")

    full_url = "http://nl.cs.montana.edu/pcp/pcp.php?ip1="+ip1+"&ip2="+ip2;
    data = urllib2.urlopen(full_url)
    print str(data.read())+"\n"
  

if __name__ == '__main__': main()
