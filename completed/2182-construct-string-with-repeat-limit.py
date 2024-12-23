# https://leetcode.com/problems/construct-string-with-repeat-limit
"""
This is a fun heap problem that requires you to think in a greedy way. The key
here is to understand that if you want to get the "largest" lexicographical
string, you need to prioritize putting the "larger" letters in the beginning.

Everything is easy if you count of characters is below the repeat limit, but when we
have more than the repeat limit, we need to use the queue to get at least one larger
letter. Once we added this buffer, we put TWO items back into the heap
"""

import heapq
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        queue = []
        for char, count in c.items():
            queue.append((-(ord(char) - ord("a")), char, count))

        heapq.heapify(queue)
        ans = ""
        while queue:
            _ord, char, count = heapq.heappop(queue)

            if count <= repeatLimit:
                ans += char * count
            else:
                ans += char * repeatLimit

                # If we have additional letters to pull from, we will attempt
                # to pull at least one more letter.
                #
                # Notice that if we don't have anything left in the queue, then
                # we also don't add the original [char] from above back into the heap
                # since the string will no longer be valid
                if len(queue) > 0:
                    next_ord, next_char, next_count = heapq.heappop(queue)
                    ans += next_char
                    next_count -= 1
                    # This means we can still use this character after finishing with the
                    # original [char]
                    if next_count > 0:
                        heapq.heappush(queue, (next_ord, next_char, next_count))

                    heapq.heappush(queue, (_ord, char, count - repeatLimit))

        return ans


if __name__ == "__main__":
    test_case_1 = {
        "s": "cczazcc",
        "repeatLimit": 3,
    }  # zzcccac
    test_case_2 = {
        "s": "aababab",
        "repeatLimit": 2,
    }  # bbabaa

    cls = Solution()
    answer = cls.repeatLimitedString(**test_case_2)
    print("----")
    print(answer)
