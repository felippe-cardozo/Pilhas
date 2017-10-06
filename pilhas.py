class Pilhas:

    def __init__(self, value=None):
        if value:
            if isinstance(value, int):
                self.objects = [value]
                self.mins = [value]
                self.size = 0
            else:
                raise Exception("Integers only")
        else:
            self.objects = []
            self.size = 0

    def push(self, value):
        if not isinstance(value, int):
            raise Exception("Integers only")
        if not self.objects:
            self.objects = [value]
            self.mins = [value]
        else:
            self.objects.append(value)
            self.size += 1
            if value < self.mins[0]:
                self.mins.append(value)
            else:
                self.mins.append(self.mins[0])

    def pop(self):
        if not self.objects:
            raise Exception("There is Nothing to pop")
        removed = self.objects[self.size]
        self.objects = self.objects[:self.size]
        self.mins = self.mins[:self.size]
        self.size -= 1
        return removed

    def min(self):
        if not self.objects:
            raise Exception("List is Empty")
        return self.mins[self.size]
