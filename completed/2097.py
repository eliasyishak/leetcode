# https://leetcode.com/problems/valid-arrangement-of-pairs
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict, deque

        edges = defaultdict(deque)
        in_degree, out_degree = defaultdict(int), defaultdict(int)

        # Build the adjacency list and track in-degrees and out-degrees
        for pair in pairs:
            start, end = pair
            edges[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        result = []

        def visit(node):
            """
            Helper function to perform the DFS; the DFS will go all
            the way to the last node and return back up, which is why
            we end up reversing the result array when create the answer
            """
            while edges[node]:
                nextNode = edges[node].popleft()
                visit(nextNode)
            result.append(node)

        # Find the start node (outDegree == 1 + inDegree )
        startNode = -1
        for node in out_degree:
            if out_degree[node] == in_degree[node] + 1:
                startNode = node
                break

        # If no such node exists, start from the first pair's first element
        # this could happen for an Euler path
        if startNode == -1:
            startNode = pairs[0][0]

        # Start DFS traversal
        visit(startNode)

        # Reverse the result since DFS gives us the path in reverse
        result.reverse()

        # Construct the result pairs
        pairedResult = [[result[i - 1], result[i]] for i in range(1, len(result))]

        return pairedResult

        """
        BRUTE FORCE ATTEMPT
        this didn't work because we fail to check for other paths for the same
        endpoint
        
        for i in range(len(pairs)):
            current_pairs = [*pairs]
            pair = current_pairs.pop(i)
            result = [pair]

            while current_pairs:
                pair_found = False
                for j in range(len(current_pairs)):
                    curr_left, curr_right = current_pairs[j]

                    # Check if it matches the left of the result
                    if curr_right == result[0][0]:
                        current_pairs.pop(j)
                        result.insert(0, [curr_left, curr_right])
                        pair_found = True
                        break

                    # Check if it matches the right side of the result
                    if curr_left == result[-1][-1]:
                        current_pairs.pop(j)
                        result.append([curr_left, curr_right])
                        pair_found = True
                        break

                if not pair_found:
                    print(result)
                    print(current_pairs)
                    quit()
                    break

            if len(result) == len(pairs):
                return result
            
        # This should never happen because the problem states that there will always be
        # an answer for the provided pairs array
        return []
        """


if __name__ == "__main__":
    test_case_1 = [[5, 1], [4, 5], [11, 9], [9, 4]]  # [[11,9],[9,4],[4,5],[5,1]]
    test_case_2 = [
        [5, 13],
        [10, 6],
        [11, 3],
        [15, 19],
        [16, 19],
        [1, 10],
        [19, 11],
        [4, 16],
        [19, 9],
        [5, 11],
        [5, 6],
        [13, 5],
        [13, 9],
        [9, 15],
        [11, 16],
        [6, 9],
        [9, 13],
        [3, 1],
        [16, 5],
        [6, 5],
    ]  # [[4, 16], [16, 5], [5, 13], [13, 5], [5, 6], [6, 9], [9, 15], [15, 19], [19, 11], [11, 3], [3, 1], [1, 10], [10, 6], [6, 5], [5, 11], [11, 16], [16, 19], [19, 9], [9, 13], [13, 9]]

    test_case = test_case_2

    cls = Solution()
    ans = cls.validArrangement(pairs=test_case)
    print("----")
    print(ans)
