### 查询一下manimgl的可用版本
```bash
(myenv-1.7.0) PS C:\Users\Administrator\Desktop\playfield\manim-test> pip index versions manimgl
WARNING: pip index is currently an experimental command. It may be removed/changed in a future release without prior warning.
manimgl (1.7.1)
Available versions: 1.7.1, 1.7.0, 1.6.1, 1.6.0, 1.5.0, 1.4.1, 1.4.0, 1.3.0, 1.2.0, 1.1.0, 1.0.0
  INSTALLED: 1.7.0
  LATEST:    1.7.1

[notice] A new release of pip is available: 23.0.1 -> 24.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(myenv-1.7.0) PS C:\Users\Administrator\Desktop\playfield\manim-test> 
```


### 用scoop 切换python版本
```bash
scoop list python
scoop reset python38
scoop reset python310

python --version
python -m venv myenv-1.7.1
.\myenv-1.7.1\Scripts\Activate.ps1

```


```bash

python --version
python -c "import sys; print(sys.executable)"
set PYTHONTRACE=1     # Windows

python -m venv myenv-1.7.1

C:\Users\Administrator\.pyenv\pyenv-win\versions\3.8.10\python -m venv myenv-1.7.1

.\myenv-1.7.1\Scripts\Activate.ps1


pyenv global 3.8.10
pyenv which python
pyenv which 3.8.10


scoop prefix python
scoop list python


cd C:\Users\Administrator\Desktop\playfield\manim-test\videos\_2017\nn
cd C:\Users\Administrator\Desktop\playfield\manim-test\videos  

pip index versions manimgl

pip install manimgl
pip install manimgl==
pip install opencv-python
pip install setuptools
pip install mapbox-earcut


$env:PYTHONPATH="C:/Users/Administrator/Desktop/playfield/manim-test/videos"
manimgl part1.py
manimgl part1.py NetworkScene -ow
```




### git

```bash
git log --oneline --all -- .
git log -- part1.py


```