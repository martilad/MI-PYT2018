import numpy
cimport numpy
cimport cython

cpdef int intmul(int a, int b):
    cdef int result
    result = a * b
    return result

@cython.boundscheck(False)
cpdef numpy.ndarray[numpy.int64_t, ndim=2] matmul(numpy.ndarray[numpy.int64_t, ndim=2] a,
                                                    numpy.ndarray[numpy.int64_t, ndim=2] b):
    cdef int n, m, p, i, k, j
    cdef numpy.int64_t x, y
    n = a.shape[0]
    m = a.shape[1]
    if b.shape[0] != m:
        raise ValueError('incompatible sizes')
    p = b.shape[1]
    cdef numpy.ndarray[numpy.int64_t, ndim=2] result = numpy.zeros((n, p), dtype=numpy.int64)
    for i in range(n):
        for j in range(p):
            for k in range(m):
                x = a[i, k]
                y = b[k, j]
                result[i, j] += x * y
    return result