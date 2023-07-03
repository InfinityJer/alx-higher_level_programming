#include <Python.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: A pointer to the PyObject string object
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	Py_UNICODE *value;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p)) {
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	value = PyUnicode_AS_UNICODE(p);

	printf("  type: %s\n", Py_TYPE(p)->tp_name);
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", value);
}
