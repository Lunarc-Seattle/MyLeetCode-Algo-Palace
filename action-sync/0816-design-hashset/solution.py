class MyHashSet:

    def __init__(self):
        self.size = 1009  # 用一个质数，减少冲突
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size  # 简单的哈希函数

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key not in bucket:  # 避免重复添加
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]
        return key in bucket

