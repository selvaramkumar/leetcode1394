import collections
class Solution:
    def findLucky(self, arr) -> int:
        counter=collections.Counter(arr)
        temp=[]
        for k,v in counter.items():
            if k==v:
                temp.append(k)       
        if len(temp)!=0:        
            return max(temp)       
        else:
            return -1

s=Solution()
arr=[2,2,3,4]
print(s.findLucky(arr))                