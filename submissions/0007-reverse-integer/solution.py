class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        # rev = int(str(abs(x))[::-1]) * sign
        return (int(str(abs(x))[::-1]) * sign) if (-2**31)<(int(str(abs(x))[::-1]) * sign)<((2**31)-1) else 0
