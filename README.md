> a repo that backup all my manimce and manimgl projects

![keep_things_pure_and_joyful](keep_things_pure_and_joyful.png)


### git command

```bash
git init
git remote add origin git@github.com:VincentZyu233/MyManimProjects.git
git add .
git commit -m "重新整理一下"
git push -u origin main
git push --force origin main


git diff HEAD README.md
git diff HEAD README.md > tmp_diff.diff
git log -p README.md
git log -p README.md > tmp_log.txt


git clean -n -X
git clean -f -X
git clean -f -d
```

### python command
```bash
python --version
python -c "import sys; print(sys.executable)"
python -m venv venv-name

# in Windows PowerShell:
.\venv-name\Scripts\Activate.ps1

# in Linux or MacOS terminal:
source venv-name/bin/activate 
```

#### 本仓库使用的python版本
> Python 3.10.11

#### 虚拟环境命名规范
> 用_venv开头，不然太多了根本找不到
```bash
(_venv-linux) vincentzyu@vincentzyu:~/Documents/github-repo/MyManimProjects/my_manimce_products$ ls | grep _venv
_venv-linux
```

### pip command
```bash
pip index versions manim
pip show manim

pip install -r requirements.txt
pip freeze > requirements.txt

```

### manage python versions via scoop(Windows)
```bash
scoop list python
scoop reset python38
scoop reset python310
```


### manage python versions via pyenv(Linux)
```bash
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git


curl https://pyenv.run | bash

# 配置环境变量：
# 将以下内容添加到 ~/.bashrc 或 ~/.zshrc：
# export PATH="$HOME/.pyenv/bin:$PATH"
# eval "$(pyenv init --path)"
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"


source ~/.bashrc  
# 或 source ~/.zshrc


pyenv install 3.10.11

# 切换到指定版本
pyenv global 3.10.11  # 设置全局 Python 版本
pyenv local 3.10.11   # 设置当前目录下的 Python 版本

pyenv versions

```