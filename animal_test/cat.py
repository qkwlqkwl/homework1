from animal_test.animal import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.hair = "短毛"
        self.animalName = "猫"

    def skill(self):
        print(f"{self.hair}的{self.animalName}会抓老鼠！")


    def calls(self):
        self.voice = ["喵喵"]
        print(f"大自然里有很多动物会发出各种叫声：")
        try:
            for i in range(0,3):
                print(f"{self.colour[i]}的{self.animalName[i]}，它的叫声是：{self.voice[i]}")
                break
        except IndexError:
            print("这是一个索引超出范围的异常")


if __name__ == '__main__':
    littleCat = Cat()
    littleCat.calls()
    littleCat.run()
    littleCat.skill()
