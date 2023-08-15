#include <Python.h>

/**
 * print_python_list_info - working with basic info about Python lists.
 * @p: PyObject pointer.
 */
void print_python_list_info(PyObject *p)
{
	int memorySize, memoryAlloc, j;
	PyObject *object;

	memorySize = Py_SIZE(p);
	memoryAlloc = ((PyListObject *)p)->allocated;

	printf("[*] Python List = %d\n", memorySize);
	printf("[*] Allocated memory = %d\n", memoryAlloc);

	for (j = 0; j < memorySize; j++)
	{
		printf("Object Element %d: ", j);

		object = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
