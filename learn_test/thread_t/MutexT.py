from time import time, sleep
from threading import Thread, Lock

# class Accout(object):
#     __slots__ = ('_balance')
#     def __init__(self):
#         self._balance = 0
#     # 存款
#     def deposit(self, money):
#         newBalance = self._balance + money
#         # 这个操作可以让在这之间加上的存款数额，无效
#         sleep(0.01)
#         self._balance = newBalance
#
#     # 该数值变成只读
#     @property
#     def balance(self):
#         return self._balance

class Accout(object):
    __slots__ = ('_balance', '_lock')
    def __init__(self):
        self._balance = 0
        self._lock = Lock()
    # 存款
    def deposit(self, money):
        self._lock.acquire()
        try:
            newBalance = self._balance + money
            # 这个操作可以让在这之间加上的存款数额，无效
            sleep(0.01)
            self._balance = newBalance
        finally:
            self._lock.release()

    # 该数值变成只读
    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def main():
    account = Accout()
    threads = []
    for thread in range(100):
        addMoneyThread = AddMoneyThread(account, 1)
        threads.append(addMoneyThread)
        addMoneyThread.start()

    for thread in threads:
        thread.join()

    print('100个人都向一个账户存了一块钱，当前账户余额：%d' % account.balance)


if __name__ == '__main__':
    main()
