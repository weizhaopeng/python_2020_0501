import time
import tkinter
import tkinter.messagebox
from threading import Thread


def download():
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成')


def showAbout():
    tkinter.messagebox.showinfo('关于', '作者')


"""
def main():
    '''
    这样的结构是因为只有一个进程，一个线程，导致了拥塞在sleep中而无法执行showabout
    '''
    top = tkinter.Tk()
    top.title = '单线程'
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=showAbout)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()
    """


def main():
    """
    通过这样的情况可以通过开辟出一个新的线程来处理耗时间的任务，从而不会拥塞
    :return:
    """

    class DownloadTaskHander(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        DownloadTaskHander(daemon=True).start()

    def showAbout():
        tkinter.messagebox.showinfo('关于', '作者')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('400x300')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=showAbout)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()
