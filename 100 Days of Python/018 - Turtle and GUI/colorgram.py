import colorgram

colors = colorgram.extract('witcher.jpg', 42)

color_list = []

for num in range(35):
    this_color = colors[num]
    rgb = this_color.rgb
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    color_tuple = (r, g, b)
    color_list.append(color_tuple)

print(color_list)
