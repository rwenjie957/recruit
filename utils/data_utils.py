import cv2
import numpy as np
from pathlib import Path
from PIL import ImageGrab
import json
import time


def load_dataset(path):
    path = Path(path)
    with open(path / 'member_database.json', 'r', encoding='utf-8') as f1:
        member_database = json.load(f1)
    with open(path / 'tag_database.json', 'r', encoding='utf-8') as f2:
        tag_database = json.load(f2)
    return member_database, tag_database


def read_img(file_path):        # 可读取中文路径
    # 以二进制模式读取文件
    with open(file_path, 'rb') as f:
        img_bytes = bytearray(f.read())
    img = cv2.imdecode(np.asarray(img_bytes, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    return img


# 加载所有识别模版
def load_templates(path):         # 'data/tags' 'data/others'
    path = Path(path)
    dataset = {}
    for i in path.iterdir():
        dataset[i.stem] = read_img(i)
    return dataset


# 截图并转换为cv2格式
def screenshot():
    img = ImageGrab.grab()
    img_cv = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2GRAY)
    return img_cv


def record_img():
    img = ImageGrab.grab()
    t = time.strftime('%H_%M_%S', time.localtime())
    img.save('recruit_history/' + t + '.jpeg')
    return t


if __name__ == '__main__':
    fp = Path('../data/others')
    import os
    os.chdir('..')
    record_img()
