class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        index_list = []
        for i in range(len(s)):
            if s[i] in vowels:
                index_list.append(i)

        new_index_list = []
        while len(index_list) > 1:
            new_index_list.append((index_list.pop(0), index_list.pop(-1)))

        s = list(s)
        for i, j in new_index_list:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

        return "".join(s)

def main():
    # Instantiate the Solution class
    solution = Solution()

    # Define the test case
    s = "leetcode"
    expected_output = "leotcede"

    # Call the reverseVowels method and get the result
    result = solution.reverseVowels(s)

    # Verify the result
    if result == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed. Expected:", expected_output, "Got:", result)

if __name__ == "__main__":
    main()
