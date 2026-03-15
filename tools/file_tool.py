import os
from datetime import datetime

def save_report(topic: str, content: str) -> str:
    os.makedirs("outputs", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"outputs/SDG_{topic.replace(' ','_')}_{ts}.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[FILE TOOL] Saved: {fname}")
    return fname
