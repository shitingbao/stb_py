#!/usr/bin/env python3
import threading


def out_name(name):
    for i in range(5):
        print(name, ":", i)


def thread_test():
    tone = threading.Thread(target=out_name("123"), name="123")
    tone.start()
    ttwo = threading.Thread(target=out_name("456"), name="456")
    ttwo.start()
