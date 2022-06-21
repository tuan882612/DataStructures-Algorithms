class search:
    def __init__(self):
        pass
    
    def binary_search(self, nums, find):
        left, right = 0, len(nums)-1
        
        while left<=right:
            mid = left + (right - left) // 2
            if nums[mid] == find:
                return True
            
            elif nums[mid] > find:
                right = mid - 1
                
            else:
                left = mid + 1
                
        return False

class sort:
    def __init__(self):
        pass

    def merge_sort(self, nums):
        if len(nums)>1:
            right, left = nums[:len(nums)//2], nums[len(nums)//2:]
            self.merge_sort(left)  
            self.merge_sort(right)
                
            i, j, k = 0, 0, 0
            while i<len(left) and j<len(right):
                if left[i] > right[j]:
                    nums[k] = right[j]
                    j+=1
                else:
                    nums[k] = left[i]
                    i+=1
                k+=1
            
            while i<len(left):
                nums[k] = left[i]
                i+=1
                k+=1
            
            while j<len(right):
                nums[k] = right[j]
                j+=1
                k+=1

    def insertion_sort(self, nums):
        for i in range(1,len(nums)):
            j = i-1
            find = nums[i]
            
            while j>-1 and nums[j] > find:
                nums[j+1] = nums[j]
                j -= 1
            
            nums[j+1] = find
        
if __name__ == "__main__":
    arr = [3,4,2,1]
    sort().insertion_sort(arr)
    print(search().binary_search(arr, 3))
