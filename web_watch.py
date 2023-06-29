import time
import socket
import hashlib
from urllib.request import urlopen, Request

target_host = "demo.testfire.net"
#target_port = 21
target_port = 80
# (address family for IPv4, TCP socket type)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
# grabbing information of a system available on a certain network and all the services running on its open ports
print("\n\n\n>> Initialising Fingerprinting using Sockets...\n")
# send some data
output = b"GET / HTTP/1.0\nHost: demo.testfire.net\n\n"
client.send(output)
# receive some data
for i in range(0, 40):
    response = client.recv(100)
    print(response)
    print("\n")
print("\n\n>> Initialising Port Scanner...\n")
target = input('Enter the host you would like to scan: ')
# returns the IP address of the given host name (target)
target_ip = socket.gethostbyname(target)
print('Scanning Host', target_ip + '...')
print("\n")


def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False


start = time.time()

for port in range(5):
    if port_scan(port):
        print(f'<Port {port} is open>')
    else:
        print(f'<Port {port} is closed>')

end = time.time()
print(f'Time taken: {end-start:.2f} seconds')

port = int(input("\nEnter the port number to be scanned: "))
print("\n")

if port_scan(port):
    print('<Port', port, 'is open>')
else:
    print("<Port", port, "is closed>")

# setting the URL you want to monitor
url = Request('https://youtube.com/',
              headers={'User-Agent': 'Mozilla/5.0'})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
# a hash is a function that converts an input of letters and numbers into an encrypted output of a fixed length (encryption)
# the hash file is changed when the data is modified because the information within the file has changed and it is considered a new/different file.
currentHash = hashlib.sha224(response).hexdigest()
# SHA = Secure Hash Algorithm
print("\n\n>> Initialising Web Server Monitoring...")
time.sleep(10)
while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()

        # create a hash
        # hexdigest returns the encypted data in a hexadecimal format
        currentHash = hashlib.sha224(response).hexdigest()

        # wait for 30 seconds
        time.sleep(30)

        # perform the get request
        response = urlopen(url).read()

        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()

        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue

        # if something changed in the hashes
        else:
            # notify
            print("\nThere were recent changes in the hashes of <<youtube.com>>\n\n")

            # again read the website
            response = urlopen(url).read()

            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

            # wait for 30 seconds
            time.sleep(30)
            continue

    # To handle exceptions
    except Exception as e:
        continue
