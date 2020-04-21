#!/usr/bin python

import os

for tmpdir in ('/tmp', r'C:\temp'):
    if os.path.isdir(tmpdir):
        break
    else:
        print('no temp directory available')
        tmpdir = r'C:\temp'

    if tmpdir:
        # enter the path
        os.chdir(tmpdir)
        # reture the current path
        cwd = os.getcwd()
        print('*** current temporary directory')
        print(cwd)

        print('*** creating example directory')
        # create a directory
        os.mkdir('example')
        # enter the directory
        os.chdir('example')
        # get the current path
        cwd = os.getcwd()
        print('*** new working directory')
        print(cwd)
        print('*** origin directory listing')
        #list all the files in the directory
        print(os.listdir(cwd))

        print('*** creating test file')
        fobj = open('test', 'w')
        fobj.write('foo\n')
        fobj.write('bar\n')
        fobj.close()
        print('***updated directory listing:')
        # list all the files in the directory
        print(os.listdir(cwd))

        print("*** renaming 'test' to 'filetest.txt'")
        # rename the file:test
        os.rename('test', 'filetest.txt')
        print("*** updated directory listing:")
        print(os.listdir(cwd))

        # combine the cwd(current directory) and the first file in it
        path = os.path.join(cwd, os.listdir(cwd)[0])
        print('*** full file pathname')
        print(path)
        print('*** (pathname, basename) == ')
        # split the path to file and directory
        print(os.path.split(path))
        print('*** (filename, extension) == ')
        # spilt the extend label from the path
        print(os.path.splitext(os.path.basename(path)))

        print('*** displaying file contents')
        # print the content of file
        fobj = open(path)
        for eachline in fobj:
            print(eachline)
        fobj.close()

        print('*** deleting test file')
        # delete  full path of the file
        os.remove(path)
        print('*** updated directory listing:')
        # list all the files in the directory
        print(os.listdir(cwd))
        # enter the parent directory
        os.chdir(os.pardir)
        print('*** deleting test directory')
        # delete the directory created
        os.rmdir('example')
        print('*** done')
