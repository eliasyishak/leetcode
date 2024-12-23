# https://leetcode.com/problems/move-pieces-to-obtain-a-string
"""
This was a great problem to understand how to approach something with both a queue
and a two pointer approach. The important thing to think about here is that the two pointer
approach felt more intitutive at first but when you think about it more, the queue approach
is much better suited when you consider that you don't have to only put the value in the queue,
you can also add the index of the item and use that index to easily compare.
"""

from collections import deque


class Solution:
    def canChangeTwoPointer(self, start: str, target: str) -> bool:
        start_index = 0
        target_index = 0
        LENGTH = len(target)

        while start_index < LENGTH or target_index < LENGTH:
            # Continue moving both of the indices until we find non "_" chars
            while start_index < LENGTH and start[start_index] == "_":
                start_index += 1
            while target_index < LENGTH and target[target_index] == "_":
                target_index += 1

            # If we passed the LENGTH while trying to find the next character, then
            # the strings are not going to match so we can exit False
            #
            # Unless both of our indices are at the end of the strings which means
            # we have exhausted all characters available
            if start_index >= LENGTH or target_index >= LENGTH:
                return start_index == target_index == LENGTH

            # The characters need to match to even be considered
            if start[start_index] != target[target_index]:
                return False

            # Breaking condition for "R"
            if start[start_index] == "R" and start_index > target_index:
                return False

            # Breaking condition for "L"
            if start[start_index] == "L" and start_index < target_index:
                return False

            start_index += 1
            target_index += 1

        # By the time we get here, that means we survived all the checks in the main
        # while loop so all conditions are satisfied
        return True

    def canChangeQueue(self, start: str, target: str) -> bool:
        start_queue = deque()
        target_queue = deque()

        for i in range(len(start)):
            if start[i] != "_":
                start_queue.append((start[i], i))
            if target[i] != "_":
                target_queue.append((target[i], i))

        # If we don't have the same number of characters, we are automatically
        # not going to have an answer that works
        if len(start_queue) != len(target_queue):
            return False

        while start_queue:
            start_char, start_index = start_queue.popleft()
            target_char, target_index = target_queue.popleft()

            # They must be the same character for us to consider this a valid solution
            if start_char != target_char:
                return False

            # Breaking condition for the "L" char
            if start_char == "L" and start_index < target_index:
                return False

            # Breaking condition for the "R" char
            if start_char == "R" and start_index > target_index:
                return False

        return True


if __name__ == "__main__":
    test_case_1 = {
        "start_": "L_L__R__R_",
        "target": "LL______RR",
    }  # true
    test_case_2 = {
        "start_": "L_L__R__R_",
        "target": "LL_R_____R",
    }  # false
    test_case_3 = {
        "start_": "___L___",
        "target": "_L_____",
    }  # true
    test_case_4 = {"start_": "_L", "target": "LL"}  # false

    test_case = test_case_1
    cls = Solution()
    ans_two_pointer = cls.canChangeTwoPointer(
        start=test_case["start_"], target=test_case["target"]
    )
    ans_queue = cls.canChangeQueue(
        start=test_case["start_"], target=test_case["target"]
    )
    print("-----")
    print("Two Pointer:", ans_two_pointer)
    print("Queue:      ", ans_queue)
