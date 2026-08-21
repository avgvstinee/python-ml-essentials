
class Dataset:
    def __init__(self,records):
        self.records = records
    
    def __len__(self):
        return len(self.records)
    
    def __getitem__(self,index):
        return self.records[index]
    
    def __iter__(self):
        return iter(self.records)
    
    def __contains__(self, record):
        return record in self.records


data = Dataset([
    {"name": "Alice"}, 
    {"name": "Bob"},
    {"name": "Charlie"}
])

print(f'There are {len(data)} records.')  # Output: 3
print(f'The first records are {data[0]} ')  # Output: {'name': 'Alice'}
print(f'The last records are {data[-1]} ')  # Output: {'name': 'Charlie'}


for record in data:
    print(record)
    

has_alice = {"name": "Alice"} in data
has_dan = {"name": "Dan"} in data
print(has_alice, has_dan)  # True False