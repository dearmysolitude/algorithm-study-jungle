# 피보나치

import sys
input = sys.stdin.readline

T = int(input().rstrip())

dp0 = [0] * 41
dp1 = [0] * 41
dp0[0] = 1 # n번째 피보나치 수열을 구할 때 발생하는 0의 갯수
dp0[1] = 0
dp0[2] = 1
dp1[0] = 0 # n번째 피보나치 수열을 구할 때 발생하는 1의 갯수
dp1[1] = 1
dp1[2] = 1
# 0반복수는: 1부터, 1반복수는 0부터 피보나치 순열로 규칙이 있다. 
def pibo(n):
    for i in range(3, n+1):
        dp0[i] = dp0[i-1]+dp0[i-2]
        dp1[i] = dp1[i-1]+dp1[i-2]
    print(dp0[n], dp1[n])
    

for _ in range(T):
    N = int(input().rstrip())
    pibo(N)