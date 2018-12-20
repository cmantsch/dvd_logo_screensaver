class DvdLogo:
    def __init__(self, position=(0, 0), canvas_size=(1280, 720), image_size=(200, 200), speed_vector=(1, 1)):
        self.pos = position
        self.min = [0, 0]
        self.max = [canvas_size[0] - image_size[0], canvas_size[1] - image_size[1]]
        self.speed = speed_vector
        # set inverter of x or y to -1 to move in other direction
        self.inverters = [1, 1]

    def get_next_position(self):
        self.pos = [self.pos[0] + self.speed[0] * self.inverters[0], self.pos[1] + self.speed[1] * self.inverters[1]]
        # check for x on maximum or minimum position
        if self.pos[0] == self.max[0] or self.pos[0] == self.min[0]:
            # flip x inverter
            self.inverters[0] *= -1
        # check for y on maximum or minimum position
        if self.pos[1] == self.max[1] or self.pos[1] == self.min[1]:
            self.inverters[1] *= -1

        return self.pos