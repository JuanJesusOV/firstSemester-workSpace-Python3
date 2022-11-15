print('V')
V=float(input())
print()

print('n')
n=float(input())
print()

print('T')
T=float(input())
print()

print('a')
a=float(input())
print()

print('b')
b=float(input())
print()

R=0.08206
Pi=(n*R*T)/V
Pr=((n*R*T)/(V-(n*b)))-((a*(n**2))/(V**2))
8
print('Pi: '+str(Pi))
print('Pr: '+str(Pr))
print()
print('Dif: '+ str(Pi-Pr))