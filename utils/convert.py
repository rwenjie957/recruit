# 数据库转换，将干员数据转换成标签数据


def convert(member_data, ignore_low_rank=True):
    tag_data = {'高级资深干员':{'高级资深干员':[]}, '非高级资深干员':{'资深干员':[]}}
    if ignore_low_rank:
        min_rank = 3
    else:
        min_rank = 1
    for k,v in member_data.items():
        if min_rank <= v['rank'] <=5:
            for i in v['tags']:
                tag_data['非高级资深干员'][i] = tag_data['非高级资深干员'].get(i, []) + [k]
            if v['rank'] == 5:
                tag_data['非高级资深干员']['资深干员'] += [k]

        else:
            tag_data['高级资深干员']['高级资深干员'] += [k]
            for i in v['tags']:
                tag_data['高级资深干员'][i] = tag_data['高级资深干员'].get(i, []) + [k]

    return tag_data


if __name__ == '__main__':
    import json
    with open('../data/member_database.json', 'r', encoding='utf-8') as j:
        js = json.load(j)
    tags = convert(js)
    with open('../data/tag_database.json', 'w', encoding='utf-8') as f:
        json.dump(tags, f, ensure_ascii=False, indent=4)