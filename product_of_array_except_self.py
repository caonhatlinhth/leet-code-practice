class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n
        left_products = [1] * n
        right_products = [1] * n

        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n -1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        for i in range(n):
            output[i] = left_products[i] * right_products[i]

        return output

def main():
    # Instantiate the Solution class
    solution = Solution()

    # Define the test case
    nums = [1,2,3,4]
    expected_output = [24,12,8,6]

    # Call the productExceptSelf method and get the result
    result = solution.productExceptSelf(nums)

    # Verify the result
    if result == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed. Expected:", expected_output, "Got:", result)

if __name__ == "__main__":
    main()
