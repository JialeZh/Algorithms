def sortArrayByParity(nums):
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    final = even + odd
    return final
sortArrayByParity([1,2,3,4])