import os
import unittest
from unittest import TestCase

import findrepeartlist
from findrepeartlist import add_rom_name_to_json_lists, get_repeat_paths_by_rom_name, move_delete_rom_to_temp_dir, \
    bak_file, del_from_n_to_end_return_item_json, del_dup_lists_in_pure_json


class Test(TestCase):
    def test_three_path_get_repeat_paths_by_rom_name(self):
        rom_name = "s1945.zip"
        jason_lists = [
            {
                "path": "/ROM/MAME/001/gunbird.zip",
                "label": "001 gunbird",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "武装飞鸟 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/ROM/MAME/003/s1945.zip",
                "label": "003 s1945",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "彩京1945 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/roms/s1945.zip",
                "label": "Strikers 1945 (World)",
                "core_path": "/retroarch/cores/mame2003_plus_libretro_libnx.nro",
                "core_name": "Arcade (MAME 2003-Plus)",
                "crc32": "3531FB50|crc",
                "db_name": "MAME.lpl"
            },
            {
                "path": "/rom/MAME/Strikers 1945/s1945.zip",
                "label": "打击者 1945",
                "core_path": "/RetroArch/cores/fbalpha2012_libretro.nro",
                "core_name": "fbalpha 2012",
                "crc32": "00000000|crc",
                "db_name": "MAME.lpl"
            }
        ]
        output_repeat_paths = ["/ROM/MAME/003/s1945.zip", "/roms/s1945.zip",
                               "/rom/MAME/Strikers 1945/s1945.zip"]
        self.assertEqual(output_repeat_paths, get_repeat_paths_by_rom_name(rom_name, jason_lists))

    def test_add_rom_name_to_json_lists(self):
        add_rom_names_list = []
        add_rom_names_dict1 = {'rom_name': 'outzone.zip', 'path': '/rom/MAME/Out Zone/outzone.zip', 'label': '异域战将',
                               'core_path': '/RetroArch/cores/fbalpha_libretro.nro', 'core_name': 'fbalpha',
                               'crc32': '00000000|crc', 'db_name': 'MAME.lpl'}
        add_rom_names_dict2 = {'rom_name': 'gunbird.zip', 'path': '/ROM/MAME/001/gunbird.zip', 'label': '异域战将',
                               'core_path': '/RetroArch/cores/fbalpha_libretro.nro', 'core_name': 'fbalpha',
                               'crc32': '00000000|crc', 'db_name': 'MAME.lpl'}
        add_rom_names_list.append(add_rom_names_dict1)
        add_rom_names_list.append(add_rom_names_dict2)
        json_lists = [{'path': '/rom/MAME/Out Zone/outzone.zip', 'label': '异域战将',
                       'core_path': '/RetroArch/cores/fbalpha_libretro.nro', 'core_name': 'fbalpha',
                       'crc32': '00000000|crc', 'db_name': 'MAME.lpl'},
                      {'path': '/ROM/MAME/001/gunbird.zip', 'label': '异域战将',
                       'core_path': '/RetroArch/cores/fbalpha_libretro.nro', 'core_name': 'fbalpha',
                       'crc32': '00000000|crc', 'db_name': 'MAME.lpl'}]
        self.assertEqual(add_rom_names_list, add_rom_name_to_json_lists(json_lists))

    if __name__ == '__main__':
        unittest.main()

    def test_move_delete_rom_to_temp_dir(self):
        path_name = 'e:/temp/rom/s1945.zip'
        input_dir = '/rom/s1945.zip'
        temp_dir = 'e:/temp/filetodelete/s1945.zip'
        if not os.path.exists(path_name):
            open(path_name, 'w+').close()
        success_or_failed = move_delete_rom_to_temp_dir(input_dir, 'filetodelete')
        deleted = not os.path.isfile(path_name)
        moved = os.path.isfile(temp_dir)
        self.assertTrue(deleted and moved and success_or_failed == 1)

    def test_bak_file_not_exist(self):
        path = 'e:/rom/s1945.zip'
        exist_bak_file = not os.path.exists("e:/rom/s1945.zip.bak")
        self.assertTrue(exist_bak_file and not bak_file(path))

    # 测试会把之前所有测试的操作，包括新建文件等内容都恢复成原来的样子
    def test_bak_file_existed(self):
        path_name = 'e:/temp/rom/s1945.zip'
        if not os.path.exists(path_name):
            open(path_name, 'w+').close()
        if os.path.exists(path_name + '.bak'):
            os.remove(path_name + '.bak')
        bak_success = bak_file(path_name)
        exist_bak_file = os.path.exists("e:/temp/rom/s1945.zip.bak")
        exist_previous_file = os.path.exists("e:/temp/rom/s1945.zip")

        self.assertEqual(exist_bak_file and exist_previous_file, bak_success)

    # 测试获取json文件中的item:中的值
    def test_del_from_n_to_end_return_item_json(self):
        input_json = {'version': '1.4', 'default_core_path': '', 'default_core_name': '', 'label_display_mode': 0,
                      'right_thumbnail_mode': 0, 'left_thumbnail_mode': 0, 'sort_mode': 0, 'items': [
                {'path': '/ROM/MAME/001/gunbird.zip', 'label': '001 gunbird',
                 'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro', 'core_name': '武装飞鸟 一代',
                 'crc32': 'MAME.lpl', 'db_name': ''}, {'path': '/ROM/MAME/002/atetris.zip', 'label': '002 atetris',
                                                       'core_path': '/retroarch/cores/mame2003_libretro_libnx.nro',
                                                       'core_name': '俄罗斯方块 一代', 'crc32': 'MAME.lpl', 'db_name': ''},
                {'path': '/ROM/MAME/003/s1945.zip', 'label': '003 s1945',
                 'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro', 'core_name': '彩京1945 一代',
                 'crc32': 'MAME.lpl', 'db_name': ''}, {'path': '/ROM/MAME/004/s1945ii.zip', 'label': '004 s1945ii',
                                                       'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro',
                                                       'core_name': '彩京1945 二代', 'crc32': 'MAME.lpl', 'db_name': ''}]}
        get_item_value = [{'path': '/ROM/MAME/001/gunbird.zip', 'label': '001 gunbird',
                           'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro', 'core_name': '武装飞鸟 一代',
                           'crc32': 'MAME.lpl', 'db_name': ''},
                          {'path': '/ROM/MAME/002/atetris.zip', 'label': '002 atetris',
                           'core_path': '/retroarch/cores/mame2003_libretro_libnx.nro',
                           'core_name': '俄罗斯方块 一代', 'crc32': 'MAME.lpl', 'db_name': ''},
                          {'path': '/ROM/MAME/003/s1945.zip', 'label': '003 s1945',
                           'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro', 'core_name': '彩京1945 一代',
                           'crc32': 'MAME.lpl', 'db_name': ''},
                          {'path': '/ROM/MAME/004/s1945ii.zip', 'label': '004 s1945ii',
                           'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro',
                           'core_name': '彩京1945 二代', 'crc32': 'MAME.lpl', 'db_name': ''}]
        self.assertEqual(get_item_value, del_from_n_to_end_return_item_json(input_json))

    def test_del_2_dup_lists_in_pure_json(self):
        jason_lists = [
            {
                "path": "/ROM/MAME/001/gunbird.zip",
                "label": "001 gunbird",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "武装飞鸟 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/ROM/MAME/003/s1945.zip",
                "label": "003 s1945",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "彩京1945 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/roms/s1945.zip",
                "label": "Strikers 1945 (World)",
                "core_path": "/retroarch/cores/mame2003_plus_libretro_libnx.nro",
                "core_name": "Arcade (MAME 2003-Plus)",
                "crc32": "3531FB50|crc",
                "db_name": "MAME.lpl"
            },
            {
                "path": "/rom/MAME/Strikers 1945/s1945.zip",
                "label": "打击者 1945",
                "core_path": "/RetroArch/cores/fbalpha2012_libretro.nro",
                "core_name": "fbalpha 2012",
                "crc32": "00000000|crc",
                "db_name": "MAME.lpl"
            }
        ]
        repeat_paths = ["/ROM/MAME/003/s1945.zip", "/roms/s1945.zip",
                        "/rom/MAME/Strikers 1945/s1945.zip"]
        deleted_json = [
            {
                "path": "/ROM/MAME/001/gunbird.zip",
                "label": "001 gunbird",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "武装飞鸟 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/ROM/MAME/003/s1945.zip",
                "label": "003 s1945",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "彩京1945 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            }
        ]
        self.assertEqual(deleted_json, del_dup_lists_in_pure_json(jason_lists, repeat_paths, 1))

    def test_del_1_dup_lists_in_pure_json(self):
        jason_lists = [
            {
                "path": "/ROM/MAME/001/gunbird.zip",
                "label": "001 gunbird",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "武装飞鸟 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/ROM/MAME/003/s1945.zip",
                "label": "003 s1945",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "彩京1945 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/roms/s1945.zip",
                "label": "Strikers 1945 (World)",
                "core_path": "/retroarch/cores/mame2003_plus_libretro_libnx.nro",
                "core_name": "Arcade (MAME 2003-Plus)",
                "crc32": "3531FB50|crc",
                "db_name": "MAME.lpl"
            }
        ]
        repeat_paths = ["/ROM/MAME/003/s1945.zip", "/roms/s1945.zip"]
        deleted_json = [
            {
                "path": "/ROM/MAME/001/gunbird.zip",
                "label": "001 gunbird",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "武装飞鸟 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/ROM/MAME/003/s1945.zip",
                "label": "003 s1945",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "彩京1945 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            }
        ]
        self.assertEqual(deleted_json, del_dup_lists_in_pure_json(jason_lists, repeat_paths, 1))

    def test_del_all_dup_lists_in_pure_json(self):
        jason_lists = [
            {
                "path": "/ROM/MAME/001/gunbird.zip",
                "label": "001 gunbird",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "武装飞鸟 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/ROM/MAME/003/s1945.zip",
                "label": "003 s1945",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "彩京1945 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/roms/s1945.zip",
                "label": "Strikers 1945 (World)",
                "core_path": "/retroarch/cores/mame2003_plus_libretro_libnx.nro",
                "core_name": "Arcade (MAME 2003-Plus)",
                "crc32": "3531FB50|crc",
                "db_name": "MAME.lpl"
            }
        ]
        repeat_paths = ["/ROM/MAME/003/s1945.zip", '/roms/s1945.zip', '/rom/MAME/Strikers 1945/s1945.zip']
        deleted_json = [
            {
                "path": "/ROM/MAME/001/gunbird.zip",
                "label": "001 gunbird",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "武装飞鸟 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            }
        ]
        self.assertEqual(deleted_json, del_dup_lists_in_pure_json(jason_lists, repeat_paths, ))

    def test_chang_to_del_names(self):
        repeat_paths_by_rom_name = [['/ROM/MAME/001/gunbird.zip', '/rom/MAME/Gun Bird 1/gunbird.zip'],
                                    ['/ROM/MAME/003/s1945.zip', '/roms/s1945.zip', '/rom/MAME/Strikers 1945/s1945.zip']]
        to_del_names = ['/rom/MAME/Gun Bird 1/gunbird.zip', '/roms/s1945.zip', '/rom/MAME/Strikers 1945/s1945.zip']
        self.assertEqual(to_del_names, findrepeartlist.chang_to_del_names(repeat_paths_by_rom_name))

    def test_chang_to_del_names_only_one_list(self):
        repeat_paths_by_rom_name = [['/ROM/MAME/001/gunbird.zip'],
                                    ['/ROM/MAME/003/s1945.zip', '/roms/s1945.zip', '/rom/MAME/Strikers 1945/s1945.zip']]
        to_del_names = ['/roms/s1945.zip', '/rom/MAME/Strikers 1945/s1945.zip']
        self.assertEqual(to_del_names, findrepeartlist.chang_to_del_names(repeat_paths_by_rom_name))

    def test_update_item_into_json(self):
        item_value = [
            {
                "path": "/ROM/MAME/001/gunbird.zip",
                "label": "001 gunbird",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "武装飞鸟 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            },
            {
                "path": "/ROM/MAME/003/s1945.zip",
                "label": "003 s1945",
                "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                "core_name": "彩京1945 一代",
                "crc32": "MAME.lpl",
                "db_name": ""
            }
        ]

        input_json = {'version': '1.4', 'default_core_path': '', 'default_core_name': '', 'label_display_mode': 0,
                      'right_thumbnail_mode': 0, 'left_thumbnail_mode': 0, 'sort_mode': 0, 'items': [
                {'path': '/ROM/MAME/001/gunbird.zip', 'label': '001 gunbird',
                 'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro', 'core_name': '武装飞鸟 一代',
                 'crc32': 'MAME.lpl', 'db_name': ''}, {'path': '/ROM/MAME/002/atetris.zip', 'label': '002 atetris',
                                                       'core_path': '/retroarch/cores/mame2003_libretro_libnx.nro',
                                                       'core_name': '俄罗斯方块 一代', 'crc32': 'MAME.lpl', 'db_name': ''},
                {'path': '/ROM/MAME/003/s1945.zip', 'label': '003 s1945',
                 'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro', 'core_name': '彩京1945 一代',
                 'crc32': 'MAME.lpl', 'db_name': ''}, {'path': '/ROM/MAME/004/s1945ii.zip', 'label': '004 s1945ii',
                                                       'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro',
                                                       'core_name': '彩京1945 二代', 'crc32': 'MAME.lpl', 'db_name': ''}]}
        updated_json = {'version': '1.4', 'default_core_path': '', 'default_core_name': '', 'label_display_mode': 0,
                        'right_thumbnail_mode': 0, 'left_thumbnail_mode': 0, 'sort_mode': 0, 'items': [
                {
                    "path": "/ROM/MAME/001/gunbird.zip",
                    "label": "001 gunbird",
                    "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                    "core_name": "武装飞鸟 一代",
                    "crc32": "MAME.lpl",
                    "db_name": ""
                },
                {
                    "path": "/ROM/MAME/003/s1945.zip",
                    "label": "003 s1945",
                    "core_path": "/retroarch/cores/fbalpha_libretro_libnx.nro",
                    "core_name": "彩京1945 一代",
                    "crc32": "MAME.lpl",
                    "db_name": ""
                }
            ]}
        self.assertEqual(updated_json, findrepeartlist.update_item_into_jason(input_json, item_value))

    #   测试列表中的文件路径同第一个文件相同则不需要删除该rom文件只需要删除列表即可
    def test_filter_need_to_delete_file(self):
        input_list = [['/ROM/MAME/001/gunbird.zip', '/ROM/MAME/001/gunbird.zip'],  # 如果是两个元素相同则都不要
                      ['/ROM/MAME/003/s1945.zip', '/ROM/MAME/003/s1945.zip', '/rom/MAME/Strikers 1945/s1945.zip'],
                      ['/ROM/MAME/004/s1945ii.zip', '/roms/s1945ii.zip', '/ROM/MAME/004/s1945ii.zip']]

        output_list = [['/ROM/MAME/003/s1945.zip', '/rom/MAME/Strikers 1945/s1945.zip'],
                       ['/ROM/MAME/004/s1945ii.zip', '/roms/s1945ii.zip']]
        self.assertEqual(output_list, findrepeartlist.filter_need_to_delete_file(input_list))
