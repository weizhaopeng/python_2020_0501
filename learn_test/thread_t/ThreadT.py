from multiprocessing import Process
from threading import Thread
from os import getpid
from random import randint
from time import time, sleep

def downloadTask(filename):
    # Process.getpid获取当前的进程号
    print('启动下载进程，进程号：%d' % getpid())
    print('开始下载%s....' % filename)
    timeToDownload = randint(5, 10)
    sleep(timeToDownload)
    print('%s下载完成！耗时%d秒' %(filename, timeToDownload))

counter = 0

def subTask():
    global counter
    while counter < 10:
        print(counter, end='', flush=True)
        counter += 1
        sleep(0.01)

class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        # Process.getpid获取当前的进程号
        print('启动下载进程，进程号：%d' % getpid())
        print('开始下载%s....' % self.filename)
        timeToDownload = randint(5, 10)
        sleep(timeToDownload)
        print('%s下载完成！耗时%d秒' % (self.filename, timeToDownload))


def main():
    """
    startTime = time()
    # 创建进程，进程的执行单位是函数，传进去参数和函数名，注意参数后需要逗号
    process1 = Process(target=downloadTask, args=('python从入门到放弃', ))
    # start方法是使得进程运行起来，运行函数
    process1.start()

    process2 = Process(target=downloadTask, args=('《活着》', ))
    process2.start()

    # 线程连接也就是等待子进程执行结束才来到这里
    process1.join()
    process2.join()
    endTime = time()
    print('下载总共耗时：%d' %(endTime - startTime))
    """

    # Process(target=subTask).start()
    # Process(target=subTask).start()

    startTime = time()
    thread1 = Thread(target=downloadTask, args=('《python从入门到放弃》', ))
    thread1.start()

    thread2 = Thread(target=downloadTask, args=('《活法》', ))
    thread2.start()
    thread1.join()
    thread2.join()
    # 只有当join执行完，从子线程中回到主线程才进行下面的操作，不执行start就不开始

    thread3 = DownloadTask('《围城》')
    thread3.start()
    thread4 = DownloadTask('《我们仨》')
    thread4.start()
    thread3.join()
    thread4.join()
    endTime = time()
    print('下载总共耗时:%.3f秒' % (endTime - startTime))


if __name__ == '__main__':
    main()
