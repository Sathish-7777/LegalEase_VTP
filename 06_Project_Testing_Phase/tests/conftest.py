import sys
from pathlib import Path

# make `import config`, `import ai_core`, `import legalEaseAPI` work from any folder
CODE_DIR = Path(__file__).resolve().parents[2] / "05_Project_Development_Phase"
sys.path.insert(0, str(CODE_DIR))
