import gaugan as gg
import os

directory = "G4N2"
i = 0
j = 0
style = 4

while True:
    if os.path.isdir(f"Processed{i}"):
        i += 1
    else:
        os.mkdir(f"Processed{i}")
        break

for filename in os.listdir(directory):
    with open(f'{directory}/{filename}', "rb") as fh:
        image = gg.processImage(fh.read(), style=4)

    with open(f'Processed{i}/output{j}.jpg', "wb") as fh:
        fh.write(image)

    j += 1
