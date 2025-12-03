
frame = 0
sprites = ['img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8',]

for x in range(30):
    frame = (frame + 1) % len(sprites)

