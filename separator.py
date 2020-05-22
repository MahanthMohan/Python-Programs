import math

class separator:

    def return_int(self, list):
        self.list = list
        data_types = [type(element) for element in list]
        for element in data_types:
            if(element == "<class 'int'>"):
                return list

separator = separator()

sample = ["foo", "toom", "apple", 123, 457]
print(separator.return_int(sample))