#!/usr/bin/python --
#-*- mode: python; coding: utf-8 -*-
# file: typing_generator.py
#    Created:       <2019/06/03 13:35:32>
#    Last Modified: <2019/06/06 11:44:41>

# 下記にあるコードの動作確認テスト
# https://docs.python.org/ja/3/library/typing.html#typing.Generatorfrom typing import Generator

def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'

def infinite_stream(start: int) -> Generator[int, None, None]:
    while True:
        yield start
        start += 1

if __name__ == "__main__":
    print("test echo_round()")
    gen = echo_round()
    next(gen)
    print(gen.send(3.14))

    print("test infinite_stream()")
    gen = infinite_stream(10)
    for i in range(10):
        print(next(gen))
