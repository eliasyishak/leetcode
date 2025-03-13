# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks
"""
Sliding window problem where we only increment the
left side by only one. I mistakenly used a while loop within
the main loop but given those conditions, we will always exit
out of the while loop after incrementing left by 1
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        # At most, we will be making k swaps
        res = k

        current_swaps = 0
        left = 0
        for right in range(n):
            if blocks[right] == "W":
                current_swaps += 1

            if right - left + 1 >= k:
                res = min(res, current_swaps)

                if blocks[left] == "W":
                    current_swaps -= 1

                left += 1

        return res


if __name__ == "__main__":
    cls = Solution()
    ans = cls.minimumRecolors(blocks="WBBWWBBWBW", k=7)  # 3
    print("------")
    print(ans)
