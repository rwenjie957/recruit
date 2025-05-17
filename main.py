# 运行窗口的分辨率固定为"1920x1080"

from utils.automation import *
from utils.data_utils import *

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(filename)s:%(message)s', datefmt='%m-%d %H:%M:%S')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('log.txt', mode='a', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

threshold = 0.8

# 加载数据
all_tags = load_templates('data/tags')
other_tags = load_templates('data/others')
member_dataset, tag_dataset = load_dataset('data')

# 立即招募
for i in range(1):
    start_recruit(other_tags, all_tags, member_dataset, tag_dataset, threshold)
    instant_recruit(other_tags, threshold, record=True)
    logger.info('本轮已全部招募完成，开始下一轮招募\n')
