# To find longest palindrome substring
def longestPalSubstring(string):
    n=len(string)
    if(n<2):
        return n
    start = 0
    maxLength=1
    for i in range(n):
        low=i-1
        high=i+1
        while(high < n and string[high]==string[i]):
            high=high+1
        while(low>=0 and string[low]==string[i]):
            low =low-1
        while (low >= 0 and high<n and string[low] == string[i]):
            low = low - 1
            high=high+1
        length = high - low -1
        if(maxLength<length):
            maxLength=length
            start=low+1
    print("Longest palindrome substring is",end=" ")
    print(string[start:start+maxLength])
    return maxLength
# string=("forgeeksskeegfor")
string=input()
print("Length is"+str(longestPalSubstring(string)))