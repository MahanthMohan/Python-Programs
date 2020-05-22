
class separator:

    def return_int(self, list):
        self.list = list   
        lst = []
        for i in range(0, len(list)):
            data_type = type(list[i])
            if(data_type is int):
                lst.append(list[i])
                return lst
        
        
separator = separator()

sample = ["foo", "toom", "apple", 123, 457]
print(separator.return_int(sample))

