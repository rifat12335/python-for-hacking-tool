# Domain TO IP
import socket
import pyfiglet

banner = pyfiglet.figlet_format("Domain to ip")
print (banner)
domain_name = input("Enter Your target Domain name:")
ip = socket.gethostbyname(domain_name)
print (ip)