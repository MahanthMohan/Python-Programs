
class listreplacer:

    def increment(self,index):
        self.index = index
        i = 1
        list = []
        while  i <= index:
            list.append(i)
            i = i+1
        return list

    def replace(self, list, replace_list):
        self.list = list
        self.replace_list = replace_list
        list_len = len(list)
        index = 0
        while(index <= list_len):
            if(index%3 == 0):
                for list[index] in list:
            return replaced_list
            elif index%5 == 0):
                replaced_list = [list.replace(list[index],"buzz") for list[index] in list]
                return replaced_list
            elif(index%3 == 0 and index%5 == 0):
                replaced_list = [list.replace(list[index],"fizzbuzz") for list[index] in list]
                return replaced_list
            index = index + 1


listreplacer = listreplacer()

replace_list = ["fizz","buzz","fizzbuzz"]
print(listreplacer.replace(listreplacer.increment(10000), replace_list))
