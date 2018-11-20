#include <Python.h>

PyDoc_STRVAR(
    mod_docstring, 
    "Demo extension module with a Python wrapper for the system(3) function");

static PyObject *demo_system(PyObject *self, PyObject *args){
    const char *command;
    int retval;

    /* Parse the given arguments: expect one string, convert to char* */
    if (!PyArg_ParseTuple(args, "s", &command)) {
        /* Error handling: if PyArg_ParseTuple returns zero, return NULL */
        return NULL;
    }

    /* Call the C function */
    retval = system(command);

    /* Return result as Python int (error handling built in) */
    return PyLong_FromLong(retval);
}

/* List of all methods in the module */
static PyMethodDef DemoMethods[] = {
    {"system",  demo_system, METH_VARARGS,
            PyDoc_STR("Execute a shell command.")},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

/* Module specification */
static struct PyModuleDef demo_module = {
   PyModuleDef_HEAD_INIT,
   "demo",          /* name of module */
   mod_docstring,   /* dosctring (may be NULL) */
   0,               /* size of per-interpreter state of the module */
   DemoMethods,     /* list of methods */
};


/* Module entrypoint */
PyMODINIT_FUNC
PyInit_demo(void)
{
    return PyModuleDef_Init(&demo_module);
}