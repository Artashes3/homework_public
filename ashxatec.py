class Mlass:
    
    def __init__(self,other) -> None:
     self.other = other
     print("hello")

    


class Junior(Mlass):
    def __init__(self,other,poqri_other) -> None:
        Mlass.__init__(self,other)
        self.poqri_other = poqri_other
        print("goodbye")





obj = Junior("1","2")
print(obj.other)


    

