def find_it(seq):
    retorno = 0
    nums = {}
    for i in seq:
        if i in nums:
            nums[i] += 1
        else:
            nums[i] = 1
    for j in seq:
        if nums.get(j) % 2 == 1:
            retorno = j
    return retorno
