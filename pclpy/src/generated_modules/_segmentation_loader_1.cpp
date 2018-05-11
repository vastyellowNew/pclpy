
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pcl/point_types.h>

namespace py = pybind11;
using namespace pybind11::literals;

PYBIND11_DECLARE_HOLDER_TYPE(T, boost::shared_ptr<T>);
#include "../make_opaque_vectors.hpp"

#include "segmentation/extract_polygonal_prism_data.hpp"
#include "segmentation/grabcut_segmentation.hpp"
#include "segmentation/min_cut_segmentation.hpp"


void defineSegmentationClasses1(py::module &m) {
    py::module m_segmentation = m.def_submodule("segmentation", "Submodule segmentation");
    defineSegmentationExtractPolygonalPrismDataClasses(m_segmentation);
    defineSegmentationGrabcutSegmentationClasses(m_segmentation);
    defineSegmentationMinCutSegmentationClasses(m_segmentation);
}