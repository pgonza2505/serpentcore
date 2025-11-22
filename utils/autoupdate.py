from __future__ import annotations

import subprocess
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent.parent


def auto_update() -> None:
    """Attempt to git pull on startup.
    
    - Skips if there are local changes.
    - Does not raise if git/network fails; just logs and continues.
    """
    try:
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_DIR,
            capture_output=True,
            text=True,
            check=False,
        )

        if status.stdout.strip():
            print("[autoupdate] Local changes detected, skipping git pull.")
            return
        
        print("[autoupdate] Pulling latest changes from origin...")
        result = subprocess.run(
            ["git", "pull", "--ff-only"],
            cwd=REPO_DIR,
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode == 0:
            print("[autoupdate] git pull completed.")
            if result.stdout.strip():
                print(result.stdout.strip())
        else:
            print("[autoupdate] git pull failed:")
            if result.stdout.strip():
                print("STDOUT:", result.stdout.strip())
            if result.stderr.strip():
                print("STDERR:", result.stderr.strip())
    
    except Exception as e:
        print(f"[autoupdate] Error while updating: {e}")