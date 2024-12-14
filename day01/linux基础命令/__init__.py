# [\u@\h \w]\$
# \u 代表当前登陆的用户
# \h 代表当前主机的主机名
# \w 代表当前目录
"""
 0 表示，默认字体
 1 表示 加粗
 4 表示 在字体下方加下划线
"""

#内外部命令
"""
 内部命令：shell 自带的命令
 
 
 外部命令： 
 
 如何查看属于内部还是外部  type  options
 eg: type echo

"""

## 别名
"""
别名 ： 
查看当前所有别名 ： alias

如何起别名 ：  alias cdetc='cd /etc'

如何删除别名 ：unalias cdetc

设置别名 只对当前的终端有效

如何使这个别名在所有的用户都可以使用：
echo "alias cdetc='cd /etc'" >> /etc/bashrc
将 设置别名 的代码写入 文件中

如何使这个别名支队当前用户有效 写如 ～/.bashrc

如何执行命令本身
\ls
"ls"
'ls'

"""


## 命令的格式
"""
命令的格式
command [options][args]
command 命令本身
options 选项  启动或者关闭命令中某些功能
    长选项   --help --color
    短选项   -l -a  
    短选项和短选项之间可以合并  -la
args 命令的作用体  一般为 目录或者文件、用户名
1、命令和选项和参数之间都要有空格隔开
2、ctrl +c 结束命令的执行
3、同一行想要执行多个命令 可以用 分号 分割 
eg：tty;echo 'hello world'
4、多行执行同一个命令  使用\ 隔开可以换行
eg: echo dadasdsad\
asdasd\
asdasdas
输出为adasdsadasdasdasdasdas

"""

## bash 快捷键
"""
bash  快捷键

ctrl + l  清屏

ctrl + o 执行并显示当前的命令

ctrl + s 锁屏

ctrl + q 解锁

ctrl + c 终止命令

ctrl + z 挂起命令

ctrl + a 光标移动到行首

ctrl + e 光标移动到行尾

ctrl + u 剪切光标之前的所有字符

ctrl + k 剪切光标之后的所有字符

ctrl + y 粘贴

ctrl + w 剪切光标之前的一个单词

ctrl + r 搜索历史命令

ctrl + p 上一条命令

ctrl + n 下一条命令

ctrl + d 退出当前终端

ctrl + t 交换光标之前的两个字符

ctrl + ？ 查看当前命令的帮助信息

ctrl + ！ 执行上一条命令

"""

## tab 快捷键
"""
tab 快捷键

命令补全
"""

## 单双引号的区别
"""
单双引号的区别

双引号会给字符串中的变量进行解析
意思是双引号里面的内容会被当做代码来执行

单引号不会给字符串中的变量进行解析
意思是 单引号里面的内容原样输出
eg:
双引号
name=alex
echo "$name"
输出内容为 alex

单引号
echo '$name'
输出内容为 $name

"""

# 命令历史
"""
命令历史的存放文集在 ./bash_history
执行上一条命令  ！！
怎么看历史命令的条数 history
查看最后 x 条命令  history 10
执行历史命令的第几条 ！10    执行第10条命令
执行命令的上一层命令  ！-1   ctrl + p

搜索历史命令 ctrl + r
取消搜索 ctrl + g


调用上一个命令的最后一个值 esc.
！string  调用上一个命令中包含string的命令 匹配最近string的命令
eg：
echo 21
echo 22
echo 23
！echo     输出为 23

"""

#命令展开
"""

echo file{1..20}  输出file1到20
echo file{1..20..2}   输出file1到20 其中步长为2
seq 1 10  输出1到10
seq 1 2 20  输出1到20 步长为2   
echo file{`seq 1 2 20`}  输出file1到20 步长为2  其中使用的是 反引号` 
其结果为 file{1 3 5 7 9 11 13 15 17 19}  不推荐


"""

# echo  回显
"""
echo -e '\a'  
输出 响铃

echo -e 'dadasda\nasdada' 
输出结果：dadasda
        asdada  
        其中\n 表示换行    

"""

#查看用户登陆信息
"""
whoami  查看当前用户

who am i 查看当前用户详细信息

w   查看当前在线用户的详细信息


"""

# 时间
"""
date  显示当前时间
2024年 12月 12日 星期四 16:36:04 CST
修改时间 date 010923102018      2018年9月1日 23:10:00

把时间改回当前时间 ntpdate time.windows.com  同步网络服务器时间
date +%a  显示当前时间的星期几中的 几  例如 今天星期四  会显示 四
date +%A  显示当前时间的星期几   例如 今天星期四  会显示 星期四
date +%b  显示当前时间的月份   显示 12月
date +%B  显示当前时间的月份   显示 十二月
date +%d  显示当前时间的日期   会显示 12   day
date +%D  显示当前时间的日期   会显示 12/12/24
date +%H  显示当前时间的小时   会显示24小时制的 当前小时
date +%h  显示当前时间的月份   会显示 12月
date +%M  显示当前时间的分钟   
date +%S  显示当前时间的秒
date +%Y  显示当前时间的年份
date +%s  显示当前时间的时间戳
date +%I  显示当前时间的小时    12小时制的时间
date +%p  显示当前时间的上午或者下午
date +%W  显示当前时间的第几周
date +%Y/%m/%d  显示当前时间的年月日

"""

# 日历
"""
cal 当月日历

cal -y  显示当年日历

cal -y 2018  显示2018年的日历
cal 2018  显示2018年的日历

"""

#关机 重启
"""
#关机
shutdown 一分钟后关机

shutdown -c  取消关机
shutdown now 立即挂机
shutdown +2 2分钟后关机
shutdown 18：00 18点关机

poweroff 关机
halt 关机
init 0 关机

# 重启
reboot 重启
reboot -f 强制重启
shutdown -r 一分钟后重启
init 6 重启

"""


