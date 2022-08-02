import os
for i in range(9999):
#     # print(["Ren", f"{i}.jpg", f"img{i}.png"])
#     subprocess.run([f"Ren {i}.jpg img{i}.png"])
    try:
        os.popen(f"Ren {i}.jpg img{i}.png").read()
    except:
        break
# print()