## 首先
"""
sudo apt install git
git config user.name "你的名字"
git config user.email "你的邮箱"
## 在对应的账户下 生成 公钥和私钥
ssh-keygen -t rsa -C "你的邮箱"

## 然后 将公钥添加到github上
将公钥复制下来
cd ./.ssh
ls -la
cat ./id_rsa.pub

## 然后 将私钥添加到本地

## 查看 有没有开启ssh-agent服务
ps -ef| grep shh-agent
## 在对应的账户下 开启ssh-agent
eval $(ssh-agent -s)
## 将私钥添加到ssh-agent服务中
ssh-add ~/.ssh/id_rsa
查看私钥是否添加成功
ssh-add -l

成功后 ssh -T git@github.com
## 然后 将本地的仓库和远程的仓库关联起来
在对应的文件夹下
git init
git add .
git commit -m "提交的信息"
git remote add origin EMAILgit remote add origin git@github.com:你的用户名/你的仓库名.git
git push -u origin master








"""