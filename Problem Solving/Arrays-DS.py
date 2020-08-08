/*
Given an array, A , of N integers, print each element in reverse order as a single line of space-separated integers.

Constraints:
1 <= N <= 1000
1 <= Ai <= 10000
*/

def reverseArray(a):
    return a[::-1]
    
    OR
    
def reverseArray(a):
    return list(reversed(a))    
