class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        key_timestamps = self.store.get(key)
        if not key_timestamps:
            return ""

        left = 0
        right = len(key_timestamps) - 1
        value = ""
        
        while left <= right:
            mid = (left + right)//2
            if key_timestamps[mid][0] == timestamp:
                return key_timestamps[mid][1]
            elif key_timestamps[mid][0] < timestamp:  
                value = key_timestamps[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return value
                




    

        

        
