'''
def Av(nums,k):
    st=0
    en=k
    av= float('-inf')
    
    while en<= len(nums):
        
        s = (sum(nums[st:en]))/k
        av = max(s,av)
        st+=1
        en+=1
    return av 
        
Arr=[-1]
k=1

print(Av(Arr,k))
'''
def Av(nums, k):
    if len(nums) < k or k <= 0:
        return None 
    
    current_sum = sum(nums[:k])
    max_average = current_sum / k

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_average = max(max_average, current_sum / k)

    return max_average

Arr = [1,2,34,5,6,4,3,4,2,9,6,4,2,3,5,5,5,5,5,3,4,34,3,1235 ,34,5345,345,34,534,5,345,34,534,5,35,34,5,345,34,5,34,5,43,534,34,5,34,5,345,345,34,5,34,3,45,34,5,34,543]
k = 44

result = Av(Arr, k)

if result is not None:
    formatted_result = "{:.2f}".format(result)
    print(formatted_result)
else:
    print("Invalid input")
