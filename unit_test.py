import unittest
from SearchInsertPosition_BinarySearch import Solution


class SearchInsertPositionTest(unittest.TestCase):
    def test_Example_1(self):
        temp = Solution()
        self.nums = [1, 3, 5, 6]
        self.target = 5
        self.assertEqual(temp.searchInsert(self.nums, self.target), 2)

    def test_Example_2(self):
        temp = Solution()
        self.nums = [1, 3, 5, 6]
        self.target = 2
        self.assertEqual(temp.searchInsert(self.nums, self.target), 1)

    def test_Example_3(self):
        temp = Solution()
        self.nums = [1, 3, 5, 6]
        self.target = 7
        self.assertEqual(temp.searchInsert(self.nums, self.target), 4)

    def test_Example_4(self):
        temp = Solution()
        self.nums = [1, 3, 5, 6]
        self.target = 0
        self.assertEqual(temp.searchInsert(self.nums, self.target), 0)

    def test_longNums(self):
        temp = Solution()
        self.nums = list(range(100000))
        self.target = 100000
        self.assertEqual(temp.searchInsert(self.nums, self.target), 100000)


if __name__ == "__main__":
    unittest.main()
