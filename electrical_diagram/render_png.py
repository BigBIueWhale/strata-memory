#!/usr/bin/env python3
"""Render diagram.html -> diagram.png at high quality using a headless Chromium.

Finds the browser binary (Playwright cache first, then PATH), screenshots the
fixed 1720x1080 canvas at 2x device scale -> a crisp 3440x2160 PNG. No
third-party Python packages required.
"""
import glob, os, subprocess, sys
from shutil import which

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, "diagram.html")
PNG  = os.path.join(HERE, "diagram.png")
W, H, SCALE = 1720, 1080, 2   # must match the html/body size

def find_chrome():
    pats = [
        "~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome",
        "~/.cache/ms-playwright/chromium-*/chrome-linux/chrome",
        "~/.cache/ms-playwright/chromium_headless_shell-*/chrome-linux64/headless_shell",
    ]
    for p in pats:
        for hit in sorted(glob.glob(os.path.expanduser(p)), reverse=True):
            if os.path.exists(hit):
                return hit
    for name in ("google-chrome-stable", "google-chrome", "chromium", "chromium-browser"):
        p = which(name)
        if p:
            return p
    sys.exit("No Chromium/Chrome binary found.")

def main():
    chrome = find_chrome()
    if os.path.exists(PNG):
        os.remove(PNG)
    cmd = [
        chrome, "--headless", "--no-sandbox", "--disable-gpu",
        "--disable-dev-shm-usage", "--hide-scrollbars",
        f"--force-device-scale-factor={SCALE}",
        f"--window-size={W},{H}",
        f"--screenshot={PNG}",
        "file://" + HTML,
    ]
    print("chrome:", chrome)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.stderr.strip():
        print(r.stderr.strip()[-600:])
    if not os.path.exists(PNG):
        sys.exit("Render FAILED (no PNG produced).")
    print(f"OK -> {PNG}  ({os.path.getsize(PNG):,} bytes, target {W*SCALE}x{H*SCALE})")

if __name__ == "__main__":
    main()
