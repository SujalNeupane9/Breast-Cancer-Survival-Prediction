from pathlib import Path
import os

PARENT_DIR = Path(__file__).parent.resolve().parent
DATA_DIR = PARENT_DIR / 'data'
MODEL_DIR = PARENT_DIR / 'model'

if not Path(DATA_DIR).exists():
    os.mkdir(DATA_DIR)

if not Path(MODELS_DIR).exists():
    os.mkdir(MODELS_DIR)
