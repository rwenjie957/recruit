import pyautogui as gui
from time import sleep

from recruit import *
from recognize import *
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def instant_recruit(others, threshold=0.8):
    for i in range(4):
        max_val, max_loc = locate(others['立即招募'], threshold)
        logger.debug(f'定位立刻招募：{max_val},{max_loc}')
        if max_val:
            gui.click(max_loc)
            sleep(1)
            max_val, max_loc = locate(others['confirm1'], threshold)
            logger.debug(f'定位确认:{max_val},{max_loc}')
            gui.click(max_loc)
            sleep(1)
        else:
            break

    for i in range(4):
        logger.info(f'正在第{i+1}轮聘用')
        max_val, max_loc = locate(others['recruit'], threshold)
        logger.debug(f'定位“立刻招募”:{max_val},{max_loc}')
        if max_val:
            gui.click(max_loc)
            sleep(1)
        else:
            break
        max_val, max_loc = locate(others['skip'], threshold)
        logger.debug(f'定位“skip”:{max_val},{max_loc}')
        gui.click(max_loc)
        sleep(3)
        gui.click(max_loc)
        sleep(1)


def start_recruit(others, tags, member_database, tag_database, threshold=0.8):
    for i in range(4):
        max_val, max_loc = locate(others['start'], threshold)
        logger.debug(f'定位空缺招募位:{max_val},{max_loc}')
        if max_val:
            gui.click(max_loc)
            sleep(1)
            logger.info(f'开始第{i+1}轮招募')

            results_recognized = recognize_tag(tags)                     # 识别的所有标签和位置{'近卫干员':(100,200)}
            logger.debug(f'识别到的标签及位置:{results_recognized}')

            tags_recognized = [i for i in results_recognized.keys()]
            logger.debug(f'识别到的标签有:{tags_recognized}')

            valid_results = recruit(tag_database, tags_recognized)
            logger.debug(f'所有有效组合{valid_results}')
            combinations = evaluate(member_database, valid_results)

            for t in combinations:
                gui.click(results_recognized[t][1])
                sleep(1)

            max_val, max_loc = locate(others['down'], threshold)
            logger.debug(f'识别“时间调整”:{max_val},{max_loc}')
            gui.click(max_loc)
            max_val, max_loc = locate(others['confirm'], threshold)
            logger.debug(f'识别“确认招募”:{max_val},{max_loc}')
            gui.click(max_loc)
            sleep(1)
        else:
            return


if __name__ == '__main__':
    from data_utils import *
    o = load_templates('../data/others')
    t = load_templates('../data/tags')
    md, td = load_dataset('../data')
    start_recruit(o, t, md, td)
    instant_recruit(o)
