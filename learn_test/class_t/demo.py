from learn_test.class_t.AoTeMan import Ultraman, Monster
from learn_test.class_t.Fighting import Fighting

def main():
    role1 = Ultraman("迪迦奥特曼", 10000, 100, 20, 20, 0, 0.2)
    role2 = Monster("加纳", 20000, 81, 40, 40, 0.05)

    arena = Fighting()
    winner = arena.duel(role1, role2)
    print("胜者是：%s" % winner)
    print(arena.battleProcess)


if __name__ == "__main__":
    main()
