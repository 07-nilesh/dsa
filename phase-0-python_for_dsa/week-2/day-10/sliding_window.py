def max_sum_fixed_window(arr,k):
    if len(arr)<k:
        return 0
    window_sum=sum(arr[:k])   #O(k)
    max_sum=window_sum
    for i in range(k,len(arr)):  #O(n-k)
        window_sum+=arr[i]-arr[i-k]
        max_sum=max(max_sum,window_sum)
    return max_sum
#space : O(1)
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sum_fixed_window(nums,k))
print(max_sum_fixed_window([5],k))