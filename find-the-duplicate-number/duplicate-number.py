class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # UNDERSTAND
        # Given an array of nums, we must find the duplicate number

        # PLAN
        # Create a hashtable to keep track of number of occurences
        # of each number in the array

        # If a number has more than one occurence, then it is the duplicate
        # because the list will only have ONE duplicate

        # EXECUTE
        num_table = {}  # init a hashtable to keep track of number counts

        # iterate through list of nums and add to hashtable
        for num in nums:
            if num not in num_table:
                num_table[num] = 1
            else:
                num_table[num] += 1

        # iterate through our hashtable and find the value that has
        # more than one occurence
        for pair in num_table.items():
            if pair[1] > 1:
                return pair[0]
