# PCP监控信息 工作进展

## 部署过程：
首先安装pip，并用pip下载psutil库，s-tui：

     export http_proxy=http://proxy.pi.sjtu.edu.cn:3004/
     export https_proxy=http://proxy.pi.sjtu.edu.cn:3004/
     wget https://files.pythonhosted.org/packages/c2/f7/c7b501b783e5a74cf1768bc174ee4fb0a8a6ee5af6afa92274ff964703e0/setuptools-40.8.0.zip
     wget https://files.pythonhosted.org/packages/4c/4d/88bc9413da11702cbbace3ccc51350ae099bb351febae8acc85fec34f9af/pip-19.0.2.tar.gz
     unzip setuptools-40.8.0.zip
     tar xvf pip-19.0.2.tar.gz
     cd setuptools-40.8.0
     python setup.py install
     cd ..
     cd pip-19.0.2
     python setup.py install
     cd ..
     yum install gcc python-devel
     pip install psutil s-tui
     
用yum下载pcp：

     yum install pcp pcp-devel 
     cd /var/lib/pcp/pmdas/simple
     
进入simple目录后，修改pmns，修改监控信息的名字：

     simple {
         numfetch    SIMPLE:0:0
         color       SIMPLE:0:1
         time
         cputemperature              SIMPLE:2:4
         powerconsumption            SIMPLE:2:5
         fanspeed                    SIMPLE:2:6
     }

     simple.time {
         user        SIMPLE:1:2
         sys         SIMPLE:1:3
     }
    
           
根据附件pmdasimple.python修改pmdasimple.python。
安装过程：

       ./Remove
       ./Install
       python
使用：
       
       pmval simple.cputemperature
       pmval simple.fanspeed
       pmval simple.powerconsumption
