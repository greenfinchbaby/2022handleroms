import os
import json
#workpath = "i:/"
workpath= "e:/temp/"
rompath = workpath + "/rom"
#thumbnail = "I:/retroarch/thumbnail"
thumbnailPath = "d://thumbnail/"
#playlists = "I:/retroarch/playlists"
playlistname ="playlists/"
playlistsPath = workpath+playlistname

#遍历目录，获取路径下所有文件
def getFileLists(filePath = playlistsPath):
 fileNames=[]
 for parent, dirnames, filenames in os.walk(filePath):
  # Case1: traversal the directories
  for dirname in dirnames:
   print("Parent folder:", parent)
   print("Dirname:", dirname)
  # Case2: traversal the files
  for filename in filenames:
   print("Parent folder:", parent)
   print("Filename:", filename)
 filepaths = appendPathToFilename(filenames)
 return filepaths

#给当前文件名列表加上路径
def appendPathToFilename(names):
 # 对原列表进行遍历
 new_names=[]
 while names:
  # 对每一个列表元素进行出栈操作，并在前面添加字符串，并保存在当前变量中
  current_name = playlistsPath + names.pop()
  # 把当前变量保存在新列表中
  new_names.append(current_name)

 return new_names  # 返回新列表




#打开单个lpl文件查找重复首字段内容
def findRepeatInLplFile(filePath = playlistsPath+"MAME.lpl"):
 with open(filePath, 'rb') as load_f:
  load_dict = json.load(load_f)
  print(load_dict)




 # with open("./record.json", "w") as dump_f:
 #  json.dump(load_dict, dump_f)
  #return "success"
print(getFileLists(playlistsPath))
findRepeatInLplFile()