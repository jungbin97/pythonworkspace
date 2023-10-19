class Solution:
    def threeSum(self, nums):
        nums.sort()
        answer = set()

        if len(nums) < 3:
            return answer
        
        for i in range(len(nums)):
            # 양수가되면 종료
            if nums[i]>0:
                break
            
            start, end = i+1, len(nums)-1

            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s>0:
                    # 0보다 크게 되면 숫자 크기를 줄여야함.
                    end -= 1
                elif s<0:
                    # 0보다 작으면 숫자 크기 늘려야함.
                    start += 1
                else:
                    answer.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1

        return [list(i) for i in answer]


print(Solution().threeSum([-1,0,1,2,-1,-4]))