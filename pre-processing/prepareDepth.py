import os
for i in range(9999):
    try:
        os.popen(f"Ren {i}.png depth{i}.png").read()
    except:
        break