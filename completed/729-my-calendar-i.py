# https://leetcode.com/problems/my-calendar-i
"""
This could probably be further optimized to use a binary search
but this works just fine :)
"""


class MyCalendar:
    def __init__(self) -> None:
        self.timestamps: list[tuple[int, str]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        temp = list(self.timestamps)

        temp.append((startTime, "start"))
        temp.append((endTime, "end"))
        temp.sort()

        for i, (_, direction) in enumerate(temp):
            if i == 0:
                continue

            _, prev_direction = temp[i - 1]
            if direction == prev_direction:
                return False

        self.timestamps = list(temp)
        return True


if __name__ == "__main__":
    cls = MyCalendar()

    print(cls.book(10, 20))  # true
    print(cls.book(15, 25))  # false
    print(cls.book(20, 30))  # true
