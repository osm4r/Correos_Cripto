from mods import *


def main():
    options = ['Deploy Contract', 'Interact Functions', 'Call Functions', 'Exit']
    op = 0
    while op != 4:
        print('\n\n---Que desea hacer?---')
        for x in range(len(options)):
            print(f'{x + 1}. {options[x]}')
        op = int(input('op: '))
        if op == 1:
            deploy('0x37BdcD6908178ad42c281f20c9d458eAd567f112', '00752bdc89972bd218d20199d21c388041f288d48bd3e33929047793c94666e1')
        if op == 2:
            interact('0x37BdcD6908178ad42c281f20c9d458eAd567f112', '00752bdc89972bd218d20199d21c388041f288d48bd3e33929047793c94666e1')
        elif op == 3:
            call('0x37BdcD6908178ad42c281f20c9d458eAd567f112', '00752bdc89972bd218d20199d21c388041f288d48bd3e33929047793c94666e1')
        elif op == 4:
            op = 4


if __name__ == '__main__':
    main() 