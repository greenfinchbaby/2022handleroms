import os
import json
import shutil
from json import JSONDecodeError

import jsonpath as jsonpath

from RetailsList import RetailsList
from collections import Counter  # 引入Counter

WORK_PATH = "i:/"
#WORK_PATH = "e:/temp/"
SUCCESS = 1
FAIL = 0
play_list_name = "playlists/"
playlistsPath = WORK_PATH + play_list_name


# 遍历目录，获取路径下所有文件
def get_file_lists(filepath=playlistsPath):
    for parent, dir_names, filenames in os.walk(filepath):
        # Case1: traversal the directories
        for dir_name in dir_names:
            print("Parent folder:", parent)
            print("Dirname:", dir_name)
        # Case2: traversal the files
        for filename in filenames:
            print("Parent folder:", parent)
            print("Filename:", filename)
    file_paths = append_path_to_filename(filenames)
    return file_paths


# 给当前文件名列表加上路径
def append_path_to_filename(names):
    # 对原列表进行遍历
    new_names = []
    while names:
        # 对每一个列表元素进行出栈操作，并在前面添加字符串，并保存在当前变量中
        current_name = playlistsPath + names.pop()
        # 把当前变量保存在新列表中
        new_names.append(current_name)

    return new_names  # 返回新列表


# 打开单个lpl文件查找重复首字段内容
def find_repeat_in_lpl_file(filepath=playlistsPath + "MAME.lpl"):
    try:
        json_lists = get_json_lists(filepath)
        filename_lists = []  # 重复的文件名列表
        repeat_directory = get_repeat_list_and_count(filename_lists, json_lists)
        # print(filename_lists) #重复文件列表
    except FileNotFoundError:
        print('无法打开指定的文件!')
        return None
    except LookupError:
        print('指定了未知的编码!')
        return None
    except JSONDecodeError:
        print("%s文件格式不正确" % filepath)
        return None
    else:
        return repeat_directory
    # json.loads(string)['code']取code值的方法
    # for key in pure_load_f:
    #  print('======key========:' + key + "************value******" + key)


# 获取无前缀json如果第二个参数为 1 'fulllist'则输出完整json，否则输出为item:下面的json
def get_json_lists(filepath=playlistsPath + "MAME.lpl", *json_type):
    full_json_lists = open_file_get_pure_json(filepath)
    # json_lists = json.loads(pure_lists)
    pure_lists = del_from_n_to_end_return_item_json(full_json_lists)
    for varib in json_type:
        if varib == 1:
            return full_json_lists
    else:
        return pure_lists


# 获取重复文件名和重复的数量
def get_repeat_list_and_count(filename_lists, json_lists):
    for dict_list in json_lists:
        # print(dict_list)  # 显示每条列表可随时注释
        # 生成一个RetailsList类的实例
        retails_list = RetailsList(dict_list)
        #path = retails_list.get_path()
        filename = retails_list.get_filename()
        filename_lists.append(filename)
    repeat_directory = find_repeat_name_in_lists(filename_lists)
    # print(dict_list.get('path'))
    return repeat_directory


# 通过名字列表获得

# 找出列表list中的重复元素
def find_repeat_name_in_lists(lists):
    b = dict(Counter(lists))
    # repeat_list =[key for key,value in b.items()if value > 1]
    get_filename_count = b.items()
    repeat_dictionary = {key: value for key, value in get_filename_count if value > 1}
    # print (repeat_list)  #只展示重复元素
    # print (repeat_dictionary)  #展现重复元素和重复次数
    return repeat_dictionary


# 打开文件去掉前面不需要信息，获取纯内容
def open_file_get_pure_json(file_path, *json_type):  # 返回的json类型1，
    try:
        with open(file_path, 'rb') as load_f:
            load_dict = json.load(load_f)
    except FileNotFoundError:
        print('无法打开指定的文件!')
        return None
    except LookupError:
        print('指定了未知的编码!')
        return None
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
        load_f.close()
        return None
    else:

        load_f.close()
        return load_dict


# 截取掉前面多余部分{'version': '1.4', 'default_core_path': '', 'default_core_name': '', 'label_display_mode': 0,
# 'right_thumbnail_mode': 0, 'left_thumbnail_mode': 0, 'sort_mode': 0, 'items':
def del_from_n_to_end_return_item_json(input_jason):
    # jason文件转为字符串
    sub_input_string = jsonpath.jsonpath(input_jason, '$..{key_name}'.format(key_name='items'))
    for return_jason in sub_input_string:  # sub_input_string为二维列表，进行降维处理
        ret_json = return_jason
    return ret_json


