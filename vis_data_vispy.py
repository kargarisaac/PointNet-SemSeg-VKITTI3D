# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:28:39 2018

@author: Isaac
"""

# -*- coding: utf-8 -*-
# vispy: gallery 10
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

""" Demonstrates use of visual.Markers to create a point cloud with a
standard turntable camera to fly around with and a centered 3D Axis.
"""

import numpy as np
import vispy.scene
from vispy.scene import visuals
import h5py

#
# Make a canvas and add simple view
#
canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()


# generate data

point_cloud = np.load('./data/vkitti3d_dataset_v1.0/01/0001_00000.npy')  # shape: (401326, 7)
data1 = point_cloud[:,:6]
label1 = point_cloud[:,-1]

#%%
# create scatter object and fill in the data
scatter = visuals.Markers()
ind = 15

rgb_codes = [[255,0,0],
            [255,255,0],
            [255,0,255],
            [0,0,255],
            [0,255,0],
            [0,255,255],
            [100,100,100],
            [255,30,50],
            [25,180,60],
            [5,220,100],
            [25,100,200],
            [105,60,90],
            [150,0,190]]

color = np.zeros((label1[ind].shape[0], 3))
for i in range(label1.shape[1]):
    color[i,:] = [code/255 for code in rgb_codes[label1[ind, i]]]    

scatter.set_data(data1[ind][:,:3], edge_color=None, face_color=color, size=5)

view.add(scatter)

view.camera = 'turntable'  # or try 'arcball'

# add a colored 3D axis for orientation
axis = visuals.XYZAxis(parent=view.scene)

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1:
        vispy.app.run()
