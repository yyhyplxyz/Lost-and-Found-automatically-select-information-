'''
import numpy as np
import PIL
import os
from PIL import Image
alltext = []
for file in os.listdir("text_pics"):
    if file.endswith(".png"):
        alltext.append("text_pics/"+file)

images = map(Image.open,alltext)
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test.jpg')
'''
import numpy as np
import PIL
import os
from PIL import Image
list_im = []
for file in os.listdir("text_pics"):
    if file.endswith(".png"):
        list_im.append("text_pics/"+file)
imgs    = [ PIL.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'Trifecta.jpg' )

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'Trifecta_vertical.jpg' )
