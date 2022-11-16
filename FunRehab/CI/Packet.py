
#GR!011#0039?{"id":"F130929327","password":"123456"}@
class PACKET():
    def __init__(self, ALLpackets = None):
        self.ALLpackets = ALLpackets

        self.HEADER = "GR"
        self.ID = None
        self.CMD = None
        self.SCMD = None
        self.MSGL = None
        self.MSG = None

        self.dot = ["!", "#", "?", "@"]
        self.dotSpot = []

    def Disassemble(self):
        # for d in self.dot:
        #     self.dotSpot.append(self.ALLpackets.find(d))

        self.dotSpot.append(self.ALLpackets.find(self.dot[0]))
        self.dotSpot.append(self.ALLpackets.find(self.dot[1]))
        self.dotSpot.append(self.ALLpackets.find(self.dot[2]))
        self.dotSpot.append(self.ALLpackets.find(self.dot[3]))
        
        self.HEADER = self.ALLpackets[0:self.dotSpot[0]]
        self.ID = self.ALLpackets[self.dotSpot[0]+1:self.dotSpot[0]+2]
        self.CMD = self.ALLpackets[self.dotSpot[0]+2:self.dotSpot[0]+3]
        self.SCMD = self.ALLpackets[self.dotSpot[0]+3:self.dotSpot[0]+4]
        print("解完封包後-------------------")

        try:
            if int(self.CMD) > 0:
                self.MSGL = self.ALLpackets[self.dotSpot[1]+1:self.dotSpot[1]+5]
                self.MSG = str(self.ALLpackets[self.dotSpot[2]+1:self.dotSpot[2] + int(self.MSGL)+1])
        except:
            print("Disassemble:" + self.ALLpackets)
            
        # 驗證封包長度，使用"@":

    def Assemble(self):
        try:
            if self.MSG is not None:
                self.MSGL = str("%04d" % len(self.MSG))
                self.ALLpackets = self.HEADER + self.dot[0] + \
                    self.ID + self.CMD + self.SCMD + self.dot[1] + \
                    self.MSGL + self.dot[2] + \
                    self.MSG + self.dot[3]
            else:
                self.ALLpackets = self.HEADER + self.dot[0] + \
                    self.ID + self.CMD + self.SCMD + \
                    self.dot[1] + self.dot[2] + self.dot[3]

            return self.ALLpackets
        except Exception as e:
            print("Error:" + str(e))
            return "Error"

    def print(self):

        print(self.HEADER + self.dot[0] + \
                    self.ID + self.CMD + self.SCMD + self.dot[1] + \
                    self.MSGL + self.dot[2] + \
                    self.MSG + self.dot[3])