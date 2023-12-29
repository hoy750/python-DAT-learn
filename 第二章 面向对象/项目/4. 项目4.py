"""P-2.37 and P-2.38"""

import random
class AnimalBase:
    def __init__(self, name: str ,gender: bool = 0, strength: float = 50) -> None:
        """
        gender: 0女， 1男
        strength: 表示力量值
        """
        self._name = name
        self._gender = gender
        self._strength = strength
    def eat(self) -> None:
        pass
    def reat(self) -> None:
        pass
    def generate(self) -> None:
        pass
    def get_gender(self) -> bool:
        return self._gender
    def get_strength(self) -> float:
        return self._strength
    def __str__(self) -> str:
        return "<" + str(self._name) + " " + str(self._gender) + " " + str(self._strength) +">"
    def __len__(self) -> str:
        return 1
class Bear(AnimalBase):
    def __init__(self, name: str = "bear", gender: bool = 0, strength: float = 100) -> None:
        super().__init__(name, gender, strength)

    def generate(self):
        # return super().generate()
        return Bear()
class Fish(AnimalBase):
    def __init__(self, name: str = "fish", gender: bool = 0, strength: float = 100) -> None:
        super().__init__(name, gender, strength)

    def generate(self):
        return Fish()
    
def createEcosystem(width: int = 10, length : int = 10, stream: int = 1) :
    """随机生成一个初始世界, 在这个世界的随机一个地方会有一条小溪， 小溪的位置指定，不指定边界地区为小溪"""
    res = [[ random.choice([None, Bear('bear', random.randint(0, 1), random.random() * 100 ), Fish('fish', random.randint(0, 1) , random.random() * 100)]) for _ in range(width)] for _ in range(length)]

    return res

def createIndex(i: int, j: int, width:int , length: int) :
    i, j  =  i + random.randint(-1, 1), j + random.randint(-1, 1)
    if i == length:
        i = 0
    if j == width:
        j = 0
    return i, j
def getResult(animal1: AnimalBase, animal2: AnimalBase):
    if isinstance(animal1, Bear) and isinstance(animal1, Fish):
        return animal1
    if isinstance(animal1, Fish) and isinstance(animal2, Bear):
        return animal2
    if animal2 == None:
        return animal1
    if animal1.get_gender() == animal2.get_gender():
        return animal1 if animal1.get_strength() >= animal2.get_strength() else animal2
    else:
        if isinstance(animal1, Bear):
            return (Bear('bear', random.randint(0, 1), random.random() * 100 ), "新生儿")
        else:
            return (Fish('fish', random.randint(0, 1) , random.random() * 100), '新生儿')
    raise "有我未考虑到的情况"
def getNone(ecosystem):
    for i  in range(len(ecosystem)):
        for j in range(len(ecosystem[i])):
            if ecosystem[i][j] == None:
                return (i, j)
    return -1
def mainLoop(ecosystem) -> None:
    for i  in range(len(ecosystem)):
        for j in range(len(ecosystem[i])):
            if ecosystem[i][j] == None:
                continue
            else:
                index = createIndex(i, j, len(ecosystem[0]), len(ecosystem))
                if index[0] == i and index[1] == j:
                    continue
                # print(index)
                result = getResult(ecosystem[i][j], ecosystem[index[0]][index[1]])
            if len(result) == 2:
                new_index = getNone(ecosystem)
                if new_index == -1:
                    print('没位置放新生儿')
                    continue
                ecosystem[new_index[0]][new_index[1]] = result[0]
            else:
                ecosystem[index[0]][index[1]] = result
                ecosystem[i][j] = None

if __name__ == "__main__" :
    
    # 定义河水的位置
    STREAM  = 1
    # 定义时间步
    TIME_STEP = 10
    # 生成生态系统
    ecosystem = createEcosystem(10, 10, STREAM)

    # print(len(ecosystem))
    # print(len(ecosystem[0]))
    # print(ecosystem[1])
    # res = (1, 0)
    # print(res[0], res[1])
    # mainLoop(ecosystem)
    # print(ecosystem[1])
    # print(getNone(ecosystem))

    for i in range(TIME_STEP) :
        mainLoop(ecosystem)
        print(ecosystem[1])

    
