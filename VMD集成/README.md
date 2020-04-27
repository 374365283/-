
# VMD集成工作

## 工作进展 
获取vmd文件：

    git clone https://github.com/OSC/bc_osc_vmd.git
    
修改submit.yml.erb ，form.yml ，template

## 问题

使用VMD launch，打开可视化界面后，无法连上服务器。可能的解决方法：目前根据文档https://osc.github.io/ood-documentation/release-1.6/enable-desktops/software-requirements.html 参考desktop的部署方式，来部署VMD,参考jupyter/template/script.sh.erb中环境变量的部署方法。
