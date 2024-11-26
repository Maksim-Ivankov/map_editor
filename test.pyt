# import matplotlib.pyplot as plt
# from PIL import Image
# import matplotlib.patches as mpatches

# im = Image.open('map_v_1.png')

# # Flip the .tif file so it plots upright
# im1 = im.transpose(Image.FLIP_TOP_BOTTOM)

# # Plot the image
# plt.imshow(im1)
# ax = plt.gca()

# # create a grid
# ax.grid(True, color='r', linestyle='--', linewidth=2)
# # put the grid below other plot elements
# ax.set_axisbelow(True)

# # Draw a box
# xy = 200, 200,
# width, height = 100, 100
# ax.add_patch(mpatches.Rectangle(xy, width, height, facecolor="none",
#     edgecolor="blue", linewidth=2))

# plt.draw()

# plt.show()





import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

from PIL import Image


# Open image file
image = Image.open('map_v_1.png')
my_dpi=200.

# Set up figure
fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
ax=fig.add_subplot(111)

# Remove whitespace from around the image
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

# Set the gridding interval: here we use the major tick interval
myInterval=300.
loc = plticker.MultipleLocator(base=myInterval)
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(loc)

# Add the grid
ax.grid(which='major', axis='both', linestyle='-', color='g')

# Add the image
ax.imshow(image)

# Find number of gridsquares in x and y direction
nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval)))
ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval)))




# # Save the figure
# fig.savefig('map_v_2.png')













