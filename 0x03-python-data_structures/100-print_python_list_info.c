#include <stdio.h>
#include <Python.h>
/**
* print_python_list_info - prints some basic info about Python lists.
* @p: pointer to python list
* Return: void
*/

void print_python_list_info(PyObject *p)
{
	PyListObject *list_;
	long int i, size;

	list_ = (PyListObject *)p;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list_->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
