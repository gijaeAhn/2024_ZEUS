#include <pybind11/pybind11.h>


namespace py = pybind11;

int add(int i, int j) {  return i + j; }
int sub(int i, int j) {  return i - j; }


struct MyData
{
  float x, y;

  MyData() : x(0), y(0) { }
  MyData(float x, float y) : x(x), y(y) { }

  void print() { printf("%f, %f\n", x, y); }
};

PYBIND11_MODULE(example, m) {          // "example" module name should be same of module name in CMakeLists
  m.doc() = "pybind11 example plugin"; // optional module docstring

  m.def("add", &add, "A function that adds two numbers");
  m.def("sub", &sub, "A function that subtracts two numbers");

  py::class_<MyData>(m, "MyData")
    .def(py::init<>())
    .def(py::init<float, float>(), "constructor 2", py::arg("x"), py::arg("y"))
    .def("print", &MyData::print)
    .def_readwrite("x", &MyData::x)
    .def_readwrite("y", &MyData::y);
}
