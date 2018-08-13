"""
1. get the hostname, port number
2. form the url based on the hostname and port number
3. wait for the client request
4. if the client sends any request, then need to accept that request and process the request and  send response back to the client
"""
import socket
port=8889
hostname=socket.gethostname()
s=socket.socket()    #by default it is tcp and ipv4 connections
#print s

s.bind((hostname, port))

s.listen(30)    # what is 30

#print s.accept()
client_socket, client_info = s.accept()
client_socket.send("hello firefox, how are you doing??")
s.close()