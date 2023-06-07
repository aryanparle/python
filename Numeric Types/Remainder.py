print('Remainder:')

a1=10
a2=3
mod1=a1%a2
print('mod: ',mod1)
#When both the integers are positive, the system rounds up away from 0
#For example, 3.33 will be rounded up to 4

b1=10
b2=-3
mod2=b1%b2
print('mod: ',mod2)

c1=-10
c2=3
mod3=c1%c2
print('mod: ',mod3)
#When one of the integers is negative, the system rounds up away from 0
#For example, 3.33 will be rounded up to 4

d1=-10
d2=-3
mod4=d1%d2
print('mod: ',mod4)
#When both the integers are negative, the system does not round up away from 0.
#For example, 0.68 will be rounded up to 0 or 2.65 will be rounded up to 2
print()

print('Examples:')

a1=14
a2=4
mod1=a1%a2
print('mod: ',mod1)

b1=14
b2=-4
mod2=b1%b2
print('mod: ',mod2)

c1=-14
c2=4
mod3=c1%c2
print('mod: ',mod3)

d1=-14
d2=-4
mod4=d1%d2
print('mod: ',mod4)

#When both the integers are positive, the system rounds up the value away from 0.
#For example, 2.44 will be rounded up to 3.

#When one of the integers is negative, the system rounds up the value away from 0.
#For example, 5.66 will be rounded up to 6

#When both the integers are negative, the system does not rounds up the value away from 0.
#For example, 3.7 will be rounded up to 3
