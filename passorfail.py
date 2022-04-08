'''
Pass or Fail program using map function
First line accepts total number of test cases
Second line acceps 3 values total no of questions, total answered correctly, passing marks
+3 for correct and -1 for wrong answer
'''
t = int(input())

for i in range(t):
    n, x, p = map(int, input().split(" "))
    positive = x*3
    negative = (n-x) * - 1
    total = positive + negative
    if(total >= p):
        print("PASS")
    else:
        print("FAIL")
