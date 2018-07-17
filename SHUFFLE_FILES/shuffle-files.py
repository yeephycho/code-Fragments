import os
import sys
import copy
import random
import shutil
import numpy as np


SRC_ROOT = "/media/yeephycho/My Passport/Normal_patch"
# SRC_ROOT = "/home/yeephycho/Projects/cv_pathology/dataset/600-normal-"
# SRC_ROOT = "/media/yeephycho/New Volume/trainingSetV9-4/0_NORMAL"
DST_ROOT = "/media/yeephycho/New Volume/NORMAL_600"


def main(arguments):
    filenames = os.listdir(SRC_ROOT)
    shuffle_list = copy.deepcopy(filenames)
    random.shuffle(shuffle_list)
    # for i in range(10):
    #     print(filenames[i])
    #     print(shuffle_list[i])
    for i in range(6000):
        src_path = os.path.join(SRC_ROOT, shuffle_list[i])
        dst_path = os.path.join(DST_ROOT, shuffle_list[i])
        shutil.copy(src_path, dst_path)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
