class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=-1
        l,r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            print(mid)
            if nums[mid] == target:
                ans = mid
                return ans
            elif nums[mid] < target:
                l = mid+1
                print('right', nums[mid])
            else:
                r = mid-1
                print('left', nums[mid])
        return ans
        