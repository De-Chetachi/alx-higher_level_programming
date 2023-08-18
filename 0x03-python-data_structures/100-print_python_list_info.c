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
	int i, size;

	list_ = (PyListObject *)p;
	size = list_->ob_base.ob_size;

	printf("[*] Size of the Python List = %ld\n", list_->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list_->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, list_->ob_item[i]->ob_type->tp_name);
	}
}
