import sys
from Player import Player

def help():
    return '''
    Commands:
    help                Show this help message
    auto n              Run the program in automatic mode with n iterations (default n=1)
    manual p            Run the program in manual mode with p number of players (default p=1)
    '''

def main(args):
    if not args:
        raise ValueError('No arguments have been provided, run the file with the "help" argument to see available options.')

    if args[0] == 'help':
        print(help())
    elif args[0] == 'auto':
        iterations = int(args[1]) if len(args) > 1 else 1
        for i in range(iterations):
            tmp_player = Player(i)
            tmp_player.make_roll()
    elif args[0] == 'manual':
        players = int(args[1]) if len(args) > 1 else 1


if __name__ == '__main__':
    main(sys.argv[1:])
