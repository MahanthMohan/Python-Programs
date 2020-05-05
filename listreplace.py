class listreplace:

    def replace(self):
        for i in range(10000):
            ret = ""
            if i%3 == 0:
                ret = ret + "fizz"
            if i%5 == 0:
                ret = ret + "buzz"
            if ret == "":
                ret = str(i)
            print(ret)

listreplace = listreplace()

print(listreplace.replace())



