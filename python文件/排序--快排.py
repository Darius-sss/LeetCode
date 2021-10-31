__time__ = '2021/10/31'
__author__ = 'ZhiYong Sun'

# 算法题快排
def quicksort(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    less = [i for i in nums[1:] if i <= pivot]
    greater = [i for i in nums[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


# 算法题延伸--原地数组实现(当时说的思路有问题，这是之后补的)
def partition(nums, p, r):      # 输入数组，左指针，右指针
    x = nums[r]                 # 以右指针所指向的数字为主元
    i = p - 1                   # 以p-1为初始交换位置
    for j in range(p, r - 1):
        if nums[j] <= x:        # 如果当前点不比主元大， 则将需要交换的位置i + 1   将i, j 进行替换
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1] # 最后将主元和 i+1 的位置的点进行交换，将主元移动到i+1的位置，此时左边比主元小右边比主元大
    return i + 1

def qsort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        qsort(nums, p, q-1)
        qsort(nums, q + 1, r)


if __name__ == '__main__':
    nums = [1, 5, 3, 3, 6, 7, 2]
    print(quicksort(nums))

    # 原地快排
    qsort(nums, 0, len(nums) - 1)
    print(nums)