# add rom filename to item in json_lists 这个方法没有用
def add_rom_name_to_json_lists(json_lists):
    add_rom_names_dict_lists = []
    for dict_list in json_lists:
        retails_list = RetailsList(dict_list)
        added_rom_name_dict = retails_list.get_dict_with_rom_name()
        add_rom_names_dict_lists.append(added_rom_name_dict)

    return add_rom_names_dict_lists


# 输入('s1945.zip') 给出重复列表
def get_repeat_paths_by_rom_name(rom_name, json_lists=get_json_lists()):
    output_repeat_paths = []
    add_rom_names_dict_lists = add_rom_name_to_json_lists(json_lists)
    for dict_list in add_rom_names_dict_lists:
        if dict_list['rom_name'] == rom_name:
            output_repeat_paths.append(dict_list['path'])
    return output_repeat_paths


# Move file to temp dir
def move_delete_rom_to_temp_dir(filepath, makedir='filetodelete'):
    if not os.path.exists(filepath):  # 不是绝对路径
        filepath = WORK_PATH[:-1] + filepath
    if not os.path.exists(filepath):  # 是绝对路径还找不到出错
        print("所提供路径{0}没有文件！".format(filepath))
        return FAIL
    file_to_delete_path = WORK_PATH + makedir
    if not os.path.exists(file_to_delete_path):
        os.mkdir(file_to_delete_path)
    # 在file to delete path   下存在文件就直接删除
    del_full_path_with_filename = file_to_delete_path + '/' + os.path.basename(filepath)
    if os.path.isfile(del_full_path_with_filename):  # 已经存在文件
        os.remove(filepath)
        print("Success, 在{1}目录已经存在文件，{0}删除成功！".format(filepath, file_to_delete_path))
    else:
        shutil.move(filepath, file_to_delete_path)
        print("Success, 移动文件{0}   到  {1}成功！".format(filepath, file_to_delete_path))
    return SUCCESS


#  保留重复列表的第一个元素从第二个元素开始删除
def move_dup_roms_to_temp_dir(dir_to_delete='', repeat_paths_by_rom_name=[]):
    if dir_to_delete == '':
        dir_to_delete = 'filetodelete'
    count = 0
    successed = 0
    for rom_repeat_pairs in repeat_paths_by_rom_name:
        for i in range(1, len(rom_repeat_pairs)):  # 保留重复列表的第一个元素从第二个元素开始删除
            # file_path_name_to_del
            # print(i, rom_repeat_pairs[i])
            count = count + move_delete_rom_to_temp_dir(rom_repeat_pairs[i], dir_to_delete)
            successed = successed + 1
    print('\n等待删除的文件移动到了{0}目录，共{2}个文件在重复列表中，移动成功了{1}个文件。'.format(dir_to_delete, count, successed))


# 备份当前lpl文件
def bak_file(bak_file_path):
    dir_name = os.path.dirname(bak_file_path)
    if os.path.exists(bak_file_path) is False:
        print("没有此文件！")
        return FAIL
    copy_filename = bak_file_path + '.bak'
    copy_file_path = copy_filename
    if not os.path.exists(copy_file_path):
        shutil.copyfile(bak_file_path, copy_file_path)  # oldfile和newfile都只能是文件
        print("备份文件{0}成功".format(copy_file_path))
    else:
        print("备份文件{0}已经存在".format(copy_file_path))
    return SUCCESS


# 给定json文件，和重复文件路径返回json
def del_dup_lists_in_pure_json(jason_lists, repeat_paths, start=0):
    deleted_json = []
    for each_dict_list in jason_lists:
        if each_dict_list['path'] not in repeat_paths[start:]:  # 从删除列表start开始删除
            deleted_json.append(each_dict_list)
    return deleted_json


# writing

# ["/ROM/MAME/003/s1945.zip", "/roms/s1945.zip"]列表中的所有文件为待删除文件名
# 输入为：[['/ROM/MAME/001/gunbird.zip', '/rom/MAME/Gun Bird 1/gunbird.zip'], ['/ROM/MAME/003/s1945.zip', '/roms/s1945.zip', '/rom/MAME/Strikers 1945/s1945.zip']
def chang_to_del_names(repeat_paths_by_rom_name):
    to_del_names = []
    for rom_repeat_pairs in repeat_paths_by_rom_name:
        for i in range(1, len(rom_repeat_pairs)):  # 保留重复列表的第一个元素从第二个元素开始删除
            to_del_names.append(rom_repeat_pairs[i])
    return to_del_names


