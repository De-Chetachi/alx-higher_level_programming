#include <Python.h>

/**
* print_python_bytes - print some basic info about
* Python lists and Python bytes objects
* @p: python object
* Return: void
*/

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	long int i, size, size_;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		bytes = (PyBytesObject *)p;
		size = bytes->ob_base.ob_size;
		size_ = size + 1;

		printf("  size: %ld\n", bytes->ob_base.ob_size);
		printf("  trying string: ");
		for (i = 0; i < size; i++)
			printf("%c", bytes->ob_sval[i]);
		printf("\n");
		if (size > 9)
		{
			size_ = 10;
		}
		printf("  first %ld bytes:", size_);

		for (i = 0; i < size_; i++)
			printf(" %02x", bytes->ob_sval[i] & 0xff);
		printf("\n");

	}
	else
		printf("[ERROR] Invalid Bytes Object");
}

/**
* print_python_list - prints some basic info about Python lists.
* @p: pointer to python list
* Return: void
*/

void print_python_list(PyObject *p)
{
	PyListObject *list_;
	int i, size;

	list_ = (PyListObject *)p;
	size = list_->ob_base.ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list_->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, list_->ob_item[i]->ob_type->tp_name);
	}
}
