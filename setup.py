import os.path as osp

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

ROOT_DIR = osp.dirname(osp.abspath(__file__))

try:
    ext_modules = [
        CUDAExtension(
            "svox.csrc",
            [
                "svox/csrc/svox.cpp",
                "svox/csrc/svox_kernel.cu",
                "svox/csrc/rt_kernel.cu",
                "svox/csrc/quantizer.cpp",
            ],
            include_dirs=[osp.join(ROOT_DIR, "svox", "csrc", "include")],
            optional=True,
        ),
    ]
except:
    import warnings

    warnings.warn("Failed to build CUDA extension")
    ext_modules = []

setup(
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension},
    zip_safe=False,
)
