'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : 4.1_reverse.py
* 작성일 : 2021.10.06.Wed
* 프로그램 설명 : 사용자로부터 문자열을 입력 받아 이것을 역순으로 출력하는 프로그램을 
작성하라. 단 스택을 사용한다.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from stackclass import Stack

instr = input('문자열 입력: ')
s = Stack()

for ch in instr:
    s.push(ch)

print('역순 문자열: ')
while not s.isEmpty():
    print(s.pop())