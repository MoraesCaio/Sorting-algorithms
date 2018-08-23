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

    def quick(self, seq):
        self._quick_sort(seq, 0, len(seq) - 1)

    def _quick_sort(self, seq, lo, hi):
        if hi <= lo:
            return

        Sorter._median_pivot(seq, lo, hi)
        pivot = Sorter._quick_partition(seq, lo, hi)
        self._quick_sort(seq, lo, pivot - 1)
        self._quick_sort(seq, pivot + 1, hi)

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

    def _test_median_pivot(self):
        a = [[2, 1, 3], [2, 3, 1], [1, 2, 3], [3, 2, 1], [1, 3, 2], [3, 1, 2]]
        for i in a:
            self._median_pivot(i, 0, 2)
        print(a)

    @staticmethod
    def counting(seq, max_val=None):
        if max_val is None:
            max_val = seq[0]
            for i in range(1, len(seq)):
                if seq[i] > max_val:
                    max_val = seq[i]

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
            max_val = seq[0]
            for i in range(1, len(seq)):
                if seq[i] > max_val:
                    max_val = seq[i]

        count = [0] * (max_val + 1)

        for i in seq:
            count[i] += 1

        i = 0
        for j in range(max_val + 1):
            for c in range(count[j]):
                seq[i] = j
                i += 1

# TO DO
    # def bubble(self, seq):
    #     pass

    # def heap(self, seq):
    #     pass

    # def counting(self, seq):
    #     pass

    # def radix(self, seq):
    #     pass

    # def bucket(self, seq):
    #     pass
