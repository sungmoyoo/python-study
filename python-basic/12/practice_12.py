#파일 읽기
'''
infile = open("phones.txt","r",encoding="utf-8")

#read() 
lines = infile.read()
print(lines)

#readlines()
lines = infile.readlines()
print(lines)


#한줄씩 읽기(for문)
for line in infile:
    line = line.rstrip()
    print(line)


#한줄씩 읽기(while문)
line = infile.readline().rstrip()
while line != "":
    print(line)
    line = infile.readline().rstrip()

infile.close()
'''

#파일 쓰기
'''
outfile = open("phones1.txt","w")

outfile.write("Hong 010-1234-5678\n")
outfile.write("Kim1 010-1234-5679\n")
outfile.write("Kim2 010-1234-5680\n")

outfile.close()
'''

#파일 추가
'''
outfile = open("phones1.txt","a")

outfile.write("Kang 010-1234-5681\n")
outfile.write("Kim3 010-1234-5682\n")
outfile.write("Jeong 010-1234-5683\n")

outfile.close()
'''

#단어 읽기(split())
'''
f = open("proverbs.txt","r")
for line in f:
    line = line.rstrip()
    line = line.rstrip(".")
    word_list = line.split()
    for word in word_list:
        print(word);

f.close()
'''

#파일 복사
'''
infilename = input("input file name: ")
outfilename = input("output file name: ")

infile = open(infilename, "r",encoding="utf-8")
outfile = open(outfilename, "w",encoding="utf-8")

line = infile.read()
outfile.write(line)

infile.close()
outfile.close()
'''

#디렉토리 안의 파일 처리
'''
import os
arr = os.listdir()

for f in arr:
    if ".txt" in f or ".py" in f:
        infile = open(f,"r",encoding="utf-8")
        for line in infile:
            e = line.rstrip()
            if "python" in e:
                print(f,":",e)
        infile.close()
'''

#csv 파일 처리
#csv모듈
'''
import csv

f = open('weather1.csv')
data = csv.reader(f)
header = next(data)

temp = 100
for row in data:
    if row[3] == None:
        row[3] = 0
    elif temp > float(row[3]):
        temp = float(row[3])
        
print("Lowest temperatute between 2022.05.24~2023.05.24: %.2f" %(temp))

f.close()
'''

'''
#일반적인 방법
with open("weather.csv","r") as data:
    for line in data:
        e = line.strip().split(',')
        print(e)
'''

#행맨
from tkinter import *
from tkinter.filedialog import askopenfilename
import random

#초기 값 설정(추측값, 기회)
guesses = ''
turns = 10

#파일 읽고 임의의 단어 선택
#infile = open('words.txt','r')
readFile = askopenfilename()
if(readFile != None):
    infile = open(readFile,'r')
    
lines = infile.readlines()
word = random.choice(lines).rstrip() 

#행맨 메인

while turns > 0:
    failed = 0
    
    for char in word: 
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed += 1
    if failed == 0: 
        print("")
        print("User Win")
        break
    print("")
    
    guess = input("guess alphabet: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong alphabet")
        print(str(turns)+'turns left')
        if turns == 0:
            print('User Lose, Answer is ' +word)
























