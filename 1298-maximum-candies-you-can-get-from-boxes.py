# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes


from collections import defaultdict, deque
from typing import List, TypedDict


class Solution:
    def maxCandies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        containedBoxes: list[list[int]],
        initialBoxes: list[int],
    ) -> int:
        res = 0
        queue: deque[int] = deque(initialBoxes)
        keys_collected: set[int] = set()
        while queue:
            current_box = queue.popleft()

            if status[current_box] == 1:
                # Collect the candy from the box
                res += candies[current_box]

                # Collect any keys that exist
                for key in keys[current_box]:
                    keys_collected.add(key)

                # Add to the queue the boxes in this box
                for inner_box in containedBoxes[current_box]:
                    queue.append(inner_box)

            else:
                print(current_box, keys_collected)

        return res


if __name__ == "__main__":

    class TestCaseType(TypedDict):
        status: List[int]
        candies: List[int]
        keys: List[List[int]]
        containedBoxes: List[List[int]]
        initialBoxes: List[int]

    test_case_1: TestCaseType = {
        "status": [1, 0, 1, 0],
        "candies": [7, 5, 4, 100],
        "keys": [[], [], [1], []],
        "containedBoxes": [[1, 2], [3], [], []],
        "initialBoxes": [0],
    }  # 16

    cls = Solution()
    ans = cls.maxCandies(**test_case_1)
    print("-----")
    print(ans)
