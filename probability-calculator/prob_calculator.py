import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.balls = kwargs
        self.contents = []

        for color, quant in self.balls.items():
            for i in range(quant):
                self.contents.append(color)

    def draw(self, number):
        # Create a list with contents -> balls
        draw_items = []
        contents = self.contents
        if number >= len(contents):
            return self.contents

        else:
            for k in range(number):
                inter = random.randint(0, len(contents) - 1)
                draw_items.append(contents[inter])
                contents.pop(inter)

        return draw_items


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    bad_results = 0
    for i in range(num_experiments):
        exp_hat = copy.deepcopy(hat)
        balls = exp_hat.draw(num_balls_drawn)
        # check if the balls drawn are equal to expected balls // set -> eliminate repetition // transform to dict
        check_balls = copy.deepcopy(balls)
        check_balls = set(check_balls)
        check_balls = dict.fromkeys(check_balls, '')

        for color in check_balls:
            check_balls[color] = balls.count(color)
        # count bad results
        for color in expected_balls:
            if color in check_balls:
                if check_balls[color] < expected_balls[color]:
                    bad_results +=1
                    break

            else:
                bad_results +=1

    return 1 - (bad_results / num_experiments)
