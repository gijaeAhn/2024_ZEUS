#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // For handling std::vector
#include "zeusKinematics.h"
#include "Transform.h"

namespace py = pybind11;

PYBIND11_MODULE(zeus_kinematics_solver, m) {
    m.def("mod_angle", &mod_angle, "Noimoprmalize an angle to the range [-PI, PI]");
    m.def("ARM6_kinematics_forward_arm", &ARM6_kinematics_forward_arm, "Pseudo forward kinematics for ZEUS series arm");
    m.def("ARM6_kinematics_forward_armReal", &ARM6_kinematics_forward_armReal,"Real forward kinematics for ZEUS series arm");
    m.def("ARM6_kinematics_inverse_arm", &ARM6_kinematics_inverse_arm, "Inverse kinematics for ZEUS series arm");
}
