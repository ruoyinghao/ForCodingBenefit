#a simple socket server in python


#serving side
if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    sock.bind(('localhost',8010))
    
    #only 1 user is allowed a time  
    sock.listen(1)
    
    while(True):
        connection,address = sock.accept()
        try:
            connection.seetimeout(1)
            
            buf = connection.recv(1024)
            if buf =='1':
                connection.send('welcome to server!')
            else:
                connection.send('opps, something happened')
        except socket.timeout:
            print('time out')
        connection.close()
