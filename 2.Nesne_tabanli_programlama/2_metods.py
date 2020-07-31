class Square(object):

    edge = 5  # metre
    area = 0

    # bu bir method'dur
    def area1(self):
        self.area = self.edge * self.edge
        print('Area: ', self.area)


s1 = Square()
s1.edge = 7
s1.area1()
