# -*- coding:utf8 -*-


class Predict(object):

    THROW_COUNT = 6
    COIN_NUM = 3
    results = {
            0: 'old sun',
            1: 'young sun',
            2: 'young moon',
            3: 'old moon'
    }

    def __init__(self):
        self.result = []

    def throw_once(self):
        pass

    def start(self):
        for x in xrange(0, self.THROW_COUNT):
            self.throw_once()
        self.parse_result()

    def parse_result(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
