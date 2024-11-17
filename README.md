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

### manage python versions via scoop(windows)
```bash
scoop list python
scoop reset python38
scoop reset python310
```


### manage python versions via pyenv(linux)
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


pyenv install 3.10.0
pyenv install 3.9.7

# 切换到指定版本
pyenv global 3.10.0  # 设置全局 Python 版本
pyenv local 3.9.7   # 设置当前目录下的 Python 版本

pyenv versions
pyenv which system

```