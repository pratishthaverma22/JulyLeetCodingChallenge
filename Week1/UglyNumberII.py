/*
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  
1. 1 is typically treated as an ugly number.
2. n does not exceed 1690.
*/

class Solution:
    def nthUglyNumber(self, n):
        factors, k = [2,3,5], 3
        starts, Numbers = [0] * k, [1]
        for i in range(n-1):
            candidates = [factors[i]*Numbers[starts[i]] for i in range(k)]
            new_num = min(candidates)
            Numbers.append(new_num)
            starts = [starts[i] + (candidates[i] == new_num) for i in range(k)]
        return Numbers[-1]
