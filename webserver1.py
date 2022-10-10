# import socket module
from socket import *

# In order to terminate the program
import sys

# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
### YOUR CODE HERE ###
#'10.127.147.133'
hostname = gethostname()
ip_address = gethostbyname(hostname)
port_number = 59670
serverSocket.bind((ip_address, port_number)) #not sure that I got my ip and socket properly but I think this is right
serverSocket.listen(1)
print(ip_address + ':' + str(port_number))

'''
Good resources for stuff
https://stackoverflow.com/questions/3840296/got-problems-about-a-simple-server-written-by-python
https://gist.github.com/skvisli/9724aff7807002b220b5
https://docs.python.org/3/library/socket.html
https://manpages.debian.org/bullseye/manpages-dev/recv.2.en.html
http://www.faqs.org/rfcs/rfc2616.html
'''
while True:
    # Establish the connection
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept() ## YOUR CODE HERE ###

    try:
        '''
        #recv(): recieve a message from socket
        #socket.recv(bufsize[, flags]), For best match with hardware and network realities, 
        #the value of bufsize should be a relatively small power of 2, for example, 4096.
        Logan's note: stuff on the internet seemed to use 1024 as the number tho
        '''
        message = connectionSocket.recv(1024) ## YOUR CODE HERE ###  may want to change up this number not sure how important it is
        if message:
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()### YOUR CODE HERE ###

            # Send one HTTP header line into socket
            ### YOUR CODE HERE ###
            # Format: "HTTP/1.1 *code-for-successful-request*\r\n\r\n"
            returnmes = 'HTTP/1.1 200 OK\r\n\r\n'.encode()
            connectionSocket.send(returnmes)

            # Send the content of the requested file into socket
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        else:
            #Avoid index error
            print("file not found")

        # Close client socket
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        ### YOUR CODE HERE ###
        # Same format as above, but with code for "Not Found"
        returnmes = 'HTTP/1.1 404 Not found \r\n\r\n'.encode()
        connectionSocket.send(returnmes)
        # Close client socket
        ### YOUR CODE HERE ###
        connectionSocket.close()

# Close server socket
serverSocket.close()

# Terminate the program after sending the corresponding data
sys.exit()

