import os
from pathlib import Path

path = os.path.expanduser('~')
print(path)

hm_path = Path.home()
print(hm_path / 'mlx')