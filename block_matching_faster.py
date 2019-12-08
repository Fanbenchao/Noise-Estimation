import numpy as np

def block_matching(img_clean,img_noisy):
    S = 5
    f = 7
    f2 = f**2
    nv = 16
    s = 7
    if img_clean.ndim < 3:
        img = img[:,:,np.newaxis]
        img_noisy = img_noisy[:,:,np.newaxis]
    img = np.pad(img_clean,((3,3),(3,3),(0,0)),'edge')
    img_noisy = np.pad(img_noisy,((3,3),(3,3),(0,0)),'edge')
    N = img.shape[0]-f+1
    M = img.shape[1]-f+1
    C = img.shape[2]
    r = np.arange(0,N,s)
    c = np.arange(0,M,s)
    L = N*M
    X = np.zeros((f2,L,C))
    X_noisy = np.zeros((f2,L,C))
    k = -1
    for i in range(f):
        for j in range(f):
            k = k+1
            blk = img[i:N+i,j:M+j,:]
            X[k,:,:] = blk.reshape(-1,C)
            blk1 = img_noisy[i:N+i,j:M+j,:]
            X_noisy[k,:,:] = blk1.reshape(-1,C)
    I = np.arange(L)
    I = I.reshape(N,M)
    pos_arr = np.zeros((nv,N*M,C),dtype = 'uint32')
    X = X.swapaxes(0,1)
    X_noisy = X_noisy.swapaxes(0,1)
#     i = 0
    block = {}
    for row in r:
        for col in c:
            index = row*M+col
            rmin = max(row-3,0)
            rmax = min(row+4,N)
            cmin = max(col-3,0)
            cmax = min(col+4,M)
            block[str(index)] = I[rmin:rmax,cmin:cmax].reshape(-1)
    for row in r:
        for col in c:
#             i = i+1
#             if i%10000 == 0:
#                 print(str(i)+'/'+str(M*N))
            off = row*M+col
            rmin = max(row-S*f,0)
            rmax = min(row+S*f+1,N)
            cmin = max(col-S*f,0)
            cmax = min(col+S*f+1,M)
            idx = I[rmin:rmax:s,cmin:cmax:s]
            idx = idx.reshape(-1)
            B = X[idx,:,:]
            v = X[off,:,:]
            dis = np.linalg.norm((B-v),axis = 1)/f2
            ind = np.argsort(dis,axis = 0)
            indc = idx[ind[:16,:]]
            pos_arr[:,block[str(off)],:] = indc[:,np.newaxis,:]
    return pos_arr.swapaxes(0,1),X,X_noisy,block