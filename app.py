from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Ensure the safeher package can be imported from the repo root.
import sys
sys.path.append(str(ROOT))

from safeher import app as safeher_app  # noqa: F401
