#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    size = PyList_Size(p);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *bytes;
    int max_print = 10;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", bytes);

    printf("  first %d bytes:", (size < max_print ? (int)size : max_print));
    for (i = 0; i < (size < max_print ? size : max_print); i++)
        printf(" %02x", (unsigned char)bytes[i]);
    printf("\n");
}
