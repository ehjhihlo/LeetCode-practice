class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=bin(x)[2:]
        y=bin(y)[2:]
        x_list = list(map(int, str(x)))
        y_list = list(map(int, str(y)))
        length = max(len(x_list),len(y_list))
        while len(x_list) < length:
            x_list.insert(0, 0)
        while len(y_list) < length:
            y_list.insert(0, 0)

        distance = 0
        for i in range(length):
            if x_list[i] != y_list[i]:
                distance+=1     
        return distance
