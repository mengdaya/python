# if嵌套
#如果满足一个条件 则输出tv，如果两个条件都不满足，则输出normal
# today1="holiday"
# bank_balance=20001
# if today1 == "holiday1":
#     if bank_balance == 20000:
#         print ("go to shopping")
#     else:
#         print ("Watch TV")
# else:
#     print ("normal working day")
#
today="holiday"
bank_balance=20001
if today == "holiday":
    if bank_balance == 2001:
        print ("hello world")
    else:
        print ("normal day")
else:
    print ("It's a nice day")
# today2="holiday"
# bank_balance2=20000
# if today2 == "holiday":
#         if bank_balance2>=20000:
#             print("go to swiming")
#         else:
#             print ("watch tv")
#         else:,
#         print ("xixishuiba")

# def sum(start,end):
#     result = 0
#     for i in range(start, end + 1):
#         result += i
#         print(result)
# print (sum(1, 10))


def sum(start,end):
    result=0
    for i in range(start,end+1):
        result += i
    print(result)
print (sum(1,10))





def sumreturn (start,end):
    result: int = 0
    for i in range(start,end+1):
        result +=i
        return result
a= sumreturn(1,5)
print (a)
