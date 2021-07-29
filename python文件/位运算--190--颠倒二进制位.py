__time__ = '2021/7/28'
__author__ = 'ZhiYong Sun'
__doc__ = '前后颠倒给定的 32 位无符号整数的二进制位。'


class Solution_non:
    def reverseBits(self, n: int) -> int:
        # 不是正经的方法
        s = str(bin(n))
        s = s[2:][::-1] + '0' * (34 - len(s))
        return int(s, 2)


# 正经方法--位运算分治
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = (n & 0xff00ff00) >> 8 | (n & 0x00ff00ff) << 8     # 0xff00ff00 -- 0b11111111000000001111111100000000
        n = (n & 0xf0f0f0f0) >> 4 | (n & 0x0f0f0f0f) << 4     # 0xf0f0f0f0 -- 0b11110000111100001111000011110000
        n = (n & 0xcccccccc) >> 2 | (n & 0x33333333) << 2     # 0xcccccccc -- 0b11001100110011001100110011001100
        n = (n & 0xaaaaaaaa) >> 1 | (n & 0x55555555) << 1     # 0xaaaaaaaa -- 0b10101010101010101010101010101010
        return n


if __name__ == "__main__":
    print(bin(43261596))
    print(bin(Solution().reverseBits(43261596)))

