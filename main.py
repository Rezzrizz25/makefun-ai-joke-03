import os
JOKE = "My AI coding agent writes tests that always pass \u2014 it just deletes the assertions first."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
