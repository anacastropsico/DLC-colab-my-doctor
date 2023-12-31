# -*- coding: utf-8 -*-
"""MY PROJECT DLC DOUTORADO

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZbulHcV00tCrO3cyoffU0aZt-Y5Voo-b
"""

import tensorflow as tf

from google.colab import drive

drive.mount ('/content/drive')

!pip install deeplabcut

#TESTAR
!pip install --upgrade deeplabcut

#tESTAR
!pip install 'deeplabcut'==2.3rc3

import os

# Commented out IPython magic to ensure Python compatibility.
os.environ ['DLClight'] = 'True'
os.environ ['Colab'] = 'True'
# %cd /content/drive/My Drive/DLC/AP/

import os
import deeplabcut
drive_path = '/content/drive/My Drive/DLC/AP/config.yaml'

"""%% TREINAR A REDE"""

import os
import deeplabcut
drive_path = '/content/drive/My Drive/DLC/AP/config.yaml'
deeplabcut.create_training_dataset (drive_path, augmenter_type='imgaug')

import deeplabcut #OPCIONAL (NÃO RODEI NO PROJETO)

train_pose_config, _ = deeplabcut.return_train_network_path(drive_path)
augs = {
    "gaussian_noise": True,
    "elastic_transform": True,
    "rotation": 180,
    "covering": True,
    "motion_blur": True,
}
deeplabcut.auxiliaryfunctions.edit_config(
    train_pose_config,
    augs,
)

import os
import deeplabcut
drive_path = '/content/drive/My Drive/DLC/AP/config.yaml'



deeplabcut.train_network (drive_path, allow_growth=True, max_snapshots_to_keep=8, saveiters=10000, maxiters=500000)

"""%% AVALIAR REDE TREINADA"""

import os
import deeplabcut
drive_path = '/content/drive/My Drive/DLC/AP/config.yaml'
deeplabcut.evaluate_network(drive_path,Shuffles=[1], plotting="bodypart", show_errors = True , comparaçãobodyparts = 'all' , rescale = False )

"""#plotar os mapas de pontuação, camadas locref e PAFs:"""

import os
import deeplabcut
drive_path = '/content/drive/My Drive/DLC/AP/config.yaml'
deeplabcut.extract_save_all_maps(drive_path, shuffle=1, Indices=[0, 5])

"""não lembro o que é

% CONVERTER VÍDEOS (opicional)
"""

ffmpeg -i "path_to_video" -c:v h264 -crf 18 -preset fast "output_path"

"""%% ANALYSE VIDEO"""

import os
import deeplabcut
drive_path = '/content/drive/My Drive/DLC/AP/config.yaml'
deeplabcut.analyze_videos(drive_path, [
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A4.mp4',





   ], videotype='mp4', robust_nframes=bool, shuffle=1, save_as_csv = True, destfolder= '/content/drive/My Drive/DLC/AP/VideosIV' )

"""%Filtro track"""

import os
import deeplabcut
drive_path = '/content/drive/My Drive/DLC/AP/config.yaml'
deeplabcut.filterpredictions(drive_path, [
                                      '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A4.mp4',
   ], videotype='mp4',
     filtertype= 'arima',ARdegree=3,MAdegree=1)

"""%Plot track"""

import os
import deeplabcut
drive_path = '/content/drive/My Drive/DLC/AP/config.yaml'
deeplabcut.plot_trajectories(drive_path,
                                      ['/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR7DIS75A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR4DIS25A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR3DIS75A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50A4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50A4.mp4',
   ], filtered=True)

"""%% Videos Rotulados"""

import os
import deeplabcut
drive_path = '/content/drive/My Drive/DLC/AP/config.yaml'
deeplabcut.create_labeled_video(drive_path, [
                                      '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T3.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR10DIS25T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR9DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T2.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR8DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR2DIS50T1.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T4.mp4',
                                       '/content/drive/My Drive/DLC/AP/VideosIV/IVR1DIS50T1.mp4',
],
     trailpoints=10, draw_skeleton = True, filtered=True, keypoints_only=True)

save_frames=True OR keypoints_only=True   # Dobrar RAN ->  [1]*10**10

deeplabcut.analyzeskeleton(config, video, videotype='avi', shuffle=1, trainingsetindex=0, save_as_csv=False, destfolder=None)

"""%Refinamento de frames outlier

"""



deeplabcut.extract_outlier_frames(drive_path, [
                                               '/content/drive/My Drive/DLC/AP/VIDEOS/IIR1DIS75A1.mp4'],  videotype= '.mp4', outlieralgorithm='manual')

"""#outlieralgorithm:'fitting', 'jump', or 'uncertain'`` #outlieralgorithm='manual')

REfinando os labes
"""

deeplabcut.refine_labels(drive_path)

"""Mesclar conjunto de dados"""

deeplabcut.merge_datasets(drive_path)

"""DEPOIS VOLTAR PARA AVALIAR A REDE, EM SEGUIDA ANALISAR OS VIDEOS

%CODIGO EXEMPLO PRA AVALIAR DISTÂNCIA ENTE DUAS BODY PARTS.
"""

import numpy as np
import pandas as pd

min_dist = 75.59
df = pd.read_hdf('/content/drive/My Drive/Teste_DLC/VIDEOS/NOR1T1-R1G1DLC_dlcrnetms5_new_projetOct24shuffle1_105000_el_filtered.h5' )
bpt1 = df.xs('part_1', level='bodyparts', axis=1).to_numpy()
bpt2 = df.xs('part_2', level='bodyparts', axis=1).to_numpy()
bpt3 = df.xs('part_3', level='bodyparts', axis=1).to_numpy()
bpt4 = df.xs('part_4', level='bodyparts', axis=1).to_numpy()
bpt5 = df.xs('fucinho', level='bodyparts', axis=1).to_numpy()
# We calculate the vectors from a point to the other
# and group them per frame and per animal.
try:
    diff1 = (bpt1 - bpt5).reshape((len(df), -1, 2))
    diff2 = (bpt2 - bpt5).reshape((len(df), -1, 2))
    diff3 = (bpt3 - bpt5).reshape((len(df), -1, 2))
    diff4 = (bpt4 - bpt5).reshape((len(df), -1, 2))
except ValueError:
    diff1 = (bpt1 - bpt5).reshape((len(df), -1, 3))
    diff2 = (bpt2 - bpt5).reshape((len(df), -1, 3))
    diff3 = (bpt3 - bpt5).reshape((len(df), -1, 3))
    diff4 = (bpt4 - bpt5).reshape((len(df), -1, 3))

dist1 = np.linalg.norm(diff1, axis=2)
mask1 = np.any(dist1 <= min_dist, axis=1)
dist2 = np.linalg.norm(diff2, axis=2)
mask2 = np.any(dist2 <= min_dist, axis=1)
dist3 = np.linalg.norm(diff3, axis=2)
mask3 = np.any(dist3 <= min_dist, axis=1)
dist4 = np.linalg.norm(diff4, axis=2)
mask4 = np.any(dist4 <= min_dist, axis=1)

flagged_frames1 = df.iloc[mask1].index
flagged_frames2 = df.iloc[mask2].index
flagged_frames3 = df.iloc[mask4].index
flagged_frames4 = df.iloc[mask4].index