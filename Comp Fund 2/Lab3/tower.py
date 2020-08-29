
class Tower(list):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def get_name(self):
        return str(self.__name)

    def move(self, dest_tower):

        if len(self) == 0:
            return
        x = self[-1]
        del self[-1]
        dest_tower.append(x)

    def __str__(self):
        disk_str = 'Tower' + str(self.__name) + ':'
        disk_str += '[' + ','.join([str(d) for d in self]) + ']'
        return disk_str



