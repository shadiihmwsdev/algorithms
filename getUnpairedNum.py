from collections import Counter
def solution(A):

    nums = A
    if len(A) == 0:
        return []
    
    ### slow solution

    # print(nums.count(9))
    # for n in nums:
    #     if(nums.count(n) == 1 or nums.count(n) > 1 and nums.count(n)  % 2 != 0):
    #         return n

    ### fastest solution
    d = dict(Counter(nums))
    baseLi = [num_count for num_count in list(d.values()) if num_count % 2 != 0]
    return list(d.keys())[list(d.values()).index(baseLi[0])]
    
print(solution([9,3,9,3,9,7,9]))