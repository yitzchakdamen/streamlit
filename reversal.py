from typing_extensions import Self
import pandas as pd






class ReversalSurgery:
    
    _instance = None
    
    def __new__(cls, *args) -> Self:
        if not cls._instance: 
            cls._instance = super(ReversalSurgery, cls).__new__(cls)
        return cls._instance

    def __init__(self, url) -> None:
        self.df = pd.read_csv(url)
    
    def get():
        pass

        
        
        
        
        
if __name__ == "__main__":
    url = "shekel.csv"
    ReversalSurgery(url).df.head()
