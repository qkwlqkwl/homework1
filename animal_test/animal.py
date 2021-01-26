class Animal:
    def __init__(self):
        # self.animalName = "动物"
        # self.colour = "各种颜色"
        # self.age = 0
        # self.gender = "公或母"
        self.animalName = ["狗","鱼","狮子"]
        self.colour = ["黄色","红色","白色"]
        self.age = ["2","1","3"]
        self.gender = ["公","母"]

    def calls(self):
        #print(f"{self.animalName}会发出各种各样的叫声")
        self.voice = ["汪汪","不会叫","吼吼"]
        print(f"大自然里有很多动物会发出各种叫声：")
        for i in range(0,3):
            print(f"{self.colour[i]}的{self.animalName[i]}，它的叫声是：{self.voice[i]}")


    def run(self):
        self.__running = ["散步", "在水里游", "奔跑"]
        for i in range(0,3):
            #print(f"{self.age[i]}岁的{self.animalName[i]}")
            if self.animalName[i] == "狗":
                print(f"{self.age[i]}岁的{self.animalName[i]}的性别是：{self.gender[0]}，它可以{self.__running[i]}")
            elif self.animalName[i] == "鱼":
                print(f"{self.age[i]}岁的{self.animalName[i]}的性别是：{self.gender[1]}，它可以{self.__running[i]}")
            elif self.animalName[i] == "狮子":
                print(f"{self.age[i]}岁的{self.animalName[i]}的性别是：{self.gender[0]}，它可以{self.__running[i]}")
            else:
                print("它跑来跑去")
                break


if __name__ == '__main__':
    calls1 = Animal()
    calls1.calls()
    calls1.run()

