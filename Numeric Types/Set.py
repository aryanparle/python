print('Set Theory')
print()

s1=set()
print('s1:',s1,type(s1),len(s1))
s2=set('abcde')
print('s2:',s2,type(s2),len(s2))
s3=set('dbfgh')
print('s3:',s3,type(s3),len(s3))
s4=set([1,2,3,4,5])
print('s4:',s4,len(s4))
s5=set([4,5,6,7,8])
print('s5:',s5,len(s5))
s6=set([x for x in range(21)])
print('s6:',s6,len(s6))
print()

print('Set Operations')
s7=set([1,2,3,4,5])
s8=set([4,5,6,7,8])
s9=set([7,8,9,10,11])
s10=set([10,11,12,13,14])

print('s7:',s7,'s8:',s8,'s9:',s9,'s10:',s10)
print()

print('Union: or')
a1=s7|s8
print('a1: s7|s8',a1,len(a1))
a2=s8|s9
print('a2: s8|s9',a2,len(a2))
a3=s9|s10
print('a3: s9|s10',a3,len(a3))
a4=s7|s10
print('a4: s7|s10',a4,len(a4))
a5=s8|s10
print('a5: s8|s10',a5,len(a5))
print()

print('Intersection: and')
b1=s7&s8
print('b1: s7&s8',b1,len(b1))
b2=s8&s9
print('b2: s8&s9',b2,len(b2))
b3=s9&s10
print('b3: s9&s10',b3,len(b3))
b4=s8&s10
print('b4: s8&s10',b4,len(b4))
b5=s7&s10
print('b5: s7&s10',b5,len(b5))
print()

print('Difference: subtraction')
c1=s7-s8
print('c1: s7-s8',c1,len(c1))
c2=s8-s7
print('c2: s8-s7',c2,len(c2))
c3=s8-s9
print('c3: s8-s9',c3,len(c3))
c4=s9-s8
print('c4: s9-s8',c4,len(c4))
c5=s9-s10
print('c5: s9-s10',c5,len(c5))
c6=s10-s9
print('c6: s10-s9',c6,len(c6))
print()

print('Symmetric Difference: xor')
d1=s7^s8
print('d1: s7^s8',d1,len(d1))
d2=s8^s9
print('d2: s8^s9',d2,len(d2))
d3=s9^s10
print('d3: s9^s10',d3,len(d3))
d4=s7^s10
print('d4: s7^s10',d4,len(d4))
print()

print('In Test')
e1=4 not in s7
print('e1:',e1)
e2=4 in s7
print('e2:',e2)
