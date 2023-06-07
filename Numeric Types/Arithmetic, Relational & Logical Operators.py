print()
a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9

print('a:',a,'b:',b,'c:',c,'d:',d,'e:',e,'f:',f,'g:',g,'h:',h,'i:',i)
print()

print('AND:')
print()
a1=a+b>b+c and c+d<d+e
print('a1:',a1)

a2=i-h!=i-h and d+f>e+b 
print('a2:',a2)

a3=f*c<e*i and g*h>d*d
print('a3:',a3)

a4=i/c<=g/b and f/b>=h/d
print('a4:',a4)
print()

print('OR:')
print()
a5=c+d>d+e or a+b<b+c
print('a5:',a5)

a6=d+f<e+b or i-h==i-h
print('a6:',a6)

a7=g*h<d*d or f*c>e*i
print('a7:',a7)

a8=f/b<=h/d or i/c>=g/b
print('a8:',a8)
print()

print('AND & OR with 3 operend:')
print()
a9=f+d!=f+d and i-e<h-i or i-b>f-d
print('a9:',a9)

a10=i-b<h-d or g-a>f-b and a+b!=c+d
print('a10:',a10)

a11=i-b<f-d or f+d==f+d and i-e>h-i
print('a11:',a11)

a12=a+b==c+d and i-b>h-d or g-a<f-b
print('a12:',a12)

a13=b*c>i/e and d*f>=h*b or h/d!=d/h
print('a13:',a13)

a14=a+b>b+c and c-d>d-e and e*f>f*g
print('a14:',a14)

a15=a+b<b+c or c-d>d-e or e*f<f*g
print('a15:',a15)
print()

print('AND,OR & NOT with 4 operend:')
print()
a16=a+b>b+c and c-d>d-e or e*f<f*g and g/h>h/i
print('a16:',a16)

a17=i-b<h-d or g-a>f-b or a+b!=c+d and f-i>g-i
print('a17:',a17)

a18=not(i-f!=g+d) or f+d!=f+d and i-e<h-i and i-b>f-d and i/f<=h/d 
print('a18:',a18)

a19=not(i/c>=i/c) and e/b<g/d or f*c!=c*f or g+i<i+h
print('a19:',a19)

a20=not(i-a<=h*d) or d/b==i*f or g+d>b+c or i/g<i/h
print('a20:',a20)







