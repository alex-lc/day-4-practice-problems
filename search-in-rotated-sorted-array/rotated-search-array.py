class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # UNDERSTAND
        # Given a list of numbers, find the index of the passed in
        # target number.
        # If the number does not exist in the list, return -1

        # PLAN
        # Check if the target number exists in our list
        # If it does, return its index
        # If it doesn't, return -1

        # EXECUTE
        if target in nums:
            return nums.index(target)
        else:
            return -1
