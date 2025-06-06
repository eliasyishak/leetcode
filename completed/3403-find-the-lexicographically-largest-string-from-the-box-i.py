# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i
"""
Such an interesting problem. When looking at the suggested solution, it
suggested enumeration (straightforward) and a two pointer solution. The two
pointer solution seemed to make sense in my mind but I kept hitting some walls
trying to implement it.

A heap solution made sense to me because we can intelligently decide from where
we should try to build our string. The heap will be based on each letter's position
and we will pop them out and see what we have for our string.

A good optimization is to break out of our while loop once we detect that the character
we are checking is smaller than what we currently have built out in res.
"""

import heapq
from typing import TypedDict


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        # Define the longest a string can be given the number of friends
        max_length = len(word) - numFriends + 1

        # Use a heap to keep track of the largest characters
        # along with their index, use a set to ensure that we
        # only keep the first occurence of a character
        heap: list[tuple[int, str, int]] = []
        for index, char in enumerate(word):
            pos = ord(char) - ord("a")
            heapq.heappush(heap, (-pos, char, index))

        # Use the heap to find the positions of the largest
        # characters and attempt to create the longest string possible
        res = ""
        while heap:
            _, char, index = heapq.heappop(heap)

            # If we detect the next char is smaller than the current res, we can
            # break early
            if len(res) > 0 and res[0] > char:
                break

            res = max(res, word[index : index + max_length])

        return res


if __name__ == "__main__":

    class TestCaseType(TypedDict):
        word: str
        numFriends: int

    test_case_1: TestCaseType = {
        "word": "dbca",
        "numFriends": 2,
    }  # dbc

    test_case_2: TestCaseType = {
        "word": "gggg",
        "numFriends": 4,
    }  # g

    test_case_3: TestCaseType = {
        "word": "dah",
        "numFriends": 3,
    }  # h

    test_case_4: TestCaseType = {
        "word": "aann",
        "numFriends": 2,
    }  # nn

    test_case_5: TestCaseType = {
        "word": "nbjnc",
        "numFriends": 2,
    }  # nbjn

    cls = Solution()
    ans = cls.answerString(**test_case_5)
    print("-----")
    print(ans)
