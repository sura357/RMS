import socket
import os
import threading
from Packet import PACKET
from Func import FUNC



class SOCKET():
    def __init__(self,ip = "10.3.141.1"):
        self.ip = ip
        self.port = 8080
        self.connLimit = 100
        self.connNum = 0

        self.cilent = {}
        self.perRead = 10240*10240
        self.threadAccept = threading.Thread(target=self.serverAccept)
        self.func = FUNC()

    def startAccept(self):
        print("開始監聽")
        
        self.threadAccept.start()

    def serverAccept(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 要選擇通訊模式
            self.ip = socket.gethostbyname(socket.gethostname())  # 找 IP
            self.server.bind((self.ip, self.port))  # 正式建立連線

            self.server.listen(self.connLimit)  # 監聽幾個人
            print('建置完成,IP 是' + self.ip)
        except Exception as e:
            print("Error:" + str(e))
            return
        
        while self.connNum <= self.connLimit:
            conn, address = self.server.accept()
            threadRead = threading.Thread(target=self.socketRead, args=(self, conn))
            threadRead.start()
            self.connNum = self.connNum + 1
    
    def socketRead(self, none, conn):
        conStr = PACKET()
        conStr.ID = "1"
        conStr.CMD = "0"
        conStr.SCMD = "1"
        connect_string = conStr.Assemble()
        print(connect_string)
        conn.send(connect_string.encode())

        while True:
            # try:
            res = conn.recv(self.perRead)
            readPack = PACKET(res.decode('utf-8'))
            print("Get:"+res.decode('utf-8'))
            readPack.Disassemble()

            print(readPack.ID," ", readPack.CMD," ",readPack.SCMD)

            # Parse
            reJason = self.func.Switch[int(readPack.ID)][int(readPack.CMD)][int(readPack.SCMD)]([conn,readPack])
                
            # except Exception as e:
            #     print("Error:" + str(e))
            #     # print("斷線")
            #     return

if __name__ == '__main__':
    CI = SOCKET()
    CI.startAccept()

