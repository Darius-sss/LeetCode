__time__ = '2021/7/23'
__author__ = 'ZhiYong Sun'
__doc__ = '快速排序'


def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]  # 选择第一个元素作为基准值，也可以用一个随机的下标
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    l = [6, 5, 3, 3, 2, 1]
    l = [2,1,5,6,5,4]
    l = [2, 1, 5, 6, 5, 4]

    print(quicksort(l))
    # 稳定性：不稳定
    # 最优时间复杂度：O(nlogn)
    # 最坏时间复杂度：O(n^2)