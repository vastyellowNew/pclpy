import pytest
import os
import numpy as np
import laspy

from pclpy import pcl
import pclpy


def test_data(*args):
    return os.path.join("test_data", *args)


def test_hi():
    assert pcl.__doc__


def test_size_xyz():
    a = np.random.ranf(30).reshape(-1, 3)
    p = pcl.PointCloudXYZ.from_array(a)
    assert p.size() == 10

#
# def test_voxel_grid_rgba(xyzrgba):
#     out = xyzrgba.voxel_grid(leaf_size=0.5)
#     assert out.size()
#     assert out.size() < xyzrgba.size()
#     assert isinstance(out, type(xyzrgba))
#
#
# def test_voxel_grid_xyz(xyz):
#     out = xyz.voxel_grid(leaf_size=0.5)
#     assert out.size()
#     assert out.size() < xyz.size()
#     assert isinstance(out, type(xyz))
#
#
# def test_approximate_voxel_grid_rgba(xyzrgba):
#     out = xyzrgba.approximate_voxel_grid(leaf_size=0.5)
#     assert out.size()
#     assert out.size() < xyzrgba.size()
#     assert isinstance(out, type(xyzrgba))
#
#
# def test_approximate_voxel_grid_xyz(xyz):
#     out = xyz.approximate_voxel_grid(leaf_size=0.5)
#     assert out.size()
#     assert out.size() < xyz.size()
#     assert isinstance(out, type(xyz))
#
#
# def test_sor_rgba(xyzrgba):
#     out = xyzrgba.sor(threshold=0.1, mean_k=2)
#     assert out.size()
#     assert out.size() < xyzrgba.size()
#     assert isinstance(out, type(xyzrgba))
#
#
# def test_sor_xyz(xyz):
#     out = xyz.sor(threshold=0.1, mean_k=2)
#     assert out.size()
#     assert out.size() < xyz.size()
#     assert isinstance(out, type(xyz))
#
#
# def test_extract_clusters_xyz(xyz):
#     clouds = xyz.extract_clusters(0.6, 2, 10)
#     assert clouds and clouds[0].size()
#
#
# def test_extract_clusters_xyzrgba(xyzrgba):
#     clouds = xyzrgba.extract_clusters(0.6, 2, 10)
#     assert clouds and clouds[0].size()
#
#
# def test_estimate_normals_xyz(xyz):
#     out = pcl.PointCloudPointNormal()
#     pn = xyz.estimate_normals(out, 0.6)
#     assert pn.size()
#
#
# def test_estimate_normals_xyzrgba(xyzrgba):
#     out = pcl.PointCloudPointNormal()
#     pn = xyzrgba.estimate_normals(out, 0.6)
#     assert pn.size()
#
#
# def test_convex_hull_xyz(xyz):
#     pn = xyz.convex_hull()
#     assert pn.size()
#     assert pn.size() < xyz.size()
#
#
# def test_convex_hull_xyzrgba(xyzrgba):
#     pn = xyzrgba.convex_hull()
#     assert pn.size()
#     assert pn.size() < xyzrgba.size()
#
#
# def test_concave_hull_xyz(xyz):
#     pn = xyz.concave_hull(0.8)
#     assert pn.size()
#     assert pn.size() < xyz.size()
#
#
# def test_concave_hull_xyzrgba(xyzrgba):
#     pn = xyzrgba.concave_hull(0.8)
#     assert pn.size()
#     assert pn.size() < xyzrgba.size()
#
#
# def test_crop_hull_xyz(xyz):
#     c = xyz.convex_hull()
#     pn = xyz.crop_hull(c)
#     assert pn.size()
#     assert pn.size() == xyz.size()
#
#
# def test_crop_hull_xyzrgba(xyzrgba):
#     c = xyzrgba.convex_hull()
#     pn = xyzrgba.crop_hull(c)
#     assert pn.size()
#     assert pn.size() == xyzrgba.size()


def test_io_las():
    pc = pclpy.io.read_las(test_data("street.las"))
    assert pc.size() == 1091656
    assert isinstance(pc, pcl.PointCloudXYZRGBA)


def test_make_kdtree():
    kdtree = pcl.kdtree.KdTreeFLANN.PointXYZ()
    assert kdtree