# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #추가
        #이름숨김: __변수명
        self.__id = id
        self.__name = name
        self.__balance = balance

        # self.id = id
        # self.name = name 
        # self.balance = balance 
    def deposit(self, amount):
        # self.balance += amount 
        self.__balance += amount
    def withdraw(self, amount):
        #self.balance -= amount
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(500)
account1.withdraw(3000)
#account1.balance = 15000000
print(account1)

#외부에서 접근
print(account1.__balance)
