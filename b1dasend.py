import  socket
ip="172.16.40.172"
port=9999
gtshttp=(ip,port)

#  lets create udp socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=input("enter message : ") 
newmsg=msg.encode('ascii')
#  now you can send
s.sendto(newmsg,gtshttp)
