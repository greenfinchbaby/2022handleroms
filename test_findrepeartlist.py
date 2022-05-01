import unittest
from unittest import TestCase
from findrepeartlist import add_rom_name_to_json_lists


class Test(TestCase):
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
