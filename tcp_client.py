import socket

target_host = "www.google.com" # Change as per your target
target_port = 80  # Change as per your target

#create a socket object in which AF_INET is for IPV4 Ip address and SOCK_STREAM is the request is TCP not UDP
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))    # Making connection to the host

request = 'GET / HTTP/1.1\r\nHost: google..com\r\n\r\n'  #Sends the GET request to the host and also Change as per your target
client.send(request.encode())          # sending the data into encoded way

response = client.recv(4096) # Capture the response from the side of the server which have 4096 bytes of data

print(response.decode()) # Give the response after decode it ...
