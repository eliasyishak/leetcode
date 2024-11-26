# https://leetcode.com/problems/find-champion-ii
from typing import List
'''
Pretty easy if you understand that the winner is the node that doesn't
have any edges going into it (in_degrees)
'''


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        players = [0 for _ in range(n)]
        for _, receiving_node in edges:
            players[receiving_node] += 1

        winner = None
        for i, in_degree in enumerate(players):
            if in_degree == 0:
                if winner is None:
                    winner = i
                else:
                    return -1

        return winner


if __name__ == "__main__":
    test_case_1 = {"edges": [[0, 1], [1, 2]], "n": 3}

    test_case = test_case_1
    cls = Solution()
    ans = cls.findChampion(edges=test_case["edges"], n=test_case["n"])
