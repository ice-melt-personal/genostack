# vagrant

## 创建
vagrant	init ubuntu/bionic64
vagrant init centos/7

得到Vagrantfile，修改一下

config.vm.box_check_update = false

## 启动和关闭
```Bash
# 启动
vagrant up	
# 关机
vagrant halt
# 关机并删除虚拟机文件
vagrant destroy

```

## 使用虚拟机

```Bash
# 使用ssh连接到虚拟机里面
vagrant ssh
# 查看目前的ssh配置，一般是默认映射到本机的2222端口的
vagrant ssh-config
# 按照上面命令显示的信息，输入ip/port/private_key文件，可以手动登录
ssh vagrant@127.0.0.1 -p 2222 -i <private_key file>
```

## ssh连接

在Vagrantfile配置文件中添加了两行代码，使用明文用户名密码

config.ssh.username = "vagrant"
config.ssh.password = "vagrant"

保存

vagrant reload