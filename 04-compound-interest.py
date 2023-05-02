
"""
The formula to calculate compound interest annually is given by: 
A = P(1 + R/100) t 
A is amount 
P is the principal amount 
R is the rate and 
T is the time span
"""

"""
Input: Principal (amount): 1200, Time: 2, Rate: 5.4
Output: Compound Interest = 133.099243
"""

amount = 1200
time  = 2
rate = 5.4

result = amount*(1+(rate/100))**time  
print(result)