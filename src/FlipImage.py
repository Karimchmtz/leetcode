class Solution(object):
    def reverseArray(self, array):
        i = 0
        while (i < len(array) / 2):
            tmp = array[i]
            array[i] = array[len(array) - 1 - i]
            array[len(array) - 1 - i] = tmp
            i += 1
        return array

    def flipAndInvertImage(self, image):
        i = 0
        while (i < len(image)):
            row = image[i]
            row = Solution.reverseArray(self, row)
            j = 0
            while (j < len(row)):
                if (row[j] == 1):
                    row[j] = 0
                else:
                    row[j] = 1
                j += 1
            image[i] = row
            i += 1
        return image