import os
import shutil

folder = input("Enter screenshot folder path: ")

destination = os.path.join(folder, "Organized_Screenshots")

os.makedirs(destination, exist_ok=True)

count = 0

for file in os.listdir(folder):

    if file.lower().endswith((".png", ".jpg", ".jpeg")):

        source = os.path.join(folder, file)

        target = os.path.join(destination, file)

        if os.path.isfile(source):
            shutil.move(source, target)
            count += 1

print(count, "images organized successfully!")