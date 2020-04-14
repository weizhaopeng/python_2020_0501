from abc import abstractmethod, ABCMeta
from random import random

"""
角色：奥特曼，小怪兽
属性：奥特曼：名字，血量，魔法值，暴击率
     小怪兽：名字，血量，护甲，魔抗，暴击率
攻击：回合制
暴击：暴击造成的伤害双倍
物理攻击：攻击力-护甲*1.5，不能小于0
魔法攻击：攻击力-魔抗，不能小于0
"""


def main():
    """
    通过实例化两个角色，让他们进行战斗，通过循环得到结果
    :return:
    """
    pass


if __name__ == '__main__':
    main()


class Role(object, metaclass=ABCMeta):
    """定义角色具备名字, 攻击力和血量基础属性"""
    __slots__ = ('_name', '_hitPoint', '_attackPower', '_armor', '_magicResistance')

    def __init__(self, name, hitPoint, attackPower, armor, magicResistance):
        self._name = name
        self._hitPoint = hitPoint
        self._attackPower = attackPower
        self._armor = armor
        self._magicResistance = magicResistance

    @property
    def name(self):
        return self._name

    @property
    def hitPoint(self):
        return self._hitPoint

    @property
    def attackPower(self):
        return self._attackPower

    @property
    def armor(self):
        return self._armor

    @property
    def magicResistance(self):
        return self._magicResistance

    @name.setter
    def name(self, newName):
        self._name = newName

    @hitPoint.setter
    def hitPoint(self, newHitPoint):
        self._hitPoint = newHitPoint

    @attackPower.setter
    def attackPower(self, newAttackPower):
        self._attackPower = newAttackPower

    @armor.setter
    def armor(self, newArmor):
        self._armor = newArmor

    @magicResistance.setter
    def magicResistance(self, newMagicResistance):
        self._magicResistance = newMagicResistance

    @property
    def isAlive(self):
        return self._hitPoint > 0

    @abstractmethod
    def attack(self, enmey):
        pass


class Ultraman(Role):
    """
    奥特曼继承自角色
    包含属性：名称，血量，攻击力, 蓝量，暴击率
    """
    __slots__ = ('_name', '_hitPoint', '_attackPower', '_armor', '_magicResistance', '_magicPower', '_critRate')

    def __init__(self, name, hitPoint, attackPower, armor, magicResistance, magicPower, critRate):
        super().__init__(name, hitPoint, attackPower, armor, magicResistance)
        self._magicPower = magicPower
        self._critRate = critRate

    @property
    def magicPower(self):
        return self._magicPower

    @property
    def critRate(self):
        return self._critRate

    @magicPower.setter
    def magicPower(self, newMagicPower):
        self._magicPower = newMagicPower

    @critRate.setter
    def critRate(self, newCritRate):
        self._critRate = newCritRate

    def attack(self, enemy):
        """
        攻击的规则是：
        如果蓝量到达100，这次攻击启用魔法攻击，无视护甲，并且必定暴击
        奥特曼的每次攻击都有暴击率的概率会暴击
        :param enemy: 敌人
        :return: 无返回值
        """

        isCrit = False
        if 100 <= self._magicPower:
            damage = self._attackPower - enemy.magicResistance
        else:
            damage = self._attackPower - (enemy.armor * 1.5)
            self._magicPower += 30
        if self._critRate < random():
            damage *= 2
            isCrit = True
        enemy.hitPoint -= damage if damage > 0 else 0
        return damage, isCrit

    def __str__(self):
        return "%s奥特曼：\n" \
               "生命值：%d\n" \
               "攻击力：%d\n" \
               "魔法值：%d\n" \
               "护甲：%d\n" \
               "魔抗：%d\n" \
               "暴击率：%d\n" \
               % (self._name, self._hitPoint, self._attackPower, self._magicPower,
                  self._armor, self._magicResistance, self._critRate)


class Monster(Role):
    __slots__ = ('_name', '_hitPoint', 'attackPower', '_armor', '_magicResistance', '_critRate')

    def __init__(self, name, hitPoint, attackPower, armor, magicResistance, critRate):
        super().__init__(name, hitPoint, attackPower, armor, magicResistance)
        self._critRate = critRate

    @property
    def critRate(self):
        return self._critRate

    @critRate.setter
    def critRate(self, newCritRate):
        self._critRate = newCritRate

    def attack(self, enmey):
        isCrit = False
        damage = self._attackPower - enmey.armor * 1.5
        if random() < self._critRate:
            damage *= 2
            isCrit = True

        enmey.hitPoint -= damage if damage > 0 else 0
        return damage, isCrit

    def __str__(self):
        return "%s怪兽\n" \
               "生命值：%d\n" \
               "攻击力：%d\n" \
               "护甲：%d\n" \
               "魔抗：%d\n" \
               "暴击率：%d\n" \
               % (self._name, self._hitPoint, self._attackPower,
                  self._armor, self._magicResistance, self._critRate)
