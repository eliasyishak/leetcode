# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values
"""
Simply increment through each array by performing the conditional checks
necessary for adding to the final array. At the end, make sure to flush
out any remaining values.
"""


class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        res: list[list[int]] = []
        i = j = 0
        n1, n2 = len(nums1), len(nums2)

        while i < n1 and j < n2:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 == id2:
                res.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                res.append([id1, val1])
                i += 1
            else:
                res.append([id2, val2])
                j += 1

        # This ensures that any of the left over values get append
        return res + nums1[i:] + nums2[j:]


if __name__ == "__main__":
    test_case_1 = {
        "nums1": [[1, 2], [2, 3], [4, 5]],
        "nums2": [[1, 4], [3, 2], [4, 1]],
    }  # [[1,6],[2,3],[3,2],[4,6]]

    test_case_2 = {
        "nums1": [[2, 4], [3, 6], [5, 5]],
        "nums2": [[1, 3], [4, 3]],
    }  # [[1,3],[2,4],[3,6],[4,3],[5,5]]

    cls = Solution()
    ans = cls.mergeArrays(**test_case_2)
    print("------")
    print(ans)
