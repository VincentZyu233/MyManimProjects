import subprocess

# 使用Powershell运行python --version命令，并使用gbk编码输出结果
output = subprocess.check_output('powershell "python --version"', shell=True, encoding='gbk', universal_newlines=True)
print(output)