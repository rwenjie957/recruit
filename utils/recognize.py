# 进行图像识别和定位
# 需要固定窗口分辨率为1920x1080
from data_utils import *
import cv2
from pathlib import Path


# 以template为模板，匹配image位置
def match(image, template):
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_val, max_loc                 # 返回最大准确度和对应的位置（左上角）


# 从截图中识别所有超过阈值的标签，返回准确度和中心位置
def recognize_tag(dataset, threshold=0.95):
    results = {}
    screen = screenshot()

    for k, v in dataset.items():
        max_val, max_loc = match(screen, v)
        if max_val > threshold:
            h, w = v.shape
            results[k] = (max_val, (max_loc[0] + w/2, max_loc[1] + h/2))

    return results


# 识别模版，返回精准度和位置
def locate(template, threshold):
    screen = screenshot()
    max_val, max_loc = match(screen, template)
    if max_val > threshold:
        h, w = template.shape
        return max_val, (max_loc[0] + w/2, max_loc[1] + h/2)
    else:
        return None, None


if __name__ == '__main__':
    # print(match('../data/default.jpeg', '../data/公开招募.jpeg'))
    ts = load_templates(Path('../data/tags'))
    other = load_templates(Path('../data/others'))

    ttt = recognize_tag(ts)
    print(ttt)