class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        large = max(candies)
        outcome = []

        for i in candies:
            if i + extraCandies >= large:
                outcome.append(True)
            else:
                outcome.append(False)

        return outcome

def main():
    # Instantiate the Solution class
    solution = Solution()

    # Define the test case
    candies = [2,3,5,1,3]
    extraCandies = 3
    expected_output = [True, True, True, False, True] 

    # Call the kidsWithCandies method and get the result
    result = solution.kidsWithCandies(candies, extraCandies)

    # Verify the result
    if result == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed. Expected:", expected_output, "Got:", result)

if __name__ == "__main__":
    main()
