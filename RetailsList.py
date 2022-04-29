# 一个条目类存取一条信息
class RetailsList:
    def __init__(self, onelist):
        self.path = onelist.get('path')
        self.label = onelist.get(' label')
        self.core_path = onelist.get(' core_path')
        self.core_name = onelist.get(' core_name')
        self.crc32 = onelist.get(' crc32')
        self.db_name = onelist.get(' db_name')

    def get_path(self):
        path = self.path
        return path

    # 获取路径下文件名
    def get_filename(self):
        path = self.get_path()
        filename = path.split("/")[-1]