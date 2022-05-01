import os
import json
from RetailsList import RetailsList
from collections import Counter  # 引入Counter

# workpath = "i:/"
work_path = "e:/temp/"
rom_path = work_path + "/rom"
# thumbnail = "I:/retroarch/thumbnail"
thumbnailPath = "d://thumbnail/"
# playlists = "I:/retroarch/playlists"
play_list_name = "playlists/"
playlistsPath = work_path + play_list_name


# 遍历目录，获取路径下所有文件
def get_file_lists(filepath=playlistsPath):
    fileNames = []
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
    json_lists = get_json_lists(filepath)
    filename_lists = []  # 重复的文件名列表
    repeat_directory = get_repeat_list_and_count(filename_lists, json_lists)
    # print(filename_lists) #重复文件列表
    return repeat_directory
    # json.loads(string)['code']取code值的方法
    # for key in pure_load_f:
    #  print('======key========:' + key + "************value******" + key)


# 获取无前缀json
def get_json_lists(filepath=playlistsPath + "MAME.lpl"):
    pure_lists = open_file_get_pure_json(filepath)
    json_lists = json.loads(pure_lists)
    return json_lists


# 获取重复文件名和重复的数量
def get_repeat_list_and_count(filename_lists, json_lists):
    for dict_list in json_lists:
        print(dict_list)  # 显示每条列表
        # 生成一个RetailsList类的实例
        retails_list = RetailsList(dict_list)
        path = retails_list.get_path()
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
def open_file_get_pure_json(file_path):
    with open(file_path, 'rb') as load_f:
        load_dict = json.load(load_f)
        pure_load_f = del_from_N_to_end(load_dict)
        return pure_load_f


# 截取掉前面多余部分{'version': '1.4', 'default_core_path': '', 'default_core_name': '', 'label_display_mode': 0,
# 'right_thumbnail_mode': 0, 'left_thumbnail_mode': 0, 'sort_mode': 0, 'items':
def del_from_N_to_end(input_jason):
    # jason文件转为字符串
    input_string = json.dumps(input_jason)
    length = len(
        "{'version': '1.4', 'default_core_path': '', 'default_core_name': '', 'label_display_mode': 0, "
        "'right_thumbnail_mode': 0, 'left_thumbnail_mode': 0, 'sort_mode': 0, 'items':{")
    sub_input_string = input_string[length:-1]
    # print(sub_input_string)
    return sub_input_string


# add rom filename to item in json_lists
def add_rom_name_to_json_lists(json_lists):
    add_rom_names_dict_lists = []
    for dict_list in json_lists:
        retails_list = RetailsList(dict_list)
        added_rom_name_dict = retails_list.get_dict_with_rom_name()
        add_rom_names_dict_lists.append(added_rom_name_dict)

    return add_rom_names_dict_lists


# 输入('s1945.zip', 3) 给出重复列表
def get_list_by_repeat_filename(repeat_file_name_and_count, json_lists=get_json_lists()):
    # print(repeat_file_name_and_count)
    json_lists_add_rom_name = add_rom_name_to_json_lists(json_lists)
    # for each in repeat_file_name_and_count:
    #     if each['id'] == your_id:
    #         print
    #         each['abstract']


# with open("./record.json", "w") as dump_f:
#  json.dump(load_dict, dump_f)
# return "success"
print("获取所有列表：")
print(get_file_lists(playlistsPath))
print("获取重复文件名和重复文件数量列表:")
repeat_directory = find_repeat_in_lpl_file()
print(repeat_directory)
print("当前列表为：")
get_json_lists = get_json_lists()
print(get_json_lists)
for item in repeat_directory.items():
    get_list_by_repeat_filename(item, get_json_lists)
