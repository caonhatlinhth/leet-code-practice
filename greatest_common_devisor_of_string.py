class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return str1[:gcd(len(str1), len(str2))]

def main():
    # Instantiate the Solution class
    solution = Solution()

    # Define the test case
    str1 = "ABCABC"
    str2 = "ABC"
    expected_output = "ABC"

    # Call the gcdOfStrings method and get the result
    result = solution.gcdOfStrings(str1, str2)

    # Verify the result
    if result == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed. Expected:", expected_output, "Got:", result)

if __name__ == "__main__":
    main()