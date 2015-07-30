# Last modified: 2015-07-30
# -Samuel Micka
.----------------------------------------------------.
 .--------------.  .--------------.  .--------------. 
 |   ______     |  |     ______   |  |   ______     | 
 |  |_   __ \   |  |   .' ___  |  |  |  |_   __ \   | 
 |    | |__) |  |  |  / .'   \_|  |  |    | |__) |  | 
 |    |  ___/   |  |  | |         |  |    |  ___/   | 
 |   _| |_      |  |  \ `.___.'\  |  |   _| |_      | 
 |  |_____|     |  |   `._____.'  |  |  |_____|     | 
 |              |  |              |  |              | 
 '--------------'  '--------------'  '--------------' 
'----------------------------------------------------' 


Hello and welcome to Ping through CDN-Proxies (pcp).

pcp is a tool designed to estimate latency between arbitrary hosts in the Internet. 
It was developed in the Montana State University's Computer Science Networking Lab. 

SYSTEM REQUIREMENTS:

1) This version of the software has been tested on linux and mac
2) You need to have an up to version of python installed (version Python 2.7.6 or higher)
3) You need to have wireshark installed and with it tshark (should come with wireshark)

USING THE TOOL:

As part of using our latency estimation service we ask that you help us collect data to 
improve our estimations. To do this we request that you run pcp_daemon.py on your machine
while you browse the internet or conduct work. This script will monitor tcp connection set 
up RTTs and check to see if the other ip address is a CDN. We then record your IP address,
the CDN IP address, and the rtt between them. 

To use the tool you can simply run pcp.py using the command 'python pcp.py'. The script will
require that you enter a valid network interface and ip address for your machine (it will also
give you the option to run ifconfig). Then you can run queries to estimate latency between hosts.

The coverage of the tool will increase quickly as more users help us collect data. 


DEVELOPMENT:

If you want to set up your own server to collect your own data or work on developing the tool further
the server code is located in the server_code/ directory. You will find the php wrappers for our
python scripts and the files associated with handling all back end functionality.

CONTACT:

If you find any issues or bugs with the scripts please contact sam.micka@cs.montana.edu

