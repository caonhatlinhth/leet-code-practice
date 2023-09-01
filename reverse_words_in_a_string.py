class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        word_list.reverse()
        output = " ".join(word_list)
        return output

def main():
    # Instantiate the Solution class
    solution = Solution()

    # Define the test case
    s = "a good  example"
    expected_output = "example good a"

    # Call the reverseWords method and get the result
    result = solution.reverseWords(s)

    # Verify the result
    if result == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed. Expected:", expected_output, "Got:", result)

if __name__ == "__main__":
    main()
