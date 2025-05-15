# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii
"""
Similar approach to the first version of this problem but with this one it
is slightly easier because we are not adding new characters when going
from z -> a

This solution works but it fails on TLE for the third test case, good enough for me :)
"""

from tqdm import tqdm


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def get_pos(char):
            return ord(char) - ord("a")

        freq = [0] * 26
        for char in s:
            pos = get_pos(char)
            freq[pos] += 1

        new_freq = [0] * 26
        for _ in tqdm(range(t), desc="Transformations"):
            for index in range(26):
                if freq[index] == 0:
                    continue

                new_index = index

                # Fill the next values in the new frequency list
                for _ in range(nums[index]):
                    new_index = (new_index + 1) % 26

                    new_freq[new_index] += freq[index]

            # Swap the lists and create a new empty
            freq = list(new_freq)
            new_freq = [0] * 26

        return sum(freq) % MOD


if __name__ == "__main__":
    test_case_1 = {
        "s": "abcyy",
        "t": 2,
        "nums": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
        ],
    }  # 7

    test_case_2 = {
        "s": "azbk",
        "t": 1,
        "nums": [
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
        ],
    }  # 8

    test_case_3 = {
        "s": "bvqbowlhpfhpaddcegzxiawnprkhbvqlmqegsydbykdrxywxvtjlqkuvzasrfdwgepgkbcsxebrkeegttxugleyzytnfpsjimuxqjpjgqbxtbrpntxgxaahldwwnemzwtpgnbvhqikibmqwkxjlvklnuidgwhrxdnwjzxgazfckirtzzwacsvinisjzjyaibwamcbjkcxkdzripdrgyeewkpgofezpcbjbpbdhzltzmqffaqrqcefjwyuyimzpftumzdkazbkijezidrcabvfiltkxzzyywxogsccxkmihqwmehuicpolzxxqvyjdtsuohwthzmigprfjooframjuckvqxjboowpmbdwokzprniwejbbbzwvspufgilhylgukfqgdkiuezvfhxsbpkorbouyqapbwlbezukjhbiiykncopskkzajggslrplccqqcnogvhzjprfyuanmuuwhbndkmasesrpgwdgjyvcscmtiwyhsexvahitchwswafbftffrfpnwepijdmxlzihsnszpjvztxjvxbcbepbfhzcvmxfdibhycvzmzsnqtowvnyqoprmlpfdemyxawlahnlyihrkauraudjvkbsovqhpfvuxletqienvlcwnwdntusvwrgmlaibacdmxwarakxiqiqaaihtnfdmkrtknqrhhsebeizjwrdavzldafamwkj",
        "t": 492153482,
        "nums": [
            23,
            20,
            4,
            11,
            4,
            24,
            13,
            25,
            12,
            21,
            17,
            7,
            6,
            21,
            12,
            11,
            22,
            25,
            22,
            16,
            19,
            8,
            16,
            18,
            19,
            16,
        ],
    }  # LOL too long, not doing matrix math

    cls = Solution()
    ans = cls.lengthAfterTransformations(**test_case_2)  # type: ignore
    print("-------")
    print(ans)
