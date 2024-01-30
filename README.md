##### deep_learning





##### 问题汇总

###### Vscode 中不显示 conda 环境变量名称

1、在 Trminal 中输入

```
conda init
```

2、重启 Terminal ，报错

```
无法加载文件 C:UsersusernameDocumentsWindowsPowerShellprofile.ps1，因为在此系统上禁止运行脚本。
```

3、使用管理员身份打开 Powershell ，命令行输入

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

后，输入 Y 然后回车

4、重启 vscode 中的 Terminal 即可



###### Pip 换源

切换到环境下，输入命令

```
pip config set global.index-url http://pypi.tuna.tsinghua.edu.cn/simple
```

































