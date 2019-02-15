"""
一维,二维,多维数组的实现 array(定长)
1. 一个工程的设计其实就是从低维到高维的创建
2. 事情往往不需"考虑的很复杂", 都是依据基础的东西构建
"""
import ctypes


class Array:
    """
    ADT实现一维数组
    """

    def __init__(self, size):
        assert size > 0, 'array size must be > 0'
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __getitem__(self, index):
        assert 0 <= index <= len(self._elements), 'index must be in range 0 < index < {}'.format(len(self._elements))
        return self._elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index <= len(self._elements), 'index must be in range 0 < index < {}'.format(len(self._elements))
        self._elements[index] = value

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        return _ArrayIterator(self._elements)

    def clear(self, value):
        for i in range(len(self._elements)):
            self._elements[i] = value


class _ArrayIterator:
    """
    数组的迭代器实现
    """

    def __init__(self, items):
        self._items = items
        self.cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < len(self._items):
            val = self._items[self.cursor]
            self.cursor += 1
            return val
        else:
            raise StopIteration


class Array2d:
    """
    依据一维数组构建二维数组, 即数组中嵌套数组, 这里不用考虑二维数组的迭代实现, 这跟一维数组的迭代没有什么不一样。
    """

    def __init__(self, numrows, numcols):
        assert numrows > 0, 'row must be > 0'
        assert numcols > 0, 'col must be > 0'
        self._the_rows = Array(numrows)
        for i in range(len(self._the_rows)):
            self._the_rows[i] = Array(numcols)

    @property
    def numRows(self):
        return len(self._the_rows)

    @property
    def numCols(self):
        return len(self._the_rows[0])

    def clear(self, value):
        for row in self._the_rows:
            row.clear(value)

    def __getitem__(self, item):  # item(x, y)
        assert len(item) == 2
        row, col = item[0], item[1]
        assert 0 <= row <= len(self._the_rows) and 0 <= col <= len(self._the_rows[0])
        the_1d_array = self._the_rows[row]
        return the_1d_array[col]

    def __setitem__(self, item, value):
        assert len(item) == 2
        row, col = item[0], item[1]
        assert 0 <= row <= len(self._the_rows) and 0 <= col <= len(self._the_rows[0])
        the_1d_array = self._the_rows[row]
        the_1d_array[col] = value


class MartixArray:
    """
    多维数组
    scaleBy:
    add 矩阵相加
    transpose 矩阵转置
    """

    def __init__(self, numrow, numcol):
        self._theGird = Array2d(numrow, numcol)
        self._theGird.clear(0)

    @property
    def numRows(self):
        return self._theGird.numRows

    @property
    def numCols(self):
        return self._theGird.numCols

    def __getitem__(self, item):
        return self._theGird[item[0], item[1]]

    def __setitem__(self, item, value):
        self._theGird[item[0], item[1]] = value

    def scaleBy(self, scalar):
        for r in range(self.numRows):
            for c in range(self.numCols):
                self[r, c] *= scalar

    def transpose(self):
        newMartix = MartixArray(self.numCols, self.numRows)
        for r in range(self.numRows):
            for c in range(self.numCols):
                newMartix[c, r] = self[r, c]
        return newMartix

    def __add__(self, rhxMartix):
        assert (rhxMartix.numRows == self.numRows and rhxMartix.numCols == self.numCols)
        newMartix = MartixArray(rhxMartix.numRows, rhxMartix.numCols)
        for r in range(self.numRows):
            for c in range(self.numCols):
                newMartix[r, c] = self[r, c] + rhxMartix[r, c]


if __name__ == "__main__":
    array1d = Array(5)
    array1d[0] = 0
    array1d[1] = 1
    array1d[2] = 2
    array1d[3] = 3
    array1d[4] = 4
    print(array1d[1])

    array2d = Array2d(3, 4)
    array2d[1, 2] = 4
    print(array2d)

    martixArray = MartixArray(4, 5)
    martixArray[1, 2] = 1
    t_array = martixArray.transpose()