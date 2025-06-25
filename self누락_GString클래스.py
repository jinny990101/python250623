#전역변수
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #버그
        print(strName)
        print(self.strName)


d = DemoString()
d.set("First Message")
d.print()
