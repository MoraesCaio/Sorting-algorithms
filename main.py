from generator import Generator
from sorter import Sorter
import argparse

parser = argparse.ArgumentParser()

# SETTINGS
parser.add_argument('-n', '--length', type=int, default=2, help='Number of elements.')
parser.add_argument('-m', '--min', type=int, default=0, help='Minimum value possible for elements.')
parser.add_argument('-M', '--max', type=int, default=100, help='Maximum value possible for elements.')
parser.add_argument('--swaps', type=int, default=1, help='Number of swaps made on "nearly sorted" list generation.')
parser.add_argument('--uniques', type=int, default=1, help='Number of unique values on "few uniques" list.')
parser.add_argument('--seed', type=int, default=None, help='Integer random seed.')

# LISTS
parser.add_argument('-sl', '--sorted', action='store_true', help='Calls sorting methods with "sorted list".')
parser.add_argument('-nl', '--nearly', action='store_true', help='Calls sorting methods with "nearly sorted list".')
parser.add_argument('-rl', '--random', action='store_true', help='Calls sorting methods with "random list".')
parser.add_argument('-Rl', '--reversed', action='store_true', help='Calls sorting methods with "reversed list".')
parser.add_argument('-ul', '--few-unique', action='store_true', help='Calls sorting methods with "few uniques list".')

# SORTING METHODS
parser.add_argument('-is', '--insertion', action='store_true', help='Calls INSERTION sort.')
parser.add_argument('-ss', '--selection', action='store_true', help='Calls SELECTION sort.')


args, _ = parser.parse_known_args()


g = Generator()
s = Sorter()
g.generate(args.length, args.min, args.max, args.uniques, args.swaps, args.seed)
print('#### LISTS ####')
g.print_lists()

def sort(lst, func, title='LIST'):
    print('\t' + title, end='')
    print(lst)
    temp = lst[:]
    func(temp)
    print('\tResult:\t\t' + str(temp))
    print('\t-----------------------')

def sort_lists(func):
    print('EXPECTED:\t' + str(g.sorted_l), end='\n\n')
    if args.sorted:
        sort(g.sorted_l, func, 'SORTED:\t\t')
    if args.nearly:
        sort(g.nearly_l, func, 'NEARLY SORTED:\t')
    if args.reversed:
        sort(g.reversed_l, func, 'REVERSED:\t')
    if args.random:
        sort(g.random_l, func, 'RANDOM:\t\t')
    if args.few_unique:
        sort(g.few_unique_l, func, 'FEW UNIQUES:\t')

if args.insertion:
    print('\n#### INSERTION ####')
    sort_lists(s.insertion)

if args.selection:
    print('\n#### SELECTION ####')
    sort_lists(s.selection)
