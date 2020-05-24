
class count:
    
    def count(self, list):
        self.list = list
        list_1 = [2,3,4,5,6]
        list_2 = [7,8,9]
        list_3 = [10, "J", "Q", "K", "A"]

        for element in list:
            if(element in list_1):
                list[list.index(element)] = 1
            elif(element in list_2):
                list[list.index(element)] = 0
            elif(element in list_3):
                list[list.index(element)] = -1
        
        result = 0
        for number in list:
            result = result + number
        return result


count = count()

list = ["A", "A", "K", "Q", "Q", "J"]
print(count.count(list))
