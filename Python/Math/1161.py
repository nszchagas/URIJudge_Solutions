def fatorial(n):
    if n == 0:
      return 1;
    else: 
      return n*fatorial(n-1)


while True:
  try: 
    m, n = map(int, input().strip().split(' '))
    print(fatorial(n) + fatorial(m))
  except EOFError: 
    break
