class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            else:
                if flowerbed[max(0, i-1)] == 0 and flowerbed[min(len(flowerbed) - 1, i+1)] == 0:
                    count += 1
                    flowerbed[i] = 1

        if n <= count:
            return True
        else:
            return False

def main():
    # Instantiate the Solution class
    solution = Solution()

    # Define the test case
    flowerbed = [1,0,0,0,1]
    n = 2
    expected_output = False 

    # Call the canPlaceFlowers method and get the result
    result = solution.canPlaceFlowers(flowerbed, n)

    # Verify the result
    if result == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed. Expected:", expected_output, "Got:", result)

if __name__ == "__main__":
    main()
