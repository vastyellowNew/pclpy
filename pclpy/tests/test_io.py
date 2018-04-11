import pytest
import os
import numpy as np
import laspy

from pclpy import pcl
import pclpy


def test_data(*args):
    return os.path.join("test_data", *args)


def test_simple_io_pcd():
    pc = pcl.PointCloudXYZ()
    reader = pcl.io.PCDReader()
    reader.read(test_data("bunny.pcd"), pc, 0)
    assert pc.size() == 397