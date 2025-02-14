"""
Using a prefix product list helps to identify the value for a given
index k.  Understanding that you can reset the list whenever we reach a 0
makes this problem optimized though since anything to the left of that 0
has a product of 0.
"""


class ProductOfNumbers:
    def __init__(self):
        self.arr = [1]
        self.size = 0

    def add(self, num: int) -> None:
        # If we have a zero passed in, we can reset the state because
        # anything to the left of the zero becomes zero
        if num == 0:
            self.arr = [1]
            self.size = 0
        else:
            self.arr.append(self.arr[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        # Anything greater than the size of the array would result
        # in a zero since the array resets whenever we have a zero
        if k > self.size:
            return 0

        return self.arr[self.size] // self.arr[self.size - k]


class ProductOfNumbersSlow:
    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        self.arr.append(num)

    def getProduct(self, k: int) -> int:
        res = 1
        for val in self.arr[-k:]:
            res *= val
        return res


if __name__ == "__main__":
    productOfNumbers = ProductOfNumbers()
    productOfNumbers.add(3)  # [3]
    productOfNumbers.add(0)  # [3,0]
    productOfNumbers.add(2)  # [3,0,2]
    productOfNumbers.add(5)  # [3,0,2,5]
    productOfNumbers.add(4)  # [3,0,2,5,4]

    print(
        productOfNumbers.getProduct(2)
    )  # return 20. The product of the last 2 numbers is 5 * 4 = 20
    print(
        productOfNumbers.getProduct(3)
    )  # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
    print(
        productOfNumbers.getProduct(4)
    )  # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0

    productOfNumbers.add(8)  # [3,0,2,5,4,8]

    print(
        productOfNumbers.getProduct(2)
    )  # return 32. The product of the last 2 numbers is 4 * 8 = 32
