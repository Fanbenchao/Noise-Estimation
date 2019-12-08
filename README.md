# Noise-Estimation
noise estimation with non-local methods
this algorithm is for raw image noise estimation. As the format of raw image is RGGB, I use img_clip_merge.py split the original image into 4 channels for noise estimation and final merge together respectively. If you use a RGB image as input, you can simple modify img_clip_merge.py properly.
I provide 3 styles noise estimation methods: 
block_matching_slow.ipynb: move stride is 1
block_matching_faster2.ipynb: move stride is 3
block_matching_faster1.ipynb: move stride is 7
you can select one of these versions suit for your application.
some extra function:
label_data.ipynb: simpy seperate run script and some useful function
block_matching_faster.py: block matching with stride 7
img_clip_merge.py: preprocess raw image and postprocess raw image
generate_img.py: generate noise image using estimation niose
