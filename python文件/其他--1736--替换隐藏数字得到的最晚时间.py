__time__ = '2021/7/24'
__author__ = 'ZhiYong Sun'

"""
给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。

有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。

替换time 中隐藏的数字，返回你可以得到的最晚有效时间。

"""


class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)

        if time[0] == '?':
            if time[1] == '?':
                time[0], time[1] = '2', '3'
            elif '0' <= time[1] <= '3':
                time[0] = '2'
            else:
                time[0] = '1'

        if time[1] == '?':
            if time[0] != '2':
                time[1] = '9'
            else:
                time[1] = '3'

        time[3] = '5' if time[3] == '?' else time[3]
        time[4] = '9' if time[4] == '?' else time[4]

        return "".join(time)


if __name__ == "__main__":
    time = "2?:?0"
    print(Solution().maximumTime(time))

    time = "1?:22"
    print(Solution().maximumTime(time))