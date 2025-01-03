# https://leetcode.com/problems/count-vowel-strings-in-ranges/?envType=daily-question&envId=2025-01-03
"""
Prefix sum problem where keep track of the valid words from the left to the
right. Tricky part of this problem was understanding that we don't use the
prefix[left] value, we need prefix[left - 1] because the left value is already
accounted for within the right sum. If we don't do this, then the
value is getting double counted
"""

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(["a", "e", "i", "o", "u"])
        res = [0] * len(queries)

        prefix = [0] * len(words)
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                if i == 0:
                    prefix[i] = 1
                else:
                    prefix[i] = prefix[i - 1] + 1
            else:
                if i > 0:
                    prefix[i] = prefix[i - 1]

        for j, (left, right) in enumerate(queries):
            if left == 0:
                res[j] = prefix[right]
            else:
                # Need to count the number of words prefix[left - 1] because the
                # word at prefix[left] is already accounted for within the running
                # count on prefix[right]
                res[j] = prefix[right] - prefix[left - 1]

        return res


if __name__ == "__main__":
    test_case_1 = {
        "words": ["aba", "bcb", "ece", "aa", "e"],
        "queries": [[0, 2], [1, 4], [1, 1]],
    }  # [2,3,0]

    test_case_2 = {
        "words": ["a", "e", "i"],
        "queries": [[0, 2], [0, 1], [2, 2]],
    }  # [3,2,1]

    test_case_3 = {
        "words": [
            "b",
            "rmivyakd",
            "kddwnexxssssnvrske",
            "vceguisunlxtldqenxiyfupvnsxdubcnaucpoi",
            "nzwdiataxfkbikbtsjvcbjxtr",
            "wlelgybcaakrxiutsmwnkuyanvcjczenuyaiy",
            "eueryyiayq",
            "bghegfwmwdoayakuzavnaucpur",
            "ukorsxjfkdojcxgjxgmxbghno",
            "pmgbiuzcwbsakwkyspeikpzhnyiqtqtfyephqhl",
            "gsjdpelkbsruooeffnvjwtsidzw",
            "ugeqzndjtogxjkmhkkczdpqzwcu",
            "ppngtecadjsirj",
            "rvfeoxunxaqezkrlr",
            "adkxoxycpinlmcvmq",
            "gfjhpxlzmokcmvhjcrbrpfakspscmju",
            "rgmzhaj",
            "ychktzwdhfuruhpvdjwfsqjhztshcxdey",
            "yifrzmmyzvfk",
            "mircixfzzobcficujgbj",
            "d",
            "pxcmwnqknyfkmafzbyajjildngccadudfziknos",
            "dxmlikjoivggmyasaktllgmfhqpyznc",
            "yqdbiiqexkemebyuitve",
        ],
        "queries": [
            [5, 21],
            [17, 22],
            [19, 23],
            [13, 15],
            [20, 23],
            [21, 23],
            [6, 20],
            [1, 8],
            [15, 20],
            [17, 22],
            [6, 6],
            [1, 2],
            [4, 11],
            [14, 23],
            [7, 10],
            [16, 22],
            [20, 22],
            [21, 22],
            [15, 18],
            [5, 16],
            [17, 23],
        ],
    }  # [2,0,0,0,0,0,2,1,0,0,0,0,2,0,1,0,0,0,0,2,0]

    cls = Solution()
    ans = cls.vowelStrings(**test_case_3)
    print("-----")
    print(ans)
