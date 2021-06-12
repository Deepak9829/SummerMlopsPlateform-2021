import socket 
import time
import threading

deepak_recv_s=socket.socket()
deepak_recv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1) #this is done so that we can reuse a port, otherwise everytime we have 
#to kill service because till some time port is remains active

digamber_recv_s=socket.socket()
digamber_recv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

deepak_send_s=socket.socket()
deepak_send_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

digamber_send_s=socket.socket()
digamber_send_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

deepak_recv_port=2024 #recive from Aman Dev Verma
digamber_recv_port=2025 #recive from Manasvi Agarwal
deepak_send_port=2026 #send to Aman Dev Verma
digamber_send_port=2027 #send to Manasvi Agarwal
ip=13.126.138.162
deepak_recv_s.bind((ip, k_recv_port))
digamber_recv_s.bind((ip, s_recv_port))
deepak_send_s.bind((ip, k_send_port))
digamber_send_s.bind((ip, s_send_port))

deepak_recv_s.listen()
digamber_recv_s.listen()
deepak_send_s.listen()
digamber_send_s.listen()

deepak_recv_session, k_recv_addr = k_recv_s.accept()
digamber_recv_session, s_recv_addr = s_recv_s.accept()
deepak_send_session, k_send_addr = k_send_s.accept()
digamber_send_session, s_send_addr = s_send_s.accept()

#above we have created total 4 socket 1) it will recive image in bytes from person2
#2)it will send those bytes recived by person2 to the person1
#3)it will recive image in bytes from person1
#2)it will send those bytes recived by person1 to the person2
def k_recv() #it will recive from digamber and send to Manasvi
    while True
        data=k_recv_session.recv(10000000)
        time.sleep(2)
        s_send_session.send(data)

def s_recv() #it will recive from deepak and send to Aman
    while True
        data=s_recv_session.recv(10000000)
        time.sleep(2)
        k_send_session.send(data)
#used threading so that above both function will run parellely
a1_recv=threading.Thread(target=k_recv)
m1_recv=threading.Thread(target=s_recv)
a1_recv.start()
m1_recv.start()
