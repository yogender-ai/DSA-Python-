class Binary:
    def binary_search(self,arr,target):
        l=0
        r=len(arr)-1
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]==target:
                return mid
            elif target>arr[mid]:
                l=mid+1
            else:
                r=mid-1

arr=[2,3,4,5,6,7,8]
target=3
B=Binary()
ans=B.binary_search(arr,target)
print(ans)
