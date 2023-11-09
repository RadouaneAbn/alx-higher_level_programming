#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - this function prints some
 *	info about Python bytes objects
 * @p: pointer to PyObject (list)
 */

void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *BUF = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &BUF, &size);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", BUF);
	if (size < 10)
		printf("  first %ld bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", BUF[i]);
	printf("\n");
}

/**
 * print_python_list - this is a function that prints some basic
 *	info about Python lists
 *
 * @p: pointer to PyObject (list)
 */

void print_python_list(PyObject *p)
{
	int list_size = PyList_Size(p), i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %lu\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
}
