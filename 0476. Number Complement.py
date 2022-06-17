class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        num_list = list(map(int, str(num)))
        com_list = []
        for i in range(len(num_list)):
            if num_list[i] == 1:
                com_list.append(0)
            elif num_list[i] == 0:
                com_list.append(1)
        s = [str(i) for i in com_list]
        com = "".join(s)
        com  = int(com, 2)
        return com
