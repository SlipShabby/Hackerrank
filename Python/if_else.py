''''
Task 
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format
A single line containing a positive integer, .
Constraints

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.

'''
n = int(input().strip())
print ("Not Weird" if not n%2 and (n in range(2,6) or n>20) else "Weird")