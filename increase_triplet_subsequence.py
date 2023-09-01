class Solution:
    def increasingTriplet(self, nums):
        n = len(nums)
        
        if n < 3:
            return False
        
        min_num = float('inf')
        second_min_num = float('inf')

        for num in nums:
            if num <= min_num:
                min_num = num
            elif num <= second_min_num:
                second_min_num = num
            else:
                return True

        return False

def main():
    # Instantiate the Solution class
    solution = Solution()

    # Define the test case
    nums = [1,2,3,4,5]
    expected_output = True

    # Call the increasingTriplet method and get the result
    result = solution.increasingTriplet(nums)

    # Verify the result
    if result == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed. Expected:", expected_output, "Got:", result)

if __name__ == "__main__":
    main()
