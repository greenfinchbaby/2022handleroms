# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from RetailsList import RetailsList
from findrepeartlist import bak_file


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
#
# test_dict = {'path': '/rom/MAME/Out Zone/outzone.zip', 'label': '异域战将', 'core_path': '/RetroArch/cores/fbalpha_libretro.nro', 'core_name': 'fbalpha', 'crc32': '00000000|crc', 'db_name': 'MAME.lpl'}
# retails_list = RetailsList(test_dict)
# # path = retails_list.get_path()
# # print(path)
#
# dict_with_rom_name = retails_list.get_dict_with_rom_name()
# print(dict_with_rom_name)
# print(retails_list.get_path_by_filename("outzone.zip")



file = "Hello.py.bak"
print(file)
# 获取前缀（文件名称）
assert os.path.splitext(file)[0] == "Hello.py"

# 获取后缀（文件类型）
assert os.path.splitext(file)[-1] == ".bak"
assert os.path.splitext(file)[-1][1:] == "py"

bak_file('e:/temp/rom/s1945.zip')