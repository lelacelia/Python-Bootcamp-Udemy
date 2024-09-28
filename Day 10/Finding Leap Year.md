# Build a program to find out which one is a LEAP year

### Instruction:
Write a program that returns True or False whether if a given year is a leap year.

A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice



This is how you work out whether if a particular year is a leap year. 

- on every year that is divisible by 4 with no remainder

- except every year that is evenly divisible by 100 with no remainder 

- unless the year is also divisible by 400 with no remainder   



e.g. The year 2000: 

2000 ÷ 4 = 500 (Leap)  
2000 ÷ 100 = 20 (Not Leap)  
2000 ÷ 400 = 5 (Leap!)  
So the year 2000 is a leap year. 



But the year 2100 is not a leap year because: 

2100 ÷ 4 = 525 (Leap)  
2100 ÷ 100 = 21 (Not Leap)  
2100 ÷ 400 = 5.25 (Not Leap)  
```p
def div_4(year_to_test):
    if year_to_test % 4 == 0:
        return "LEAP"
    else:
        return "NOT LEAP"

def div_100(year_to_test):
    if year_to_test % 100 == 0:
        if year_to_test % 100 % 2 == 0:
            return "NOT LEAP"
        else:
            return "LEAP"
    else:
        return "NOT LEAP"

def div_400(year_to_test):
    if year_to_test % 400 == 0:
        return "LEAP"
    else:
        return "NOT LEAP"



def is_leap_year(year):
    # Write your code here.
    test_result = {}
    
    test_result["test1"] = div_4(year)
    test_result["test2"] = div_100(year)
    test_result["test3"] = div_400(year)
    
    count_pass = 0
    
    for test in test_result:
        if test_result[test] == "LEAP":
            count_pass += 1
     
    if count_pass >= 2:
         return True
    else:
        return False
    # Don't change the function name.


is_leap_year(2020)
```
