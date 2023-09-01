class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_word = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            new_word.append(word1[i])
            new_word.append(word2[j])
            i += 1
            j += 1

        while i < len(word1):
            new_word.append(word1[i])
            i += 1
        
        while j < len(word2):
            new_word.append(word2[j])
            j += 1
        
        return ''.join(new_word)

def main():
    # Instantiate the Solution class
    solution = Solution()

    # Define the test case
    word1 = "abc"
    word2 = "pqr"
    expected_output = "apbqcr"

    # Call the mergeAlternately method and get the result
    result = solution.mergeAlternately(word1, word2)

    # Verify the result
    if result == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed. Expected:", expected_output, "Got:", result)

if __name__ == "__main__":
    main()
