class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data[key]

        left, right = 0, len(arr) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2

            curr_timestamp, curr_val = arr[mid]

            if curr_timestamp <= timestamp:
                res = curr_val
                left = mid + 1
            else:
                right = mid - 1

        return res