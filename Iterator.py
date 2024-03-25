class Family:
    def __init__(self):
        self.dad = "Вадим"
        self.mom = "Татьяна"
        self.son = "Алексей"
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i == 1:
            return f"Папа - {self.dad}"
        if self.i == 2:
            return f"Мама - {self.mom}"
        if self.i == 3:
            return f"Я - {self.son}"
        if self.i == 4:
            return "Счастливая семья :)"

        raise StopIteration()

my_family = Family()
print(my_family)
for vale in my_family:
    print(vale)