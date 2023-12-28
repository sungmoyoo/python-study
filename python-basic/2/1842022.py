#자동판매기 시뮬레이션 
cash =  int(input("투입한 돈 :"))
price = int(input("물건 값 :"))
remainder = cash-price
coin500 = remainder//500
coin100 = (remainder%500)//100

print("투입한 돈 :", cash)
print("거스름 돈 :", remainder)
print("500원 동전의 개수 :",coin500)
print("100원 동전의 개수 :",coin100)
