# https://leetcode.com/problems/partition-labels
"""
Fun problem, the key here was to preprocess the entire string and keep
track of the last index for a given character.

Then we keep iterating through the entire string attempting to close the
substring and moving the end further if we encounter a character that has
a further last index
"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Get the last index for each letter
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i

        res: list[int] = []
        end = size = 0
        for i, char in enumerate(s):
            end = max(end, last_index[char])
            size += 1

            # If we are at the current character's last index, then we
            # can record it as a valid answer
            if i == end:
                res.append(size)
                size = 0

        return res


if __name__ == "__main__":
    test_case_1 = "ababcbacadefegdehijhklij"  # [9,7,8]

    cls = Solution()
    ans = cls.partitionLabels(test_case_1)
    print("-----")
    print(ans)
