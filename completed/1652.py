# https://leetcode.com/problems/defuse-the-bomb
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        code_length = len(code)
        result = [0 for _ in range(code_length)]
        if k == 0:
            return result

        factor = 1 if k > 0 else -1
        for i in range(code_length):
            cur = 0

            j = i
            for _ in range(abs(k)):
                j += 1 * factor

                cur += code[j % code_length]
                print(i, j, cur)

            print()
            result[i] = cur

        return result


if __name__ == "__main__":
    test_case_1 = {"code": [5, 7, 1, 4], "k": 3}  # [12,10,16,13]
    test_case_2 = {"code": [2, 4, 9, 3], "k": -2}  # [12,5,6,13]

    test_case = test_case_2
    cls = Solution()
    print(cls.decrypt(test_case["code"], test_case["k"]))
