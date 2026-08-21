
class Dataset:
    def __init__(self,records):
        self.records = records
    
    def __len__(self):
        return len(self.records)
    

data = Dataset([
    {"name": "Alice"}, 
    {"name": "Bob"},
    {"name": "Charlie"}
])

print(f'There are {len(data)} records.')  # Output: 3
# Output: {'name': 'Alice'}