import subprocess
from PIL import Image

in_file = "dds/Weapons_NC_Doku_DN_src.dds"
out_file = "out/Weapons_NC_Doku_DN_src.png"

output = subprocess.call(
    f"./texassemble.exe h-strip {in_file} -o {out_file} -y -f R8G8B8A8_UNORM")

# print(output.args)

with Image.open(out_file) as cube:
    size = cube.size[1]
    print(size)
    for i in range(6):
        crop = (i * size, 0, i * size + size, size)
        print(crop)
        x_pos = cube.crop(crop)
        # TODO: Strip the name from the path of in_file instead of providing a separate filename
        x_pos.save("out/Weapons_NC_Doku_DN_src_0" + str(i + 1) + ".png")
