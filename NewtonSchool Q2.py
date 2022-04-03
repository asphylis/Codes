count_n = 0
count_t = 0
rounds = int(input())
if(rounds%2 == 0):
  print("Wrong Input")
  quit()
result = input()
for elements in range(0, rounds):
	if(result[elements] == "N"):
		count_n = count_n + 1
	else:
		count_t = count_t + 1
if(count_n > count_t):
	print("Nutan")
else:
	print("Tusla")
