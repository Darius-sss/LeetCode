__time__ = '2021/8/9'
__author__ = 'ZhiYong Sun'
# 自我介绍
# 自己用过哪些数据结构
# 问了一些元组的问题
# -- 元组中的列表能否改数据，为什么？
# -- 列表中的元组能否改数据，为什么？

# 针对爬虫问了一些问题：
# -- 爬虫的基本流程
# -- 爬虫中遇到了什么样的问题
# -- 正则库有哪些函数
# -- 除了正则进行处理还可以用什么其他库
# -- 爬虫中request的函数，及其参数

# 测试方面的问题
# -- 你认为经过实习之后功能测试最重要的是什么
# -- 以及经历功能测试给你带来的指导性意见
# -- 测试百度界面

# 操作系统的问题
# -- python的多线程是真的还是假的，用Java呢
# -- 线程和进程之间的区别


# 网络方面的问题
# -- TCP 和 UDP 之间的区别
# -- 网络的五层和七层的架构



# 算法题快排
def quicksort(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    less = [i for i in nums[1:] if i <= pivot]
    greater = [i for i in nums[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


# 算法题延伸--原地数组实现(当时说的思路有问题，这是之后补的)
def partition(nums, p, r):
    x = nums[r]
    i = p - 1
    for j in range(p, r - 1):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1


def qsort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        qsort(nums, p, q-1)
        qsort(nums, q + 1, r)


if __name__ == '__main__':
    nums = [1, 5, 3, 3, 6, 7, 2]
    # print(quicksort(nums))

    # 原地快排
    qsort(nums, 0, len(nums) - 1)
    print(nums)


# 需要进一步学习相关的知识
# 网络方面需要学习
# 面试中说到的正则以及bf4以及request需要复习
# 常用的linux命令 grep！！！
# 线程和进程之间的关系，以及python的多线程问题

