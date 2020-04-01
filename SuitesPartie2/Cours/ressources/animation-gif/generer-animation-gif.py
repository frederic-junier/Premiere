
import glob
import moviepy.editor as mpy

gif_name = 'sierpinski'
fps = 1
file_list = glob.glob('*.png') # Get all the pngs in the current directory
list.sort(file_list) # Sort the images by #, this may need to be tweaked for your use case
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('{}.gif'.format(gif_name), fps=fps)

