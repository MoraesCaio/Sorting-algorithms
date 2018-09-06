from generator import Generator
from sorter import Sorter
import argparse
import inspect

parser = argparse.ArgumentParser()

# SETTINGS
parser.add_argument('-n', '--length', type=int, default=10, help='Number of elements. Minimum = 2')
parser.add_argument('-m', '--min', type=int, default=0, help='Minimum value possible for elements. Default = 0')
parser.add_argument('-M', '--max', type=int, default=100, help='Maximum value possible for elements. Default = 100')
parser.add_argument('--swaps', type=int, default=4, help='Number of swaps made on "nearly sorted" list generation.\n' +
                                                         'For verbose, use a negative value.')
parser.add_argument('--uniques', type=int, default=5, help='Number of unique values on "few uniques" list.\n' +
                                                           'For verbose, use a negative value.')
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
parser.add_argument('-ms', '--merge', action='store_true', help='Calls MERGE sort.')
parser.add_argument('-msv', '--merge-verbose', action='store_true', help='Calls Verbose MERGE sort.')
parser.add_argument('-qs', '--quick', action='store_true', help='Calls QUICK sort.')
parser.add_argument('-cs', '--counting', action='store_true', help='Calls COUNTING sort in place.')
parser.add_argument('-csnip', '--counting-not-in-place', action='store_true', help='Calls COUNTING sort NOT in place.')
parser.add_argument('-hs', '--heap', action='store_true', help='Calls HEAP sort.')


args, _ = parser.parse_known_args()


def decorate_sort_class(cls):
    for name, method in inspect.getmembers(cls, inspect.ismethod):
        # avoids 'private' methods
        if not name.startswith('_'):
            setattr(cls, name, decorator_output_sort(method))
    return cls


def decorator_output_sort(func):
    def wrapper(*args, list_dict=None, **kwargs):
        temp_copy = list_dict['list'][:]
        wrapped_func = func(temp_copy, *args, **kwargs)
        print('\t' + list_dict['title'] + str(list_dict['list']))

        expected_result = sorted(g.few_unique_l) if list_dict['expected_few_unique'] else g.sorted_l

        print('\tList is sorted? ' + str(temp_copy == expected_result))
        print('\tResult:\t\t' + str(temp_copy))
        print('\t-----------------------')
        print('\tEXPECTED:\t' + str(expected_result), end='\n\n')
        return wrapped_func
    return wrapper


g = Generator()
s = decorate_sort_class(Sorter())
g.generate(args.length, args.min, args.max, args.uniques, args.swaps, args.seed)

# LISTS list_dict=[{'list': [integersList], 'title': titleStr, 'expected_few_unique': bool}]
list_dicts = []

if args.sorted:
    list_dicts.append({'list': g.sorted_l, 'title': 'SORTED:\t\t', 'expected_few_unique': False})

if args.nearly:
    list_dicts.append({'list': g.nearly_l, 'title': 'NEARLY SORTED:\t', 'expected_few_unique': False})

if args.reversed:
    list_dicts.append({'list': g.reversed_l, 'title': 'REVERSED:\t', 'expected_few_unique': False})

if args.random:
    list_dicts.append({'list': g.random_l, 'title': 'RANDOM:\t\t', 'expected_few_unique': False})

if args.few_unique:
    list_dicts.append({'list': g.few_unique_l, 'title': 'FEW UNIQUES:\t', 'expected_few_unique': True})


print('#### LISTS ####')
g.print_lists()


if args.insertion:
    print('\n#### INSERTION ####')
    for lst in list_dicts:
        s.insertion(list_dict=lst)

if args.selection:
    print('\n#### SELECTION ####')
    for lst in list_dicts:
        s.selection(list_dict=lst)

if args.merge or args.merge_verbose:
    print('\n#### MERGE ####')
    for lst in list_dicts:
        s.merge(list_dict=lst, verbose=args.merge_verbose)

if args.quick:
    print('\n#### QUICK ####')
    for lst in list_dicts:
        s.quick(list_dict=lst)

if args.counting or args.counting_not_in_place:
    print('\n#### COUNTING ####')
    for lst in list_dicts:
        s.counting(list_dict=lst, in_place=args.counting)

if args.heap:
    print('\n#### HEAP ####')
    for lst in list_dicts:
        s.heap(list_dict=lst)

# TO DO
# if args.bubble:
#     print('\n#### BUBBLE ####')
#     sort_lists(s.bubble)

# if args.radix:
#     print('\n#### RADIX ####')
#     sort_lists(s.radix)

# if args.bucket:
#     print('\n#### BUCKET ####')
#     sort_lists(s.bucket)
