import unittest
from RetailsList import RetailsList


class TestRetailsList(unittest.TestCase):
    # 针对RetailsList的类测试
    def setUp(self):
        onelist = {'path': '/ROM/MAME/001/gunbird.zip', 'label': '001 gunbird',
                   'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro', 'core_name': '武装飞鸟 一代',
                   'crc32': 'MAME.lpl', 'db_name': ''}
        self.my_list = RetailsList(onelist)
        self.path = '/ROM/MAME/001/gunbird.zip'
        self.label = '001 gunbird'
        self.rom_name = 'gunbird.zip'
        self.dict_with_rom_name = {'rom_name': 'gunbird.zip', 'path': '/ROM/MAME/001/gunbird.zip', 'label': '001 gunbird',
             'core_path': '/retroarch/cores/fbalpha_libretro_libnx.nro', 'core_name': '武装飞鸟 一代',
             'crc32': 'MAME.lpl', 'db_name': ''}

    # 测试get_path函数
    def test_store_get_path(self):
        self.assertEqual(self.path, self.my_list.get_path())

    # 测试是不是能把path中的路径romname分离出来
    def test_rom_name(self):
        self.assertEqual(self.rom_name, self.my_list.rom_name)

    def test_get_dict_with_rom_name(self):
        dict_with_rom_name = self.my_list.get_dict_with_rom_name()
        self.assertDictEqual (self.dict_with_rom_name, dict_with_rom_name)

    if __name__ == '__main__':
        unittest.main()
