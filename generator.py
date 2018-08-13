from random import randint, sample, choice, seed


class Generator(object):

    random_l = []
    sorted_l = []
    nearly_l = []
    swapped_els = []
    reversed_l = []
    unique_vals = []
    few_unique_l = []

    def generate(self, n, min_v, max_v, n_uniques, n_swaps, rnd_seed=None):
        if n < 1 or type(n) is not int:
            raise ValueError('Invalid value for n, it must be an integer greater than 1.')

        seed(rnd_seed)
        self.random_l = [randint(min_v, max_v) for i in range(0, n)]
        self.sorted_l = sorted(self.random_l)
        self.reversed_l = self. sorted_l[::-1]

        self.unique_vals = sample(set(self.sorted_l), abs(n_uniques))
        if n_uniques < 0:
            print('\nUNIQUE VALUES\n\t' + str(self.unique_vals), end='\n\n')
        self.few_unique_l = [choice(self.unique_vals) for i in range(0, n)]

        self.nearly_l = self._nearly_sorted(self.sorted_l, abs(n_swaps), (n_swaps < 0))

    def _nearly_sorted(self, sorted_l, n_swaps, verbose=False):
        nearly_l = sorted_l[:]  # shallow copy of sorted_l
        idx_l = range(len(nearly_l))
        half = len(idx_l) // 2

        # first_half_sample and second_half_sample
        f_h_sample = sample(idx_l[:half], n_swaps)
        s_h_sample = sample(idx_l[half:], n_swaps)

        if verbose:
            print('INDEXES OF SWAPPED ELEMENTS')
            print('\t' + str(f_h_sample) + ' -> ' + str(s_h_sample))

        for i in range(n_swaps):
            nearly_l[f_h_sample[i]], nearly_l[s_h_sample[i]] = nearly_l[s_h_sample[i]], nearly_l[f_h_sample[i]]
            self.swapped_els.append((nearly_l[f_h_sample[i]], nearly_l[s_h_sample[i]]))
            if verbose:
                print('\tSwapped ' + str(nearly_l[f_h_sample[i]]) + ' by ' + str(nearly_l[s_h_sample[i]]) + '.')
        print()

        return nearly_l

    def print_lists(self):
        print('\tRandom:\t\t', end='')
        print(self.random_l)
        print('\tSorted:\t\t', end='')
        print(self.sorted_l)
        print('\tNearly sorted:\t', end='')
        print(self.nearly_l)
        print('\tReversed:\t', end='')
        print(self.reversed_l)
        print('\tFew uniques:\t', end='')
        print(self.few_unique_l)
