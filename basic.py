#write a program to swap two numbers using circumflex
a=1
b=2
a=a^b
b=a^b
a=b^a
print(a)
print(b)


#swap two numbers using conditional swap by logical AND/OR
a=1
b=2
temp=a
a=(a|b)&b
b=(temp|b)&temp
print(a,b)


#swap using dictionaries
v={'anu':11,'manu':15}
v['anu'],v['manu']=v['manu'],v['anu']
print(v)


#using  iter tool for swaping
gen=iter([1,2,3])
lst=list(gen)
lst[0],lst[1]=lst[1],lst[0]
print(lst)


#write a program to print the squares of n numbers in a list using  single line list comprehension
print([i*i for i in range(1,11) if i%2!=0])


#strong number
num=int(input("enter the number"))
copy=num
sum=0
while num>0:
    digit=num%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    num//=10
if sum==copy:
    print(copy,"is a strong number")
else:
    print(copy,"is not a strong number")



#happy number
num=int(input("enter a number"))
visit=set()
while num!=1 and num not in visit:
    visit.add(num)
    sum=0
    temp=num
    while temp>0:
        d=temp%10
        sum+=d**2
        temp//=10
    num=sum
if num==1:
    print("happy")
else:
    print("not")




#nivens number
n=int(input("enter the number"))
sum=0
while(n>0):
    rem=n%10
    sum+=rem
    n//=10
if n%sum==0:
    print("nivens number")
else:
    print("not")
        
