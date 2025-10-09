
class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_num:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration
        
it = MyIterator(3)
# print(next(it))
# print(next(it))
# print(next(it))

for num in it:
    print(num)