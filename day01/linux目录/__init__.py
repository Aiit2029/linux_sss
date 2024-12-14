## 文件目录结构
"""
# linux中文件名称区分大小写  / windows中文件名称不区分大小写
# linux文件系统中 一切从 根 开始
# 根目录 ： /
# 家目录 ： ~
# 上一级目录 ： ..
# 当前目录 ： .
# 目录之间用 / 分割
# 绝对路径 ： 从根目录开始的路径
# 相对路径 ： 从当前目录开始的路径
# 目录的权限 ： rwx
# 隐藏的文件以.开头
# linux中路径的分割符号 为 /
"""

## 文件命名 规范
"""
文件字符最长为255个字符
包括路径在内文件名称最常委4095个字符
颜色 ：
蓝色 --》 目录/文件夹  
绿色 --》 可执行的文件  
红色 --》 压缩文件
蓝绿色 --》 链接文件  
灰色 --》 其他文件
白色 --》 单独的文件


which 命令 查看命令的路径

# 除了/和NULL 所有的字符都可以被使用来表示文件名

对大小写敏感
"""

## 文件系统结构
"""
/boot 存放引导文件 包括内核文件 引导加载器
/dev 存放设备文件和特殊文件  
## 什么是设备文件？
    # 指的是 硬件设备和别的文件
/bin 所有的用户都可以使用的命令 
/sbin system 管理员使用的命令
/lib  启动时程序需要的基本库文件
/lib64  专门存放为64位操作系统准备的辅助库文件
/etc 存放系统的配置文件
/home/username 普通用户的家目录
/root 超级用户的家目录
/media   存放移动设备的挂载点
/mnt  挂载临时文件系统的位置
/opt  存放第三方软件的安装目录
/tmp  存放临时文件
/usr 存放用户的应用程序
/var 存放经常改变的文件，比如日志文件
/srv 存放服务启动之后需要提取的数据
/proc 存放内核启动和进程相关的虚拟文件


"""

# linux应用程序的组成
"""
# 二进制文件
    # /bin
    # /sbin
    # /usr/bin
    # /usr/sbin
    # /usr/local/bin
    # /usr/local/sbin
# 库文件
    # lib
    # lib64
    # /usr/lib
    # /usr/lib64
    # /usr/local/lib
    # /usr/local/lib64
# 配置文件
    # /etc
    # /etc/name
    # /usr/local/etc
# 帮助文件
    # /usr/share/doc
    # /usr/share/man
    # /usr/local/share/doc
    # /usr/local/share/man

"""

## 绝对路径和相对路径
"""
绝对路径：
    从根目录开始的路径
    可以读取到任何文件
相对路径：
    从当前目录开始的路径
    可以简短的表示一个文件或者文件夹
    . 在linux中表示当前目录
    .. 表示 上一级目录 
   
"""

## 目录名和基名
"""
basename /usr/bin/ls
    获取文件的名称 ls
dirname /usr/bin/ls
    获取文件的路径 /usr/bin

"""

## 切换目录
"""

可以使用相对路径
可以使用绝对路径
cd .
cd ..
cd -
cd /lib

"""

## 列出目录或文件
"""
ls -a 列出所有的文件
ls -l 列出所有的文件的详细信息
drwxrwxr-x 3 priceless priceless  4096 12月 11 13:55 linux_study
权限    硬链接数  所有者  组          大小   时间          名称
ls -R 目录递归显示

ls -d 列出目录本身

ls -1 每个文件单独一行显示

ls -S 按照文件大小排序显示
ls -t 按照时间排序显示
ls -r 反向排序显示
ls -h 按照人类的可读方式显示文件大小  21M
ls -d */ 列出所有的目录
ls -a .* 只显示隐藏文件 


"""

## 权限 & linux 下的目录类型
"""
drwxrwxr-x 3 priceless priceless  4096 12月 11 13:55 linux_study
- 表示文件
d directory 目录
s socket 套接字
b block 块设备
c character 字符设备
| 表示符号链接文件
权限：
    r 可读
    w 可写
    x 可执行
    - 没有权限
"""

##查看文件状态
"""
stat 查看文件状态
access 访问时间
modify 修改时间
change 状态改变时间



"""

## 创建和修改文件
"""
touch  创建文件
touch -a 修改文件的访问时间 和 c修改时间
touch -m 修改文件的修改时间 mtime 和 ctime

"""

