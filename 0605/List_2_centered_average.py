# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
  
  len_new = len(nums)-2
  
  min_n = nums[0]
  max_n = nums [0]
  
  for n in nums:
    min_n = min(min_n , n)
    
  for n in nums:
    max_n = max(max_n , n)
  
  return ( (sum(nums) - min_n - max_n) / len_new ) 