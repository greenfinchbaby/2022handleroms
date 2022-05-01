import os
import unittest
from unittest import TestCase
from findrepeartlist import add_rom_name_to_json_lists, get_repeat_paths_by_rom_name, move_delete_rom_to_temp_dir, \
    bak_file


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

    #       def test_first_last_name(self):
    #           --snip--
    #
    #       def test_first_last_middle_name(self):
    #           """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
    # ❶         formatted_name = get_formatted_name(
    #               'wolfgang', 'mozart', 'amadeus')
    #           self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

    if __name__ == '__main__':
        unittest.main()
#
    def test_move_delete_rom_to_temp_dir(self):
        path_name = 'e:/temp/rom/s1945.zip'
        inputdir = '/rom/s1945.zip'
        temp_dir = 'e:/temp/filetodelete/s1945.zip'
        if not os.path.exists(path_name):
            open(path_name, 'w+').close()
        success_or_failed = move_delete_rom_to_temp_dir(inputdir, 'filetodelete')
        deleted = not os.path.isfile(path_name)
        moved = os.path.isfile(temp_dir)
        self.assertTrue(deleted and moved and success_or_failed == 1)

    def test_bak_file_not_exist(self):
        path = 'e:/rom/s1945.zip'
        exist_bak_file = not os.path.exists("e:/rom/s1945.zip.bak")
        self.assertTrue(exist_bak_file and not bak_file(path))
    def test_bak_file_existed(self):
        path_name = 'e:/rom/s1945.zip'
        if not os.path.exists(path_name):
            open(path_name, 'w+').close()
        if os.path.exists(path_name+'.bak'):
            os.remove(path_name+'.bak')
        exist_bak_file = os.path.exists("e:/rom/s1945.zip.bak")
        self.assertEqual(exist_bak_file,bak_file(path_name))