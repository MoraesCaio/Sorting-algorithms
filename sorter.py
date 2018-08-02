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
        if verbose: print('\tSplitting: ' + str(seq))
        
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

        if verbose: print('\tMerging: ' + str(seq))

    # TO DO
    # def bubble(self, seq):
    #     pass

    # def quick(self, seq):
    #     pass

    # def heap(self, seq):
    #     pass

    # def counting(self, seq):
    #     pass

    # def radix(self, seq):
    #     pass

    # def bucket(self, seq):
    #     pass
