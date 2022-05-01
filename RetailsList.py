# 一个条目类存取一条信息
class RetailsList:
    def __init__(self, one_list_dict):
        self.path = one_list_dict.get('path')
        self.rom_name = self.get_filename()
        self.label = one_list_dict.get(' label')
        self.core_path = one_list_dict.get(' core_path')
        self.core_name = one_list_dict.get(' core_name')
        self.crc32 = one_list_dict.get(' crc32')
        self.db_name = one_list_dict.get(' db_name')
        self.filename = one_list_dict.get('path').split("/")[-1]
        self.one_list_dict = one_list_dict

    def get_path(self):
        path = self.path
        return path

    # 获取路径下文件名
    def get_filename(self):
        path = self.get_path()
        filename = path.split("/")[-1]
        return filename

    # 根据文件名获取当前条目路径
    def get_path_by_filename(self, filename):
        path = self.get_path()
        if filename == path.split("/")[-1]:
            return path
        else:
            return None

    # 返回一个具有rom_name的list
    def get_dict_with_rom_name(self):
        # keys = self.keys().copy()
        # keys = keys.append("rome_name")
        # values = self.values().copy()
        # values = values.append(self.filename)
        # one_list_dict = dict.fromkeys(keys, values)
        rom_name = self.get_filename()
        one_list_dict_with_rom_name = {'rom_name': rom_name}
        one_list_dict_with_rom_name.update(self.one_list_dict)
        return one_list_dict_with_rom_name
