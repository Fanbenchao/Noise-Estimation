import numpy as np
def img_clip_merge(img,img_noisy):
    H,W = img.shape
    img1 = img[0:H:2,0:W:2]
    img_noisy1 = img_noisy[0:H:2,0:W:2]
    img2 = img[0:H:2,1:W:2]
    img_noisy2 = img_noisy[0:H:2,1:W:2]
    img3 = img[1:H:2,0:W:2]
    img_noisy3 = img_noisy[1:H:2,0:W:2]
    img4 = img[1:H:2,1:W:2]
    img_noisy4 = img_noisy[1:H:2,1:W:2]
    img1 = img1[:,:,np.newaxis]
    img2 = img2[:,:,np.newaxis]
    img3 = img3[:,:,np.newaxis]
    img4 = img4[:,:,np.newaxis]
    img_noisy1 = img_noisy1[:,:,np.newaxis]
    img_noisy2 = img_noisy2[:,:,np.newaxis]
    img_noisy3 = img_noisy3[:,:,np.newaxis]
    img_noisy4 = img_noisy4[:,:,np.newaxis]
    img_merge = np.concatenate((img1,img2,img3,img4),axis = -1)
    img_noisy_merge = np.concatenate((img_noisy1,img_noisy2,img_noisy3,img_noisy4),axis = -1)
    return img_merge,img_noisy_merge

def merge(new_img,block_noisy_std,block_noisy_mean,shape):
    H,W = shape
    img = np.zeros((H,W))
    img[0:H:2,0:W:2] = new_img[:,:,0]
    img[0:H:2,1:W:2] = new_img[:,:,1]
    img[1:H:2,0:W:2] = new_img[:,:,2]
    img[1:H:2,1:W:2] = new_img[:,:,3]
    noisy_std = np.zeros((H,W))
    noisy_mean = np.zeros((H,W))
    noisy_std[0:H:2,0:W:2] = block_noisy_std[:,:,0]
    noisy_std[0:H:2,1:W:2] = block_noisy_std[:,:,1]
    noisy_std[1:H:2,0:W:2] = block_noisy_std[:,:,2]
    noisy_std[1:H:2,1:W:2] = block_noisy_std[:,:,3]
    noisy_mean[0:H:2,0:W:2] = block_noisy_mean[:,:,0]
    noisy_mean[0:H:2,1:W:2] = block_noisy_mean[:,:,1]
    noisy_mean[1:H:2,0:W:2] = block_noisy_mean[:,:,2]
    noisy_mean[1:H:2,1:W:2] = block_noisy_mean[:,:,3]
    return img,noisy_std,noisy_mean