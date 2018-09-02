import math


class Sorter(object):

    def insertion(self, seq):
        i = 1

        for i in range(len(seq)):

            # searching position on sorted part of the list
            for j in range(i, 0, -1):

                # found correct position -> stops swapping
                if seq[j - 1] <= seq[j]:
                    break

                # swapping elements
                seq[j], seq[j - 1] = seq[j - 1], seq[j]

    def selection(self, seq):

        for i in range(len(seq)):

            idxMin = i

            # searching for miminum
            for j in range(i + 1, len(seq)):
                if seq[j] < seq[idxMin]:
                    idxMin = j

            # swaps if current is not the minimum found
            if idxMin != i:
                seq[i], seq[idxMin] = seq[idxMin], seq[i]

    def merge(self, seq, verbose=False):
        if verbose:
            print('\tSplitting: ' + str(seq))

        if len(seq) > 1:
            middle = len(seq) // 2
            left, right = seq[:middle], seq[middle:]

            self.merge(left)
            self.merge(right)

            # Merging halves
            i, j, k = 0, 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    seq[k] = left[i]
                    i += 1
                else:
                    seq[k] = right[j]
                    j += 1
                k += 1

            # Adding remaining elements from each half
            while i < len(left):
                seq[k] = left[i]
                i, k = (i + 1), (k + 1)

            while j < len(right):
                seq[k] = right[j]
                j, k = (j + 1), (k + 1)

        if verbose:
            print('\tMerging: ' + str(seq))

    # QUICK METHODS: quick (caller), _quick_sort (recursive), _quick_partition and _median_pivot (optimizer)
    def quick(self, seq):
        self._quick_sort(seq, 0, len(seq) - 1)

    @staticmethod
    def _quick_sort(seq, lo, hi):
        if hi <= lo:
            return

        Sorter._median_pivot(seq, lo, hi)
        pivot = Sorter._quick_partition(seq, lo, hi)
        Sorter._quick_sort(seq, lo, pivot - 1)
        Sorter._quick_sort(seq, pivot + 1, hi)

    @staticmethod
    def _quick_partition(seq, lo, hi):
        i = lo + 1
        j = hi
        while True:

            while seq[i] <= seq[lo]:
                i += 1
                if i >= hi:
                    break

            while seq[j] > seq[lo]:
                j -= 1
                if j <= lo:
                    break

            if i >= j:
                break

            seq[i], seq[j] = seq[j], seq[i]

        seq[lo], seq[j] = seq[j], seq[lo]
        return j

    @staticmethod
    def _median_pivot(seq, lo, hi):
        mid = (lo + hi) // 2
        if seq[lo] > seq[mid]:
            seq[lo], seq[mid] = seq[mid], seq[lo]
        if seq[mid] > seq[hi]:
            seq[mid], seq[hi] = seq[hi], seq[mid]
        if seq[mid] > seq[lo]:
            seq[mid], seq[lo] = seq[lo], seq[mid]

    # COUNTING METHODS: counting and counting_in_place (less memory use)
    @staticmethod
    def counting(seq, max_val=None):
        if max_val is None:
            max_val = max(seq)

        count = [0] * (max_val + 1)

        for i in range(len(seq)):
            count[seq[i]] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        result = [0] * len(seq)
        for i in range(len(seq) - 1, -1, -1):
            result[count[seq[i]] - 1] = seq[i]
            count[seq[i]] -= 1

        for i in range(len(seq)):
            seq[i] = result[i]

    @staticmethod
    def counting_in_place(seq, max_val=None):
        if max_val is None:
            max_val = max(seq)

        count = [0] * (max_val + 1)

        for i in seq:
            count[i] += 1

        i = 0
        for j in range(max_val + 1):
            for c in range(count[j]):
                seq[i] = j
                i += 1

    # HEAP METHODS: _parent (not used), _left, _right, _max_heapify and heap
    def heap(self, seq):
        for i in range(len(seq)):
            heap_last_idx = len(seq) - 1 - i
            Sorter._max_heapify(seq, heap_last_idx)
            seq[0], seq[heap_last_idx] = seq[heap_last_idx], seq[0]

    @staticmethod
    def _parent(i):
        return math.ceil(i / 2) - 1

    @staticmethod
    def _left(i):
        return i * 2 + 1

    @staticmethod
    def _right(i):
        return i * 2 + 2

    @staticmethod
    def _max_heapify(seq, heap_last_idx):
        start_idx = Sorter._parent(heap_last_idx)
        for i in range(start_idx, -1, -1):
            L = Sorter._left(i)
            R = Sorter._right(i)
            max_val = i
            if L <= heap_last_idx and seq[L] > seq[max_val]:
                max_val = L
            if R <= heap_last_idx and seq[R] > seq[max_val]:
                max_val = R
            seq[i], seq[max_val] = seq[max_val], seq[i]


# TO DO
    # def bubble(self, seq):
    #     pass

    # def radix(self, seq):
    #     pass

    # def bucket(self, seq):
    #     pass
