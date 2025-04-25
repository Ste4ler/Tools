import socket

target_host = "www.google.com" # The target host is the server we want to connect to
target_port = 80 # The target port is the port we want to connect to on the server

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Create a socket object in which AF_INET is for IPV4 Ip address and SOCK_DGRAM is the request is UDP not TCP

client.sendto(b"AAABBBCCC", (target_host,target_port))  # Send data to the server. The data is in bytes format, so we use b"AAABBBCCC" to send it as bytes.

data,addr = client.recvfrom(4096)   # Capture the response from the server. The buffer size is 4096 bytes. The data received is in bytes format.
print(data) # Print the data received from the server. The data is in bytes format, so we print it as is.
