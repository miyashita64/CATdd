"""ディレクトリをPythonのパッケージとして識別するための特別なファイル..

@author: miyashita
"""

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / "src"))
