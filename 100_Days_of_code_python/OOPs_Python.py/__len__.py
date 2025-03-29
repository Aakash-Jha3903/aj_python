class DataClass:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        i=0
        for c in self.data:
            i=i+1
        return i 
        # return len(self.data)

# Example usage:
my_list = DataClass([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5
print(len(DataClass("hell0o")))  # Output:
print(len(my_list.data))  # Output: 5

