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
 pure_lists = openFileGetPureJson(filePath)
 json_lists = json.loads(pure_lists)

 for onelist in json_lists:
  print(onelist)

 # for key in pure_load_f:
 #  print('======key========:' + key + "************value******" + key)

#打开文件去掉前面不需要信息，获取纯内容
def openFileGetPureJson(filePath):
 with open(filePath, 'rb') as load_f:
  load_dict = json.load(load_f)
  pure_load_f = delFromNToEnd(load_dict)
  return pure_load_f

#截取掉前面多余部分{'version': '1.4', 'default_core_path': '', 'default_core_name': '', 'label_display_mode': 0, 'right_thumbnail_mode': 0, 'left_thumbnail_mode': 0, 'sort_mode': 0, 'items':
def delFromNToEnd(input_jason):
  #jason文件转为字符串
  input_string = json.dumps(input_jason)
  length = len("{'version': '1.4', 'default_core_path': '', 'default_core_name': '', 'label_display_mode': 0, 'right_thumbnail_mode': 0, 'left_thumbnail_mode': 0, 'sort_mode': 0, 'items':{")
  subinputstring = input_string[length:-1]
  print(subinputstring)
  return subinputstring

 # with open("./record.json", "w") as dump_f:
 #  json.dump(load_dict, dump_f)
  #return "success"
print(getFileLists(playlistsPath))
findRepeatInLplFile()