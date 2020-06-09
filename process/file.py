#!/usr/bin/env python3
import os


def getFileInfo(file_path):
    with open(file_path, "w+") as f:  # open的第二个参数有w,r,a好几种类型，分别代表操作的类型，读写追加，以及是否创建文件等
        print(f.name)  # 文件名
        tx = f.read()  # 读取文件所有内容
        print(tx)
        f.seek(0)  # 重新移动游标，如果读取过一次文件内容，游标就会在文件末尾，如果再次读取就需要将游标移动到开始位置或者你想读取的位置
        tx = f.readline()  # 读取一行，因为上面已经调用过read，如果没有调用seek移动游标到起始位置，那这里读取的内容就是空
        print(tx)
        f.close()  # 关闭文件流
