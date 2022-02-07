# Time:  O(n)
# Space: O(c), c is the max of nums

# counting sort, inplace solution
class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def inplace_counting_sort(nums, left, right, reverse=False):  # Time: O(n)
            if right-left+1 == 0:
                return
            count = [0]*(max(nums[i] for i in xrange(left, right+1))+1)
            for i in xrange(left, right+1):
                count[nums[i]] += 1
            for i in xrange(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(xrange(left, right+1)):  # inplace but unstable sort
                if nums[i] < 0:  # processed
                    continue
                while i != left+count[nums[i]]-1:
                    count[nums[i]] -= 1
                    nums[left+count[nums[i]]], nums[i] = ~nums[i], nums[left+count[nums[i]]]
                count[nums[i]] -= 1
                nums[i] = ~nums[i]
            for i in xrange(left, right+1):
                nums[i] = ~nums[i]  # restore values
            if reverse:  # unstable
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
    
        def partition(index, nums):
            for i in xrange(len(nums)):
                j = index(i)
                while nums[i] > 0:
                    nums[i], nums[j] = nums[j], ~nums[i]  # processed
                    j = index(j)
            for i in xrange(len(nums)):
                nums[i] = ~nums[i]  # restore values
        
        def index(i):
            return i//2 if i%2 == 0 else (len(nums)+1)//2+i//2

        def inverse_index(i):
            return 2*i if i < (len(nums)+1)//2 else 1+2*(i-(len(nums)+1)//2)

        partition(index, nums)
        inplace_counting_sort(nums, 0, (len(nums)+1)//2-1)
        inplace_counting_sort(nums, (len(nums)+1)//2, len(nums)-1, True)
        partition(inverse_index, nums)
        return nums


# Time:  O(nlogn)
# Space: O(n)
# sort, inplace solution
class Solution2(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def partition(index, nums):
            for i in xrange(len(nums)):
                j = index(i)
                while nums[i] > 0:
                    nums[i], nums[j] = nums[j], ~nums[i]  # processed
                    j = index(j)
            for i in xrange(len(nums)):
                nums[i] = ~nums[i]  # restore values
        
        def index(i):
            return i//2 if i%2 == 0 else (len(nums)+1)//2+i//2

        def inverse_index(i):
            return 2*i if i < (len(nums)+1)//2 else 1+2*(i-(len(nums)+1)//2)

        partition(index, nums)
        nums[:(len(nums)+1)//2], nums[(len(nums)+1)//2:] = sorted(nums[:(len(nums)+1)//2]), sorted(nums[(len(nums)+1)//2:], reverse=True)
        partition(inverse_index, nums)
        return nums


# Time:  O(nlogn)
# Space: O(n)
# sort
class Solution3(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums[::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2], reverse=True)
        return nums