# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign
"""
We can perform a binary search on the "number of tasks" we can complete

This means that we are not really searching for something in a list but a result

Since we have sorted the tasks, if we wanted to check if we could perform 2 tasks, we just
need to check if we can accomplish the task at index = 1 in and to the left

Using the SortedList datastructure also makes it easier for us to find items in an array
and have O(1) removal and lookup times
"""

from sortedcontainers import SortedList


class Solution:
    def maxTaskAssign(
        self, tasks: list[int], workers: list[int], pills: int, strength: int
    ) -> int:
        # Sort both of the lists so that we can use properties of sorted
        # lists to solve more efficiently
        tasks.sort()
        workers.sort()

        # Trim both lists so they have the same length
        #
        # Keep the strongest workers and weakest tasks
        if len(tasks) > len(workers):
            tasks = tasks[0 : len(workers)]
        if len(tasks) < len(workers):
            workers = workers[-len(tasks) :]

        print("tasks  ", tasks)
        print("workers", workers)

        def check(mid: int) -> bool:
            pills_left = int(pills)

            # Take a subset of the strongest workers since that gives us
            # the best chance of accomplishing all of the tasks
            worker_pool = SortedList(workers[len(workers) - mid :])

            # Loop through the tasks in reverse order from the mid point attempting
            # to sovle each task
            for i in range(mid - 1, -1, -1):
                if worker_pool[-1] >= tasks[i]:
                    worker_pool.pop()
                else:
                    if pills_left == 0:
                        return False
                    rep = worker_pool.bisect_left(tasks[i] - strength)
                    if rep == len(worker_pool):
                        return False
                    pills_left -= 1
                    worker_pool.pop(rep)

            return True

        # We can perform a binary search on the "number of tasks" we can complete
        #
        # This means that we are not really searching for something in a list but a result
        #
        # Since we have sorted the tasks, if we wanted to check if we could perform 2 tasks, we just
        # need to check if we can accomplish the task at index = 1 in and to the left
        left = 0
        right = len(tasks)
        res = 0

        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1

        return res


if __name__ == "__main__":
    test_case_1 = {
        "tasks": [10, 15, 30],
        "workers": [0, 10, 10, 10, 10],
        "pills": 3,
        "strength": 10,
    }  # 2

    test_case_2 = {
        "tasks": [6, 7, 7, 8, 9],
        "workers": [2, 5, 6],
        "pills": 1,
        "strength": 3,
    }  # 2

    cls = Solution()
    ans = cls.maxTaskAssign(**test_case_1)  # type: ignore
    print("-------")
    print(ans)
