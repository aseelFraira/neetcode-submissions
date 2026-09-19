class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[(key,timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:
        for ts in range(timestamp,-1,-1):
            if self.store.get((key,ts)):
                return self.store.get((key,ts))
        return ""


    

        

        
