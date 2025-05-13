import itertools
import logging
import random


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# 所有组合可能出现的干员
def recruit(tag_data, tags_input):      # [tag1, tag2]
    result = {}
    for i in range(1, len(tags_input)+1):
        for j in itertools.combinations(tags_input, i):
            if '高级资深干员' in j:
                temp_set = set(tag_data['高级资深干员'][j[0]])
                for k in range(1, len(j)):
                    temp_set = temp_set.intersection(tag_data['高级资深干员'][j[k]])
                if temp_set:
                    result.update({j: temp_set})
            else:
                temp_set = set(tag_data['非高级资深干员'][j[0]])
                for k in range(1, len(j)):
                    temp_set = temp_set.intersection(tag_data['非高级资深干员'][j[k]])
                if temp_set:
                    result.update({j: temp_set})

    return result                       # {(tag1, tag2):{member1,member2,member3}}


# 为所有结果评分，返回最高等级的随机组合
def evaluate(member_data, result):
    ranks = {}
    max_rank = 1
    for k, v in result.items():
        point = 6
        for i in v:
            point = min(member_data[i]['rank'], point)
        ranks[k] = point
        max_rank = max(max_rank, point)

    choices = []
    for k, v in ranks.items():
        if v == max_rank:
            choices.append(k)
    logger.info(f'最可能出现星级：{max_rank}, 组合有{choices}')
    combination = random.choice(choices)
    logger.info(f'已随机选择{combination}')
    return combination                                      # (tag1, tag2)


if __name__ == '__main__':

    a = ['远程位', '输出', '先锋干员','高级资深干员']
    b = ['远程位', '重装干员', '医疗干员','术师干员','辅助干员']
    c = ['资深干员', '控场']
    from data_utils import load_dataset
    m, t = load_dataset('../data')
    r = recruit(t,c)
    print(r)
    print(evaluate(m, r))

