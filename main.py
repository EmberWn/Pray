# -*- coding:utf8 -*-
import random
from Config import ParamConfig


class Predict(object):

    def __init__(self):
        self.result = []

    def throw_once(self):
        rand_num = random.randint(0, ParamConfig.RESULTS_COUNT - 1)
        if rand_num < ParamConfig.YINANDYANG:
            num = ParamConfig.YIN
        else:
            num = ParamConfig.YANG
        self.result.append(num)

    def start(self):
        for x in xrange(0, ParamConfig.THROW_COUNT):
            self.throw_once()
        self.parse_result()

    def parse_result(self):
        self.result.reverse()
        nums = []
        start = 0
        length = len(self.result)
        print self.result
        while True:
            end = start + ParamConfig.ONE_TRIGRAM_THROW_COUNT
            trigram = self.result[start: end]
            nums.append(self.calculate(trigram))
            start = end
            if start == length:
                break
        print nums
        self.output_result(nums)

    def calculate(self, trigram):
        num = 0
        for i in trigram:
            num = i + (num << 1)
        return num

    def output_result(self, nums):
        print ParamConfig.EightTrigrams[nums[0]], ParamConfig.EightTrigrams[nums[1]]


def main():
    pre = Predict()
    pre.start()


if __name__ == '__main__':
    main()
