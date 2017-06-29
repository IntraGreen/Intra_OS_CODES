import socket
import threading
import argparse

def serveClient(clientToServeSocket,clientIPAddress,portNumber):
    clientRequest = clientToServeSocket.recv(4096)
    print "[!] Received data from the client (%s:%d):%s" % (clientIPAddress,portNumber,clientRequest)

    #reply back to client with a response
    clientToServeSocket.send("I am a server response, my version is 3.2")
    # We're done close the client socket
    clientToServeSocket.close()

def startServer(portNumber):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("0.0.0.0",portNumber))
    server.listen(10)
    print "[!] Listening locally on port %d ..." % portNumber

    while True:
        client,address = server.accept()
        print "[+] Connected with the client: %s:%d" % (address[0],address[1])

        #Handle clients through multi-threading
        serveClientThread = threading.Thread(target=serveClient,args=(client,address[0],address[1]))
        serveClientThread.start()

def main():
     # Parse the command line arguments
    parser = argparse.ArgumentParser('TCP server')
    parser.add_argument("-p","--port", type=int, help="The port number to connect with", default=4444)
    args = parser.parse_args()

    # Store the argument value
    portNumber = args.port
    
    #Call the start server function
    startServer(portNumber)

if __name__ == "__main__":
    main()