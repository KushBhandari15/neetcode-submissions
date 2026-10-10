class MyHashSet:

    def __init__(self):
        self.values = []

    def add(self, key: int) -> None:
        if key not in self.values:
            self.values.append(key)
        return
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.values.remove(key)
        return

    def contains(self, key: int) -> bool:
        return key in self.values


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)