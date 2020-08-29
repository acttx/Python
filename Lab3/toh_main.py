from towers_of_hanoi import TowerOfHanoi


def main():
    for disks in range(3, 25):
        toh = TowerOfHanoi(disks)
        toh.play()


if __name__ == '__main__':
    main()