## 文件通配符
"""
* 所有的文件
？ 匹配的是任意单个字符
~ 匹配的是当前用户的家目录
[123] 其中一个
[0-9] 0-9之间的任意一个数字
[A-Z] ascii码表中的A-Z之间的任意一个字符
[:lower:]  表示小字母
[:upper:]  表示大写字母
[:alpha:]  表示字母
[:digit:]  表示数字
[:alnum:]  表示字母或者数字
[[:lower:]]  表示小写字母的任意一个
"""

## 创建目录
"""
mkdir 创建目录
mkdir -p 递归创建目录
mkdir -pv 递归创建目录并显示创建目录的详细过程

"""

## 删除目录
"""
rmdir 只能删除空目录
rmdir -p 删除目录并递归删除空目录

rm -rf 删除非空目录
"""


## 显示目录树
"""
tree 
tree -d . 只显示目录
tree -dL 2. 显示目录的层级为2 不包括当前目录

"""

## 复制文件和文件夹
"""
cp copy
cp -i 提示是否覆盖
cp -n 不覆盖
cp -R/-r 递归复制文件夹
cp -d 只复制链接文件不复制源文件
cp -b 备份文件
cp --backup=number 备份文件加上数字
cp -p 保留源文件的属性

"""

## 移动、重命名文件和文件夹
"""
mv move
mv -i 提示
mv file1 f1 重命名
mv -f file1 f5 强制覆盖
mv -b 备份文件
mv -v 显示移动的过程
"""

## 删除
"""
rm -i 提示
rm -f 强制删除
rm -r/-R 递归删除
rm -d 删除空目录
rm -rf * 强制删除所有文件



"""

## 软链接和硬链接
"""
软链接 ln -s f1       f2
            目标文件  创建的链接文件
软链接只是一个快捷方式


硬链接 ln f1 f2
硬链接 是直接复制文件的指针  硬链接的数量和源文件的数量是一致的
会导致 磁盘的引用次数加1


"""

## I/O重定向
"""
>>  追加
将标准输出追加到文件中
2>> 将标准错误输出追加到文件中
&>> 将标准输出和标准错误输出都追加到文件中

>   覆盖

> 将标准输出重定向到文件中
2> 将标准错误输出重定向到文件中
&> 将标准输出和标准错误输出都重定向到文件中
禁止覆盖
set -C
允许覆盖
set +C

"""

## 字符替换
"""
tr 
tr 'a-z' 'A-Z' < /etc/issue  将小写字母转换为大写字母
  
eg:
tr ab 12
输入： abc   输出： 12c
输入： abcd  输出： 12cd
输入： abb   输出： 122
tr ab 123
输入： abc   输出： 12c
tr abc 12
输入： abc   输出： 122
(普通情况以前方的字符为准)

tr -t abc 12
输入： abc   输出： 12c
输入： ab  输出： 12
(-t 为截断  以后方的字符为准)


(tr -d abc)
输入: asdasdqwer   输出： sdqwer  删除了abc

tr -s a
输入： aaaaaaaa   输出： a
(去重)

tr -sc a
输入：aaaaasdasdassdddd 输出：aaaaasdasdasd
(除了a之外的字符都去重)   -c 是 取反的意思


ctrl + d 结束


"""

## 多行发送给 stdout
"""
cat > f1

[cat >> f1 <<EOF
asdasd
asdadasd
asdadad
EOF]

"""

## 管道 pipe
"""
命令1|命令2|命令3
默认情况下 管道只能传送标准输出
如果需要把标准错误输出也传送过去则需要 |&
有一些命令是不接受管道的

"""

## cat 显示文本
"""
cat -n 显示每一行的行号
cat -b 显示非空行的行号
cat -E 在每一行的结尾显示 $
cat -s 对于空行进行合并

"""

## tac 倒序显示

## less 分屏显示文本
"""
/string  表示搜索 某字符串
小写的n 表示向下搜索
大写的N 表示向上搜索

less 是 man命令的默认分页工具
more 和 less 类似
"""

## more 分页显示文本
"""
默认显示读取的百分比
读取完成自动退出
"""

## head 显示文件的前面的内容
"""
head 默认显示文本的前10行

head -n x 显示前X行
head -c 10 显示前10个字符

"""

## tail 显示文件的后面的内容
"""
默认显示文本的最后10行

-x 显示最后X行
-n 显示后x行
-c x 显示最后x个字符 其中换行符也占字符

"""

