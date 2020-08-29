from tower import Tower
from disk import Disk


class TowerOfHanoi:

    def __init__(self, num_disk):
        self.__towers = [Tower('A'), Tower('B'), Tower('C')]
        self.__num_of_moves = 0
        self.__num_of_disks = num_disk

        for i in range(int(num_disk), 0, -1):
            self.__towers[0].append(Disk(i))

    def get_num_of_moves(self):
        return int(self.__num_of_moves)

    def move_disks(self, num_disks_to_move, source, helper, target):
        if num_disks_to_move == 1:
            Tower.move(source, target)
            self.display_towers()
            self.__num_of_moves += 1
            return

        self.move_disks(num_disks_to_move - 1, source, target, helper)
        self.move_disks(1, source, helper, target)
        self.move_disks(num_disks_to_move - 1, helper, source, target)

    def play(self):
        a = self.__towers[0]
        b = self.__towers[1]
        c = self.__towers[2]

        self.display_towers()
        self.move_disks(self.__num_of_disks, a, b, c)
        print("Moving", self.__num_of_disks, "disks completed in", self.get_num_of_moves(), "moves!")

    def display_towers(self):
        if self.__num_of_disks == 4:
            print('Towers:')
            print(self.__towers[0])
            print(self.__towers[1])
            print(self.__towers[2])


