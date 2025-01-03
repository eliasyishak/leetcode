# https://leetcode.com/problems/minimum-cost-for-tickets
"""
Used DFS with a cache to test out all different possible scenarios for decisions
being made about which tickets should be bought.
"""

from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def dfs(day_index: int, curr_cost: int):
            if (day_index, curr_cost) in self.cache:
                return self.cache[(day_index, curr_cost)]

            if day_index is None or day_index >= len(days):
                return curr_cost

            # One day pass
            one_day_cost = curr_cost + costs[0]
            one_day_index = day_index + 1

            # Seven day pass
            seven_day_cost = curr_cost + costs[1]
            seven_day_index = None
            for i, val in enumerate(days[day_index:]):
                if val > days[day_index] + 6:
                    seven_day_index = day_index + i
                    break

            # Monthly (30 day) cost
            month_cost = curr_cost + costs[2]
            month_index = None
            for i, val in enumerate(days[day_index:]):
                if val > days[day_index] + 29:
                    month_index = day_index + i
                    break

            # Get the minimum of the three options after completing the three branches
            res = min(
                [
                    dfs(day_index=one_day_index, curr_cost=one_day_cost),
                    dfs(day_index=seven_day_index, curr_cost=seven_day_cost),
                    dfs(day_index=month_index, curr_cost=month_cost),
                ]
            )
            self.cache[(day_index, curr_cost)] = res
            return res

        return dfs(day_index=0, curr_cost=0)


if __name__ == "__main__":
    test_case_1 = {
        "days": [1, 4, 6, 7, 8, 20],
        "costs": [2, 7, 15],
    }  # 11

    test_case_2 = {
        "days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
        "costs": [2, 7, 15],
    }  # 17

    test_case_3 = {
        "days": [
            1,
            2,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            20,
            21,
            24,
            25,
            27,
            28,
            29,
            30,
            31,
            34,
            37,
            38,
            39,
            41,
            43,
            44,
            45,
            47,
            48,
            49,
            54,
            57,
            60,
            62,
            63,
            66,
            69,
            70,
            72,
            74,
            76,
            78,
            80,
            81,
            82,
            83,
            84,
            85,
            88,
            89,
            91,
            93,
            94,
            97,
            99,
        ],
        "costs": [9, 38, 134],
    }  # 423

    cls = Solution()
    ans = cls.mincostTickets(**test_case_3)
    print("-----")
    print(ans)
