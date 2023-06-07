print('Logical Operators')
print()

a=10
b=8
c=12
d=11
e=13
f=9

print('a:',a,'b:',b,'c:',c,'d:',d,'e:',e,'f:',f)
print()
print('ADD')

a1=a>b and b<a
print('a1:',a1)

a2=d>e and f!=a
print('a2:',a2)

a3=a+b==d and f*e<b%d
print('a3:',a3)

a4=c*a%f//d!=b*d*a/d and e-d+e*a>a/f*c
print('a4:',a4)

a5=f%d//d+c-a<=f*d*a/d and d+a*f*c>=a//c*d%f
print('a5:',a5)

a6=a+b-c*d/e%f!=f%e/d*c-b+a and a-b-c*d/e%f!=f%e/d*c-b-a
print('a6:',a6)

a7=c+a-f/d>=b*d*a/d and e+d*e*a>=a/f*c+d
print('a7:',a7)

print()
print('OR')

b1=d<f or f>d
print('b1:',b1)

b2=a+b<=d*f or e*a<=d+f
print('b2:',b2)

b3=f%d*a/c!=b*e*f+c or a//b*c*e+f!=a*b//c%d
print('b3:',b3)

b4=a+b-c*d>=d+c-e*f or a/b*c-d<=d/c*e-f
print('b4:',b4)

b5=f%e/d*c-b+a<=f+e-d*c-b+a or f+e-d*c-b+a<=f%e/d*c-b+a
print('b5:',b5)

b6=a+b-c*d/e%f!=f%e/d*c-b+a or a-b-c*d/e%f!=f%e/d*c-b-a
print('b6:',b6)

b7=f+d+a+c>=b-e-f-c or a*b*c*e*f<=a/b/c/d
print('b7:',b7)

print()
print('NOT')

c1= not(a*b==b*a)
print('c1:',c1)

c2= not(d%f==e//c)
print('c2:',c2)

c3= not(a-e+c>b*d)
print('c3:',c3)

c4= not(d%f*c+a<=e*f*c//d)
print('c4:',c4)

c5= not(a+b+c-d-e>=a-b-c+d)
print('c5:',c5)

c6= not(a*b*c+d/e/f<=a/b/c+d*e*f)
print('c6:',c6)

c7= not(a*b*c-d/e/f>=a/b/c+d*e*f)
print('c7:',c7)


