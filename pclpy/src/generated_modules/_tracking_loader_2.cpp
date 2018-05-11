
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pcl/point_types.h>

namespace py = pybind11;
using namespace pybind11::literals;

PYBIND11_DECLARE_HOLDER_TYPE(T, boost::shared_ptr<T>);
#include "../make_opaque_vectors.hpp"

#include "tracking/tracker.hpp"
#include "tracking/particle_filter.hpp"
#include "tracking/kld_adaptive_particle_filter.hpp"


void defineTrackingClasses2(py::module &m) {
    py::module m_tracking = m.def_submodule("tracking", "Submodule tracking");
    defineTrackingTrackerClasses(m_tracking);
    defineTrackingParticleFilterClasses(m_tracking);
    defineTrackingKldAdaptiveParticleFilterClasses(m_tracking);
}