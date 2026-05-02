class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            # 加上 a 的当前位
            if i >= 0:
                carry += int(a[i])
                i -= 1
            # 加上 b 的当前位
            if j >= 0:
                carry += int(b[j])
                j -= 1

            # 当前位的结果是 carry % 2，进位是 carry // 2
            res.append(str(carry % 2))
            carry //= 2
        return "".join(res[::-1])        