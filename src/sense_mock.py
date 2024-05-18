class SenseMock:
    def __init__(self):
        self.led_matrix = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]

    def set_pixels(self, pixels):
        if len(pixels) != 64:
            raise ValueError("pixels list must have 64 elements")

        pixels.reverse()
        for i, color in enumerate(pixels):
            x = i % 8
            y = i // 8
            self.led_matrix[y][x] = color

        self.print_led_matrix()

    def clear(self, colour=(0, 0, 0)):
        self.led_matrix = [[colour for _ in range(8)] for _ in range(8)]

    def print_led_matrix(self):
        for row in self.led_matrix:
            for colour in row:
                r, g, b = colour
                print(f"\033[38;2;{r};{g};{b}m0\033[0m", end="")
            print()
