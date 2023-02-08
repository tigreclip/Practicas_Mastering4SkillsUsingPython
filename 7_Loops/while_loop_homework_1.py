""" 
Dado un número inicial  X y un número final Y, imprime todos los
números entre X e Y (inclusive) 
"""

start, end = map(int, input().split())

while start <= end:
    print(start)
    start += 1