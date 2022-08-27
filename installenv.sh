#!/bin/bash
eval "$(command conda 'shell.bash' 'hook' 2> /dev/null)"
rm -rf env_deep/
conda create --prefix env_deep/ python=3.8 -y
conda activate env_deep/

pip install pybind11
pip install Pillow
pip install plyfile
pip install tqdm
pip install scikit-image
