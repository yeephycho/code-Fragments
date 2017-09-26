#! /usr/bin/env python
# -*- coding: UTF-8 -*-

'''
  Based on SO:
  https://stackoverflow.com/questions/19251993/comparing-two-directories-with-subdirectories-to-find-any-changes
'''

import os


def ls(path):
    all = []
    walked = os.walk(path)
    for base, sub_f, files in walked:
        for sub in sub_f:
            entry = os.path.join(base, sub)
            entry = entry[len(path):].strip('\\')
            all.append(entry)

        for file in files:
            entry = os.path.join(base, file)
            entry = entry[len(path):].strip('\\')
            all.append(entry)
    all.sort()
    return all


def folder_common(folder1_path, folder2_path):
    folder1_list = ls(folder1_path)
    folder2_list = ls(folder2_path)
    common = [item for item in folder1_list if item in folder2_list]
    # common.extend([item for item in folder2_list if item in folder1_list])
    return common


def folder_diff(folder1_path, folder2_path):
    folder1_list = ls(folder1_path)
    folder2_list = ls(folder2_path)
    diff = [item for item in folder1_list if item not in folder2_list]
    diff.extend([item for item in folder2_list if item not in folder1_list])
    return diff


# For MacOS
root = "/Users/huyixuan/Desktop"

# For Ubuntu
# root = "/home/yeephycho/Desktop"


path1 = os.path.join(root, "img")
path2 = os.path.join(root, "img2")
common_file = folder_common(path1, path2)
print(common_file)

diff_file = folder_diff(path1, path2)
print(diff_file)
