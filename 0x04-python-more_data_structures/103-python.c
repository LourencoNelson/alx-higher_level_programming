#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    char *data;
    Py_ssize_t size, i;

    if (!PyBytes_Check(p))
    {
        printf("Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    data = PyBytes_AsString(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", data);
    printf("  first %ld bytes:", size < 10 ? size : 10);

    for (i = 0; i < size && i < 10; i++)
        printf(" %02x", (unsigned char)data[i]);
    puts("");
}
