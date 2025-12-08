import numpy as np

# np.isin()
# +++++++++++++++++++++++++
def how_np_isin():
    a = [1,2,3,4,5]
    b = [2,5]
    mask = np.isin(a,b)
    print(mask) 
    # [False  True False False  True]
    # print(a[mask])
    # TypeError: only integer scalar arrays 
    # can be converted to a scalar index

    c = np.array([1,2,3,4,5])
    d = [2,5]
    mask2 = np.isin(c,d)
    print(c[mask2])
    # [2 5]

    e = np.array([1,2,3,4,5])
    f = np.array([2,5])
    mask3 = np.isin(e,f)
    print(e[mask3])
    # [2 5]

# verschachtelte for loop
# +++++++++++++++++++++++++
def verschachtelte_for_loop():
    a = np.array([111,222,333,111,111])
    label_map = {111:0, 222:1, 333:1}
    c = np.array([label_map[v] for v in a])
    print(c)
    # [0 1 1 0 0]


# np.zeros()
# +++++++++++++++++++++++++++
def how_np_zeros():
    a = np.zeros((3,2))
    print(a)
    # [[0. 0.]
    #  [0. 0.]
    #  [0. 0.]]

    b = np.zeros(5)
    print(b)
    # [0. 0. 0. 0. 0.]

    c = np.zeros((3,3,3))
    print(c.ndim)
    # 3

# np.arange()
def how_np_arange():
    a = np.arange(7)
    print(a)
    # [0 1 2 3 4 5 6]

    b = np.arange(0,10,3)
    print(b)
    # [0 3 6 9]


def use_np_array_eigenschaft():
    a = np.array([0,1,2,3])
    b = np.zeros((4,5))
    print(b)
    b[a,1]=2
    print(b)
    """ [[0. 0. 0. 0. 0.]
        [0. 0. 0. 0. 0.]
        [0. 0. 0. 0. 0.]
        [0. 0. 0. 0. 0.]]
        
        [[0. 2. 0. 0. 0.]
        [0. 2. 0. 0. 0.]
        [0. 2. 0. 0. 0.]
        [0. 2. 0. 0. 0.]] """

def how_np_log():
    print(np.log(2.73)) # base is e)
    # np.float64(1.0043016091968684)
    print(np.log10(100))
    # np.float64(2.0)
    print(np.log2(4)) # base 2
    # np.float64(2.0)
    print(np.log1p(1.7)) 
    # base e, it calculates log(1+x)
    # np.float64(0.9932517730102833)

def max_maximum():

    a = max(1,2)
    print(a) # 2
    b = [1,2,3]
    c = [4,5,6]
    print(max(b,c)) # [4, 5, 6]
    d = np.array([b])
    e = np.array([c])
    f = np.maximum(d,e)
    print(f) # [[4 5 6]]
    print(type(f)) # <class 'numpy.ndarray'>
    print(f[0][1]) # 5


    # array([[0, 1],
    #       [2, 3]])
    a = np.arange(4).reshape((2,2))
    # array([2, 3])
    b = np.max(a, axis=0) 
    # array([1, 3])
    c = np.max(a, axis=1)
    d = np.max(a, axis=1, keepdims=True)
    print(d)
    # [[1]
    #  [3]]

    
def py_np_abs():
    print(-np.abs(10))
    print(-abs(10))



























