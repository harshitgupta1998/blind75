# a =-14
# b = 16
# boo = False
# if a < 0 and b >= 0:
#     a = ~a
#     a,b = b, a
#     while (b != 0 ):
#         pass
# elif a >= 0 and b < 0:
#     b -= 1
#     print(a & b)
# elif a < 0 and b < 0:
#     a = -1 * a
#     b = -1 * a
#     boo = True
# while True:
#     if not b:
#         print(a)
#         break
#     Sum = a ^ b
#     carry = (a & b) << 1
#     a = Sum
#     b = carry
# if boo:
#     print(-1 * Sum)
# print(Sum)
class Solution:
    def addVal(self, a: int, b: int, mask: int) -> int:
        if b == 0:
            return a
        return self.addVal((a^b) & mask, ((a&b)<<1) & mask, mask)
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        val = self.addVal(a, b, mask)
        if val > 2**31:
            return ~(val ^ mask)
        else:
            return val

print(Solution().getSum(-1,1))