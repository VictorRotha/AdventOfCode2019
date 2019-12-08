with open('input.txt', 'r') as f:
    pixels = f.readline().strip()

width, height = 25, 6
size = width * height

layer_num = len(pixels)//size

layers = []
for n in range(layer_num):
    layer = pixels[n*size:n*size+size]
    layers.append(layer)

min_zeros = size
min_layer = None
for layer in layers:
    if layer.count('0') < min_zeros:
        min_zeros = layer.count('0')
        min_layer = layer

print (f'Layer {min_layer} \nZeros {min_zeros}, Product12 {min_layer.count("1")*min_layer.count("2")}')

# PART 01: 1463


