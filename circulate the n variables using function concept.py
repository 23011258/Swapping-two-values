Program to circulate N values.
#Developed by: 
#RegisterNumber:
def circulate():
    list1=eval(input())
    n=int(input())
    result=list1[n:]+list1[:n]
    print("After circulating the values are:",result)