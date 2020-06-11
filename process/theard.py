#!/usr/bin/env python3
import threading


def out_name(name):
    for i in range(5):
        print(name, ":", i)


def thread_test():
    # 这里要用元组，不然会将这个字符串的每一个字符都当成一个参数，引起参数个数不匹配的问题
    tone = threading.Thread(target=out_name, args=("123",))
    print("this first")
    ttwo = threading.Thread(target=out_name, args=("456",))

    ttwo.start()
    tone.start()


if __name__ == "__main__":
    thread_test()
