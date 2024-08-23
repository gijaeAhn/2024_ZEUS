#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // For converting between C++ STL and Python
#include "Transform.h"     // Include your header file

namespace py = pybind11;

PYBIND11_MODULE(transform, m) {
    // Bind the Transform class
    py::class_<Transform>(m, "Transform")
        .def(py::init<>())  // Constructor
        .def("clear", &Transform::clear)
        .def("translate", py::overload_cast<double, double, double>(&Transform::translate))
        .def("translate", py::overload_cast<const double *>(&Transform::translate))
        .def("translateX", &Transform::translateX, py::arg("x") = 0)
        .def("translateY", &Transform::translateY, py::arg("y") = 0)
        .def("translateZ", &Transform::translateZ, py::arg("z") = 0)
        .def("rotateX", &Transform::rotateX, py::arg("a") = 0)
        .def("rotateY", &Transform::rotateY, py::arg("a") = 0)
        .def("rotateZ", &Transform::rotateZ, py::arg("a") = 0)
        .def("rotateDotX", &Transform::rotateDotX, py::arg("a") = 0)
        .def("rotateDotY", &Transform::rotateDotY, py::arg("a") = 0)
        .def("rotateDotZ", &Transform::rotateDotZ, py::arg("a") = 0)
        .def("translateNeg", &Transform::translateNeg)
        .def("rotateDotXNeg", &Transform::rotateDotXNeg)
        .def("rotateDotYNeg", &Transform::rotateDotYNeg)
        .def("rotateDotZNeg", &Transform::rotateDotZNeg)
        .def("getVal", py::overload_cast<int,int>(&Transform::getVal))
        .def("mDH", &Transform::mDH)
        .def("apply", &Transform::apply)
        .def("apply0", &Transform::apply0)
        .def("getZ", py::overload_cast<>(&Transform::getZ))
        .def("getXYZ", &Transform::getXYZ)
        .def("__call__", py::overload_cast<int, int>(&Transform::operator()))
        .def("__call__", py::overload_cast<int, int>(&Transform::operator(), py::const_))
        .def_static("inv", &inv)
        .def_static("trcopy", &trcopy)
        .def_static("transform6D", &transform6D)
        .def_static("transformQuatP", &transformQuatP)
        .def_static("position6D", &position6D)
        .def_static("to_quatp", &to_quatp)
        .def_static("getAngularVelocityTensor", &getAngularVelocityTensor)
        .def_static("printTransform", &printTransform)
        .def_static("printVector", &printVector);
}
