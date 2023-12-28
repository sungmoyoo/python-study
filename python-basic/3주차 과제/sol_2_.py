fuel = int(input("Input amount of fuel(L): ")) #주유한 연료의 양을 입력받기 
distance = int(input("Input drive distance(km): ")) #주행한 거리를 입력받기

fuel_economy = distance/fuel #연비 계산

print("Fuel economy:", fuel_economy,"km/L") #입력받은 값을 계산하여 출력
