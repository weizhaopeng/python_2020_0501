from multiprocessing import Process, Queue
from time import time


# def main():
    # 通过单线程进行相加耗时25s
    # total = 0
    # numberList = [x for x in range(1, 100000001)]
    # start = time()
    # for number in numberList:
    #     total += number
    # print(total)
    # end = time()
    # print('execution time:%d' % (end - start))

def main1():
    processor = []
    numberList = [x for x in range(1, 100001)]
    resultQueue = Queue()
    index = 0
    for _ in range(2):
        p = Process(target=taskHandler, args=(numberList[index:index + 50000], resultQueue, ))
        index += 50000
        processor.append(p)
        p.start()
    start = time()
    for p in processor:
        p.join()

    total = 0
    while not resultQueue.empty():
        total += resultQueue.get()
    print(total)
    end = time()
    print('execution time:%d' % (start - end), 's', sep='')


def taskHandler(numberList, resultQueue):
    total = 0
    for number in numberList:
        total += number
    resultQueue.put(total)


if __name__ == '__main__':
    # main()
    main1()
