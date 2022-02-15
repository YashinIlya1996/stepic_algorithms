class MyBinaryHeap:
    """При обращении к элементу по индексу нумерация считется с 1"""

    def __init__(self, lst=None, maxheap=False):
        if lst is None:
            lst = list()
        self.heap = heapifying(lst)
        self.max = not maxheap

    def get(self, ind):
        """Возвращает элемент по индексу, учитывая, что нумерация с 1"""
        return self.heap[ind - 1] if ind <= len(self.heap) else None

    def get_parent(self, ind):
        """возвращает индекс родителя"""
        return ind // 2 if ind != 1 else None

    def get_child(self, ind):
        """возвращает индексы детей"""
        n = len(self.heap)
        ch1 = 2 * ind if 2 * ind <= n else None
        ch2 = 2 * ind + 1 if 2 * ind + 1 <= n else None
        return ch1, ch2

    def sift_up(self, ind):
        p_ind = self.get_parent(ind)
        if p_ind:
            func = max if self.max else min
            if self.get(ind) == func(self.get(ind), self.get(p_ind)):
                return
            else:
                self._swap(ind, p_ind)
                self.sift_up(p_ind)

    def sift_down(self, ind):
        ch1_ind, ch2_ind = self.get_child(ind)
        if not ch1_ind:
            return
        elif not ch2_ind:
            func = min if self.max else max
            if self.get(ch1_ind) == func(self.get(ch1_ind), self.get(ind)):
                self._swap(ind, ch1_ind)
            return
        else:
            func = min if self.max else max
            if not (self.get(ind) == func(self.get(ch1_ind), self.get(ind), self.get(ch2_ind))):
                ch_ind = ch2_ind if func(self.get(ch1_ind), self.get(ch2_ind)) == self.get(ch2_ind) else ch1_ind
                self._swap(ind, ch_ind)
                self.sift_down(ch_ind)

    def insert(self, n):
        self.heap.append(n)
        self.sift_up(len(self.heap))

    def pop_root(self):
        """ Возвращает корень и удаляет его из кучи"""
        if len(self.heap) == 1:
            root = self.heap.pop()
        else:
            self._swap(1, len(self.heap))
            root = self.heap.pop()
            self.sift_down(1)
        return root

    def _swap(self, ind1, ind2):
        self.heap[ind1 - 1], self.heap[ind2 - 1] = self.heap[ind2 - 1], self.heap[ind1 - 1]

    def __repr__(self):
        return self.heap.__repr__()

    def heapifying(self, lst: list):
        self.heap = lst
        for i in range(len(lst) // 2, 0, -1):
            self.sift_down(i)
        return self.heap