def update_item_into_jason(input_json, item_value):
    input_json['items'] = item_value
    return input_json


def write_json_data(dict_input, json_path):
    # 写入json文件
    try:
        with open(json_path, 'w', encoding='utf-8') as r:
            # 定义为写模式，名称定义为r

            json.dump(dict_input, r, ensure_ascii=False, indent=1)
            # 将dict写入名称为r的文件中
    except IOError as error:
        print(f"出现写入文件异常！：{error}")
        r.close()
        # 关闭json写模式
    print('保存数据完成!')


#   列表中的路径同第一个路径重复，则去掉相应路径，如果只存在一个列表则去掉该第一个路径
def filter_need_to_delete_file(repeat_paths_by_rom_name):
    filtered_repeat_paths = []

    for rom_repeat_paths in repeat_paths_by_rom_name:
        a_list_repeat_paths = []
        for a_file_name in rom_repeat_paths:
            if a_file_name not in a_list_repeat_paths:
                a_list_repeat_paths.append(a_file_name)
            else:
                print(f"同{[a_file_name]}重名，去除该名无需删除rom文件！")
        if len(a_list_repeat_paths) != 1:
            filtered_repeat_paths.append(a_list_repeat_paths)
        else:
            print(f"{rom_repeat_paths[0]}文件名唯一无需删除rom文件！")

    return filtered_repeat_paths


def menu_main():
    global got_pure_json_lists
    # 用户菜单
    print("获取目录下所有文件列表：")
    file_lists = get_file_lists(playlistsPath)
    print(file_lists)
    print("获取重复文件名和重复文件数量列表:")
    for file_path_name in file_lists:
        repeat_directory = find_repeat_in_lpl_file(file_path_name)
        if repeat_directory is None:
            continue
        # 如果file_path_name为.bak文件就跳过
        if os.path.splitext(file_path_name)[-1] == ".bak":
            print(f'{file_path_name}为bak文件，跳过！')
            continue

        if len(repeat_directory) == 0:
            print(f"{file_path_name}中没有重复文件！")
            continue
        print("\n%s中的重复文件名:\n" % file_path_name)
        for key, value in repeat_directory.items():
            print("{0}，重复次数：{1}".format(key, value))
        print("当前列表为：")
        got_pure_json_lists = get_json_lists(file_path_name)
        print(got_pure_json_lists)
        inital_numbers = len(got_pure_json_lists)
        print(f"当前列表条数：{inital_numbers}条")
        repeat_paths_by_rom_name = []
        for key, value in repeat_directory.items():
            repeat_paths_by_rom_name.append(get_repeat_paths_by_rom_name(key, got_pure_json_lists))
        print("\n重复文件路径为：\n")
        print(repeat_paths_by_rom_name)
        #   在移动重复文件之前需要对重复文件的路径和第一个列表中的路径进行判定，如果相同则不需要移动只需要删除列表即可
        repeat_paths_need_to_delete_file = filter_need_to_delete_file(repeat_paths_by_rom_name)

        # dir_to_delete = input("请输入要新建的目录用来存放删除的roms(缺省为./filetodelete):")
        move_dup_roms_to_temp_dir('', repeat_paths_need_to_delete_file)  # 第一个参数可以改为用户输入时选择的dir_to_delete值
        # 备份当前文件
        print("\n备份LPL文件：")
        if bak_file(file_path_name) == SUCCESS:
            # 删除当前LPL文件的重复条目
            print("删除当前重复条目:")
            full_list = get_json_lists(file_path_name, 1)
            to_del_names = chang_to_del_names(repeat_paths_by_rom_name)
            deleted_dup_items_json_list = del_dup_lists_in_pure_json(got_pure_json_lists, to_del_names)
            # print(deleted_dup_items_json_list)
            after_deleted_list_count = len(deleted_dup_items_json_list)
            print(f"当前列表条数：{after_deleted_list_count}条")
            full_list_deleted_dup = full_list
            full_list_deleted_dup['items'] = deleted_dup_items_json_list
            deleted_num = inital_numbers - after_deleted_list_count
            print(f"删除了：{deleted_num}条重复数据！")
            # 把当前删除完重复条目的列表写入MAME.lpl文件中
            write_json_data(full_list_deleted_dup, file_path_name)
        else:
            print("备份文件失败！")


if __name__ == '__main__':
    menu_main()
