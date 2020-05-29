
class listreplace:

    def replace(self,list):
	self.list = list
	replace_list = ["fizz","buzz","fizzbuzz"]
        for index in range(10000):
		if(list[index]%3 == 0):
			list[index] = replace_list[1]
                if(list[index]%5 == 0):
                        list[index] = replace_list[2]
                if(list[index]%3 == 0 and list[index]%5 == 0):
                        list[index] = replace_list[3] 
	return list 

   def create_list(self, max):
	self.max = max
	i = 0
	lst = []
	while(i <= max):
		i = i + 1
		lst.append(i)
	return lst


listreplace = listreplace()

print(listreplace.replace(listreplace.create_list(10000)))



