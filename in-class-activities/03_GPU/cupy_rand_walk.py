import numpy as np
import cupy as cp
import time

def rand_walk_np(N):
    # each random walk has 100 random normal steps
    steps = np.random.normal(loc=0, scale=1, size=(N, 100))

    # each walk starts at 100 and then diverges based on randomly generated steps
    steps[:, 0] = 0
    r_walks = 100 + np.cumsum(steps, axis=0)

    average_finish = np.mean(r_walks[:, -1])
    std_finish = np.std(r_walks[:, -1])
    return average_finish, std_finish


def rand_walk_cp(N):
    # generate on GPU + use single precision floats
    steps_dev = cp.random.normal(loc=0, scale=1, size=(N, 100), dtype=np.float32)

    # perform cumulative sum, and reduction operations on GPU
    steps_dev[:, 0] = 0
    r_walks_dev = 100 + cp.cumsum(steps_dev, axis=0)

    average_finish_dev = cp.mean(r_walks_dev[:, -1])
    std_finish_dev = cp.std(r_walks_dev[:, -1])

    # Bring Average and standard deviation to CPU host
    average_finish = average_finish_dev.get()
    std_finish = std_finish_dev.get()
    return average_finish, std_finish

if __name__ == '__main__':
    N = 10 ** 6
    t0 = time.time()
    average_finish, std_finish = rand_walk_np(N)
    t1 = time.time()
    average_finish, std_finish = rand_walk_cp(N)
    t2 = time.time()

    print('1m runs')
    print('NumPy (s): ', t1 - t0, 'CuPy (s): ', t2 - t1)

    N = 10 ** 7
    t0 = time.time()
    average_finish, std_finish = rand_walk_np(N)
    t1 = time.time()
    average_finish, std_finish = rand_walk_cp(N)
    t2 = time.time()

    print('10m runs')
    print('Numpy (s): ', t1 - t0, 'CuPy (s): ', t2 - t1)
