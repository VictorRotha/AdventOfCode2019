
with open('input.txt', 'r') as f:
    pixels = f.readline().strip()

width, height = 25, 6
size = width * height

layers = []
for n in range(len(pixels)//size):
    layer = pixels[n*size:n*size+size]
    layers.append(layer)

# PART 01
min_zeros = size
min_layer = None
for layer in layers:
    if layer.count('0') < min_zeros:
        min_zeros = layer.count('0')
        min_layer = layer
print (f'Layer {min_layer} \nZeros {min_zeros}, Product12 {min_layer.count("1")*min_layer.count("2")}')
# PART 01: 1463

# PART 02
image = ''
for pos in range(size):
    layer_num = 0
    while True:
        pixel = layers[layer_num][pos]
        if not pixel == '2':
            image += pixel
            break
        layer_num += 1

for n in range(height):
    row = image[n*width:n*width + width]
    for char in row:
        char = '1 ' if char == '1' else '  '
        print(char, end='')
    print()

# PART 02: GKCKH








