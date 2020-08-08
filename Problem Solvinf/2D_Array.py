/*
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Function Description
Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.
hourglassSum has the following parameter(s):
arr: an array of integers

Input Format
Each of the 6 lines of inputs arr[i] contains 6 space-separated integers arr[i][j].

Constraints
-9 <= arr[i][j] <= 9
0 <= i,j <= 5

Output Format
Print the largest (maximum) hourglass sum found in arr.
*/

def hourglassSum(arr):
    maxSum = -63
    
    for i in range(4):
        for j in range(4):
        
            top = sum(arr[i][j:j+3])
            
            mid = arr[i+1][j+1]
            
            bottom = sum(arr[i+2][j:j+3])
            
            hourglass = top + mid + bottom
            
            if hourglass > maxSum:
                maxSum = hourglass
                
    return maxSum
