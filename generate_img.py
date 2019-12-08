import numpy as np

def generate_img(pos_arr,X,X_noisy,block,img_clean):
    noisy = (X_noisy-X)/255
    if img_clean.ndim < 3:
        img_clean = img_clean[:,:,np.axis]
    H,W,C= img_clean.shape
    block_noisy_std = np.zeros((H*W,C))
    block_noisy_mean = np.zeros((H*W,C))
    for key,value in block.items():
        for i in range(C): 
            block_noisy_std[value,i] = np.std(noisy[pos_arr[int(key),:,i],:,i])
            block_noisy_mean[value,i] = np.mean(noisy[pos_arr[int(key),:,i],:,i])
    block_noisy_std = block_noisy_std.reshape(H,W,C)
    block_noisy_mean = block_noisy_mean.reshape(H,W,C)
    new_img = img_clean/255 + np.random.normal(block_noisy_mean,block_noisy_std,block_noisy_std.shape)
    if new_img.min() < 0:
        low_clip = 0.0
    else:
        low_clip = new_img.min()
    if new_img.max() >1:
        high_clip = 1.0
    else: 
        high_clip = new_img.max()
    new_img = np.clip(new_img, low_clip, high_clip)
    new_img = np.uint8(new_img*255)
    return new_img,block_noisy_std,block_noisy_mean