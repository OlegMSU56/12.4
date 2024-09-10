import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# first = Runner('Вася', 100)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)
#
# t = Tournament(100, first, second, third)
# print(t.start())

logging.basicConfig(level=logging.INFO,
                        filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(levelname)s | %(message)s')
class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            runner = Runner('af', -50)
        except ValueError as VE:
            logging.warning(f'Неверная скорость для Runner. ValueError: {VE}')
        else:
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')


    def test_run(self):
        try:
            runner = Runner(123)
        except TypeError as TE:
            logging.warning(f'Неверный тип данных для объекта Runner. TypeError: {TE}')
        else:
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')


    def test_challenge(self):
        runner_1 = Runner('Katie')
        runner_2 = Runner('Maggie')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)



if __name__ == '__main__':
    unittest.main()

