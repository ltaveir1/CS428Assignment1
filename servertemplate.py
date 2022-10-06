# import socket module
from socket import *

# In order to terminate the program
import sys

# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
### YOUR CODE HERE ###
serverSocket.bind(('192.168.0.230', 49666)) #not sure that I got my ip and socket properly but I think this is right
serverSocket.listen(1)

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

    connectionSocket, addr = f.read() ## YOUR CODE HERE ###

    try:
        '''
        #recv(): recieve a message from socket
        #socket.recv(bufsize[, flags]), For best match with hardware and network realities, 
        #the value of bufsize should be a relatively small power of 2, for example, 4096.
        Logan's note: stuff on the internet seemed to use 1024 as the number tho
        '''
        message = connectionSocket.recv(4096) ## YOUR CODE HERE ###  may want to change up this number not sure how important it is
        
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()### YOUR CODE HERE ###

        # Send one HTTP header line into socket
        ### YOUR CODE HERE ###
        # Format: "HTTP/1.1 *code-for-successful-request*\r\n\r\n"
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

        # Send the content of the requested file into socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Close client socket
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        ### YOUR CODE HERE ###
        # Same format as above, but with code for "Not Found"
        connectionSocket.send('HTTP/1.1 404 Not found\r\n\r\n')
        # Close client socket
        ### YOUR CODE HERE ###
        connectionSocket.close()

# Close server socket
serverSocket.close()

# Terminate the program after sending the corresponding data
sys.exit()

