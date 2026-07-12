def analyze_complexity(nums):
    first_item=nums[0]
    print(f"first item : {first_item}")

    print("---Single Loop---")
    for item in nums:
        print(item)

    print("---Nested Loop---")
    for i in range(len(nums)):
        for j in range(len(nums)):
            print(f"Pair: {nums[i]},{nums[j]}")
    
analyze_complexity([10,20,30])