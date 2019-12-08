# Noise-Estimation
noise estimation with non-local methods
<p>this algorithm is for raw image noise estimation. As the format of raw image is RGGB, I use img_clip_merge.py split the original image into 4 channels for noise estimation and final merge together respectively. If you use a RGB image as input, you can simple modify img_clip_merge.py properly.</p>
<p>I provide 3 styles noise estimation methods:</p> 
<p>block_matching_slow.ipynb: move stride is 1</p>
<p>block_matching_faster2.ipynb: move stride is 3</p>
<p>block_matching_faster1.ipynb: move stride is 7</p>
<p>you can select one of these versions suit for your application.</p>
<p>some extra function:</p>
<p>label_data.ipynb: simpy seperate run script and some useful function</p>
<p>block_matching_faster.py: block matching with stride 7</p>
<p>img_clip_merge.py: preprocess raw image and postprocess raw image</p>
<p>generate_img.py: generate noise image using estimation niose</p>
