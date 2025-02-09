# https://leetcode.com/problems/circular-sentence
"""
Simply use the modulus operator to get the next element to compare
against. It suffices to only check the current word's last letter with
the next word's first letter.  This is because we will have the next word
for the last item in the words array be the first word in the sentence due
to the modulus operation.
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        n = len(words)

        for i, word in enumerate(words):
            next_word = words[(i + 1) % n]

            if word[-1] != next_word[0]:
                return False

        return True


if __name__ == "__main__":
    test_case_1 = "leetcode exercises sound delightful"  # true
    test_case_2 = "Leetcode is cool"  # false
    test_case_3 = "ab a"  # false
    test_case_4 = "ab a a"  # false

    cls = Solution()
    ans = cls.isCircularSentence(test_case_4)
    print("-----")
    print(ans)
