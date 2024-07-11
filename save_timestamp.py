from datetime import datetime
from pymol import cmd, stored

def save_timestamp(prefix):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fname = f"{stored.save_dir}/{prefix}_{now}.pse"
    cmd.save(fname)
    print(f"saved to {fname}")

cmd.extend("save_timestamp", save_timestamp)
