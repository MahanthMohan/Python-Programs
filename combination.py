
class combination:

    def combination(self, input_list):
        self.input_list = input_list
        leng = len(input_list)
        if(leng == 1):
            return input_list[0]
        else:
            return input_list[leng - 1] * input_list[combination.combination(leng - 2)]

combination = combination()

print(combination.combination([3,6,9,7]))


