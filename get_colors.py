from PIL import Image
import collections

img = Image.open('public/images/logos/Logo-Catedra-EMACSA-.jpg').convert('RGB')
img = img.resize((300, 300))
colors = img.getdata()

counts = collections.Counter(colors)
# Filter out light colors and greys
valid_colors = []
for color, count in counts.most_common():
    if sum(color) < 700 and max(color) - min(color) > 30:
        valid_colors.append((color, count))

for color, count in valid_colors[:10]:
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x} - {count} pixels")
