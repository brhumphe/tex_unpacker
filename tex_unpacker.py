import subprocess
from PIL import Image

in_file = "dds/Shared_Characters_DN_src.dds"
out_file = "out/Shared_Characters_DN_src.png"

subprocess.run(
    "./texassemble.exe h-strip "
    "{in_path}"
    " -o "
    "{out_path}"
    " -y -f R8G8B8A8_UNORM".format(in_path=in_file, out_path=out_file))

with Image.open(out_file) as cube:
    size = cube.size[1]
    print(size)
    for i in range(6):
        crop = (i * size, 0, i * size + size, size)
        print(crop)
        x_pos = cube.crop(crop)
        x_pos.save("out/Shared_Characters_DN_src_0" + str(i + 1) + ".png")
