class TimeMap:

    def __init__(self):
        # Key: key, value: [(value, timestamp)]
        self.hashmap = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap[key]
        res = ""
        low, high = 0, len(arr) - 1
        while low <= high:
            middle = (low + high) // 2
            if arr[middle][1] <= timestamp:
                res = arr[middle][0]
                low = middle + 1
            else :
                high = middle - 1
                
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)