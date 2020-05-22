
class combination:

    def combination(self, *args):
        result = 1
        for element in args:
            result = result * element
        return result

combination = combination()

print(combination.combination(3,4,5))


