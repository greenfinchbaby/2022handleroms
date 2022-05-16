#  Handle Roms In Retroarch
This  project is used to delete duplicate lists in playlists directory of Retrarch .\
本项目用于删除Retrarch模拟器中的重复列表。
## Content

- 查找所列目录中的lpl文件
- 跳过目录中的.bak文件与非lpl格式文件
- 备份原有的lpl文件到同目录下的.bak文件
- 删除lp文件中的对应重复的目录到特定目录以便删除（此版本没有设置目录位置，下一版本进行修改为指定目录）
- 此项目为本人第一个python的试写项目，也非常适合初学者进行熟悉Python的语法，和作为初学Python的练手项目
## Files
[RetailsListi.py](./RetailsList.py) - 一个具体条目类存取一条信息\
[Main.py](。/main.py) - 测试类下一个版本会删除\
[findrepeatlist](./findrepeartlist.py) - 程序的主要功能类（下一版本进行重构）\
[test_class_retailslist.py](./test_class_retailslist.py) - 测试类可以删除\
[test_findrepeartlist.py](./test_findrepeartlist.py) - 测试类可删除