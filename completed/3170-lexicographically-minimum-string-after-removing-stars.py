# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars
"""
Good use of heaps for this problem. Good problem over all.
"""

import heapq
from collections import defaultdict


class Solution:
    def clearStars(self, s: str) -> str:
        heap: list[str] = []
        index_stack: dict[str, list[int]] = defaultdict(list)
        skips: set[int] = set()
        for i, char in enumerate(s):
            if char.isalpha():
                # We could use another data structure to check if we have this char
                # already but since the most items we could have in this heap is 26,
                # we can just look it up with built in "in" operators
                if char not in heap:
                    heapq.heappush(heap, char)
                index_stack[char].append(i)
            # "*" case
            else:
                # Only need to do operation here to delete
                if heap:
                    # The top of the heap is the smallest character
                    remove_char = heap[0]

                    # The last item in the stack will be the closest index
                    # of the character we want to remove
                    remove_index = index_stack[remove_char].pop()

                    skips.add(remove_index)

                    # Pop from the heap if we don't have any more indexes in the stack
                    if len(index_stack[remove_char]) == 0:
                        heapq.heappop(heap)
                        del index_stack[remove_char]

        res = ""
        for i, char in enumerate(s):
            if char == "*" or i in skips:
                continue

            res += char

        return res


if __name__ == "__main__":
    test_case_1 = "abc*de*fgh*"  # defgh
    test_case_2 = "c*zb"  # zb
    test_case_3 = "aaba*"  # aab
    test_case_4 = "deed****k*"

    cls = Solution()
    ans = cls.clearStars(test_case_4)
    print("------")
    print(ans)
