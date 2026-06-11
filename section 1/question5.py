class AccountLockedError(Exception):
    pass
class Loginsystem:
    def __init__(self):
        self.__password = "python@123"
        self.__attempts = 3
    def login(self, passsword):
        try:
            if passsword == self.__password:
                print("Login successful!")
            else:
                self.__attempts -= 1
                print("wrong password!")
                print("Remaining attempts",self.__attempts)
            if self.__attempts == 0:
                raise AccountLockedError("Account Locked!")
        except AccountLockedError as e:
            print(e)
        finally:
            print("Login process completed.")
obj = Loginsystem()
obj.login("abc")
obj.login("123")
obj.login("xyz")                               

                