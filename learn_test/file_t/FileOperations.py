
class FileOperations(object):

    def openFile(self, filename):
        try:
            demoFile = open(filename, "r", encoding="utf-8")
        except FileNotFoundError:
            print("找不到文件")
        except LookupError:
            print("未知的编码方式")
        except UnicodeDecodeError:
            print("文件解码出错")
        finally:
            demoFile.close()

        with open(filename, 'a+', encoding='utf-8') as demoFile:
            for line in demoFile:
                print(line)

    def readFile(self, filePoint):
        for line in filePoint:
            print(line)
        """
        print(filePoint.readline())
        """



