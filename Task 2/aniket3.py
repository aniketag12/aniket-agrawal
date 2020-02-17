print("hello this is aniket")
print(2+5)
var = 10;
a = 5 ;
sum = a+var ;
print(sum)
def myname(a , b):
    return a+b;
print(myname(20,50))
aniket_agrawal = 10 ;
naman = 3 ;
print(aniket_agrawal + naman);
aniket = "sometimes" ;


new_string = "aniket is a good guy " ;
print(new_string + aniket);

a= 200 ;
b = 200;
if a<b :
 print("a is less than b ");
elif a>b :
 print("b is less than a ");
else :
    print("both are equal");

        
num = 8

while num <= 10:
    print(num)
    num += 1
i = 1 ;    
for i in range(1 ,20 ,i+1):
    print(i);

relatives = [ "naagi" , "chitru" , " naman" , "balaji" , 10 ,20]
print(relatives[2]);
relatives.append("new_list_object")
print(relatives);


dictionary_tk = {
  "name": "8",
  "nickname": "Tk",
  "nationality": "Brazilian"
}




print(5*6)
print("love" , 5 ,6 ,7)
print('LOVE', 30, 82.2, sep=",")
for i in "python":
    print(i)

for i in  "python" :
    print(i)
    
new_variable = "this is the number"
print(new_variable)
    
import functools
memoize = functools.lru_cache
print(memoize)

number = input()
print(type(number))
number = str(number)
print(type(number))
print(range(0,5))

print("i couldn't get the range function ")


print(isinstance(5 , int))
print(isinstance("girl" ,str))
print(isinstance(3.14 , int))
print(isinstance(3.14 , float))
print( 4 +3.14)
result = (3/2)
print(result)
print(isinstance(result , float))
print(36%2)
print( "to find the index of any character in string")

print("large".index("e"))

print( "s" in "metamorphic")
print("b" in "beautiful")
new_variable = "smallarena"
print(new_variable[6])
print("upper code can access individual character in string ")
print(new_variable[-2])


print("I love {programming} in {python}".format(programming="programming", python="Python"))

print("A string is considered to be true in Python if it is not an empty string. So, we get the following:")
print(bool(""))
print(bool("x"))


num = input()
if int(num)<25:
    print("number is less than 25")
else:
        print("nuumber is greater than 25")
        
def add_two_numbers( num1 ,num2):
    return num1 +num2
print(add_two_numbers(33 ,45))

def side_effects():
    print("hey i'm just gonna print this without any return statement")
print(side_effects())

companies = [ "google" , "coffeebeans " , "aws" , "quintype"]
companies.append("microsoft")
print(companies)
companies.insert(3,"gm motors")
print(companies)
print("last code helps to insert a particular element at particular position")
companies.extend(["scala" , "mercedes"])
print(companies)

print("Handling Exceptions with Try/Except/Finally");

# Errors and Exceptions in Python are handled with the Try: Except: Finally construct. You put the unsafe code in the try: block. You put the fall-back code in the Except: block. The final code is kept in the Finally: block.
try:
     print("in the try block")
     print(1/0)
     
except:
     print("In the except block")
finally:
    print("In the finally block")
      
  
