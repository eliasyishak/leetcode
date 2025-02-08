# https://leetcode.com/problems/design-a-number-container-system
"""
This problem can be solved in two ways.

The first way is thanks to a datastructure that is not standard to the python
library. The sortedcollections.SortedSet data structure can keep track of order
when adding and removing from the set in better than O(n) time

The second way is to use a heap, which was my first idea when thinking of this problem.
Initially, I was actively managing the two dictionaries on every change, when in reality,
we can do this lazily instead whenever we invoke the find method for a number. I like this
solution better since it makes sure that the change is done faster in O(logn) time, which is
what it takes to insert into a heap.
"""

import heapq
from collections import defaultdict

from sortedcollections import SortedSet  # type: ignore


class NumberContainersSortedSet:
    def __init__(self) -> None:
        # Key is the number, value is a min heap of indexes
        self.numbers: dict[int, set[int]] = defaultdict(SortedSet)

        # Key is the index, value is the number
        self.indexes: dict[int, int] = {}

    def change(self, index: int, number: int) -> None:
        self.numbers[number].add(index)

        # If we are setting the value for that index for the first time
        if index not in self.indexes:
            self.indexes[index] = number

        # If we are changing the number at that index
        else:
            prev_number = self.indexes[index]

            # Remove the index for this number
            self.numbers[prev_number].remove(index)
            self.indexes[index] = number

    def find(self, number: int) -> int:
        if number in self.numbers and len(self.numbers[number]) > 0:
            return min(self.numbers[number])

        return -1


class NumberContainers:
    def __init__(self) -> None:
        # Key is the number, value is a min heap of indexes
        self.numbers: dict[int, list[int]] = defaultdict(list)

        # Key is the index, value is the number
        self.indexes: dict[int, int] = {}

    def change(self, index: int, number: int) -> None:
        """
        In this solution, we will just map each index to a number
        and each number to an index, it will be when we attempt to
        find a value that we correct overwritten values
        """

        self.indexes[index] = number

        heapq.heappush(self.numbers[number], index)

    def find(self, number: int) -> int:
        if number not in self.numbers:
            return -1

        while self.numbers[number]:
            top_index = self.numbers[number][0]
            if self.indexes[top_index] == number:
                return top_index

            heapq.heappop(self.numbers[number])

        return -1


if __name__ == "__main__":
    container = NumberContainers()

    container.change(1, 10)
    print(container.find(10), "should be", 1)
    container.change(1, 20)
    print(container.find(10), "should be", -1)
    print(container.find(20), "should be", 1)
    print(container.find(30), "should be", -1)
