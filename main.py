# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from RetailsList import RetailsList

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

print_hi('PyCharm')
test_dict = {'path': '/rom/MAME/Out Zone/outzone.zip', 'label': '异域战将', 'core_path': '/RetroArch/cores/fbalpha_libretro.nro', 'core_name': 'fbalpha', 'crc32': '00000000|crc', 'db_name': 'MAME.lpl'}
retails_list = RetailsList(test_dict)
# path = retails_list.get_path()
# print(path)

dict_with_rom_name = retails_list.get_dict_with_rom_name()
print(dict_with_rom_name)
# print(retails_list.get_path_by_filename("outzone.zip")
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del tinydict['Name']# 删除键是'Name'的条目
tinydict.clear()# 清空字典所有条目
if len(tinydict) ==0:
    print("空")