## cut  切割
"""
cut -c2-5   表示切割显示第二到第五个字符
-c 按照字符切割
-d 按照分割符切割  默认是tab
-f# 表示切割后的第几个字段
#，#,#,显示离散的多个
#-# 显示连续的多个
1-5,7可以结合使用


ps -ef|cut -d" " -f1 > c
-d 表示分隔符
-f1 表示显示第一列
awk  'a[$0]++==0' c  去重
($0 表示当前行 c文件中的每一行 如果当前行是第一次出现则输出)


"""

## grep
"""
grep -c 'string' c 统计string出现的次数
grep -n 'string' c 统计有string出现的行数

"""

## paste 合并
"""
默认是相同的行合并到一起 默认是tab键分割
paste -d ' ' c f  合并两个文件  用空格分割
-d 指定分割符号
-s 将每个文件的所有的行显示成一列

"""

##wc word count
"""
wc b.txt
3,4,12   3行 4个单词 12个字符 


wc -l 只显示行数

wc -w 只显示单词数

wc -c 只显示字节数

wc -m 只显示字符数  中文也只算一个字符  utf-8中一个中文占3个字节

wc -L 只显示最长的行的长度

"""

## sort 排序
"""
默认按照字母排序

sort -r 倒序排序
sort -R 随机排序
sort -n 按照数字大小排序
sort -f 忽略大小写排序
sort -t 指定分隔符
sort -k 指定排序的字段
sort -nt: -k3 passwd 按照第三个字段的数字大小对passwd文件进行排序


"""

## uniq  合并相同的行
"""
uniq 合并相同的行
相邻
完全相同

uniq -c 统计相同的行出现的次数 只能统计相邻的相同的行 否则按照 单个的字符统计
uniq -d 只显示重复的行
uniq -u 只显示不重复的行

"""

## diff 对比文件
"""
diff d f

"""

## 修改文件的属组
"""
chown
chown root.root d 修改d文件的属组为root.root
chown root:root d 修改d文件的属组为root.root
chown -R root:root a 递归修改a目录下的所有文件的属组为root.root
chown --reference=b f3  将f3文件的属组修改为b文件的属组

chgrp root b 将b文件的属组修改为root
chgrp --reference=b f3 将f3文件的属组修改为b文件的属组


"""

## 权限
"""

属主  u   user
属组  g   group
其他  o   other
修改权限 chmod
chmod u+x f 为f文件的属主添加可执行的权限
chmod u-x f 为f文件的属主删除可执行的权限
chmod u=r f 设置f文件的属主的权限为可读的权限

drwxrwxr-x 4 priceless priceless  4096 12月 14 15:30 linux_study
一共十个  其中第一个是文件的类型  后面9位表示权限
其中第一个字母：
- 表示文件
d directory 目录
s socket 套接字
b block 块设备
c character 字符设备
| 表示符号链接文件
后面的9位字母表示权限 每三个一组
3组
r 表示 可读
w 表示 可写
x 表示 可执行
- 表示 没有权限

rwx rwx r-x 其中的-表示没有权限 分三个 表示
第一组 为 属主  属主拥有 读写执行的权限
第二组 为 属组  属组拥有 读写执行的权限
第三组 为 其他  其他拥有 读和执行的权限 而没有写的权限

对于文件来说
    # r 可以使用文本查看工具查看其中的内容
    # w 可以修改文本中的内容
    # x 执行 可以直接 ./filename 执行
    
对于目录来说
    # r 可以使用ls等文件查看的命令查看
    # w 可以创建文件也可以删除文件
    # x 可以cd进入目录
文件是否能够删除 取决于目录的权限

r w x 可以使用数字来表示
有则为1 没有则为0
rwx 表示 4 2 1

所以 chmod 改变权限 可以写成  
chmod 777 f  表示给f文件的所有权限
chmod 755 d  表示给d目录的所有权限
chmod 600 f  420 000 000 表示给f文件的属主的权限为可读可写
chmod --reference=b f3 将f3文件的权限修改为b文件的权限

## 设定特殊权限

+i  表示文件不可修改 不能删除 不能变更 
+a  表示文件只能追加内容

chattr +i a 为a文件添加不可修改的属性 
lsattr a 查看a文件的属性





"""

## 添加用户
"""
useradd u1 添加用户
passwd u1  为用户 u1 设置密码

"""







