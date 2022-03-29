# -*- coding: utf-8 -*-
n = int(input())
dentro = 0
for i in range(n):
    if int(input()) in range(10, 21):
        dentro += 1
print(f"{dentro} in")
print(f"{n-dentro} out")
