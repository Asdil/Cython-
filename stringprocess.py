%%cython
from libc.stdlib cimport malloc, free
from libc.string cimport strcmp
from cpython.string cimport PyString_AsString

cdef char ** to_cstring_array(list_str):
    cdef char **ret = <char **>malloc(len(list_str) * sizeof(char *))
    for i in range(len(list_str)):
        ret[i] = PyString_AsString(list_str[i])
    return ret

cpdef list foo(list list_str1, list list_str2):
    cdef int len_str1 = len(list_str1)
    cdef int len_str2 = len(list_str2)
    cdef list ret = []
    cdef char **c_arr1 = to_cstring_array(list_str1)
    cdef char **c_arr2 = to_cstring_array(list_str2)
    assert len_str1 == len_str2
    for i in range(len_str1):
        if strcmp(c_arr1[i], c_arr2[i]) == 0:
            ret.append(0)
        else:
            ret.append(1)
    return ret
