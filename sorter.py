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
