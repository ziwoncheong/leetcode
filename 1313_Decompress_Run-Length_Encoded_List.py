class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:     
        output = []
        
        for i in range(len(nums)-1):
            #홀수인경우
            if i%2 == 0:
                freq, val = nums[i], nums[i+1]
                output.extend([val]*freq)
            #짝수인경우
            else:
                pass
            
        return output
