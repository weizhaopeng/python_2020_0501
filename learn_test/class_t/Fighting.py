class Fighting(object):
    """
    定义一个战斗类，战斗的双方都是从这里进行战斗，
    战斗的角色都必须实现attack这个方法，同时双方都要有必要的属性
    """
    __slots__ = "_battleProcess"

    def __init__(self):
        self._battleProcess = None

    @property
    def battleProcess(self):
        return self._battleProcess

    @battleProcess.setter
    def battleProcess(self, damageList):
        self._battleProcess = damageList

    def duel(self, role1, role2):
        damageList = []
        winner = None
        while True:
            damageList.append(role1.attack(role2))
            if not role2.isAlive:
                winner = role1
                break
            damageList.append(role2.attack(role1))
            if not role1.isAlive:
                winner = role2
                break
        self._battleProcess = damageList
        return winner.name

    @staticmethod
    def showBothRoles(role1, role2):
        print("战士1：\n")
        print(role1)
        print("战士2：\n")
        print(role2)
