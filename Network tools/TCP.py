import socket 

target_host = "www.google.com"
target_port = 80

# creating a client object 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connecting client to host 
client.connect((target_host,target_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()


#this program is basically a simpler version of how the internal works when we write www.google.com in the browser. It creates a TCP connection to the server and sends a GET request to retrieve the homepage of Google. The response from the server is then printed to the console.   

