class FixedSizeFIFO:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0

#заполнение буфера
    def push(self, value):
        if self.is_full():
            raise ValueError("Буфер заполнен")
        else:
            self.buffer[self.tail] = value
            self.tail = self.tail + 1

#вывод буфера
    def pop(self):
        if self.is_empty():
            raise ValueError("Буфер пуст")
        else:
            value = self.buffer[self.head]
            self.buffer[self.head] = None
            self.head = self.head + 1
            return value

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.size == self.tail