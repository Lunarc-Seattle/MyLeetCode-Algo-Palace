class TimeMap:

    def __init__(self):
        self.store = {} # key(string) : ["string" , timestamp_int]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [ ]
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        value = self.store[key] # this is a list
        res = ""
        l , r = 0, len(value)-1
        # binary search
        while l <= r: # get the last equal value
            mid = (l+r)//2
            if value[mid][1] <= timestamp:
                l = mid +1 
                res = value[mid][0] # # Potential candidate
            else:
                r = mid -1
        return res
        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
