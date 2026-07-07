class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort() # sort the list of nums
        freq_count = []

        left, right = 0, 1
        subcount = 1
        while right < len(nums):
            print(nums[left], nums[right], right)
            if nums[left] != nums[right]:
                freq_count.append((nums[left], subcount))
                left = right
                right += 1
                subcount = 1
            else:
                subcount += 1
                right += 1
        
        freq_count.append((nums[left], subcount))
        freq_count.sort(key=lambda x: x[1], reverse=True)
        print(freq_count)
        return [count[0] for count in freq_count[:k]]
            