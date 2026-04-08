import os
import os.path as osp
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

ROOT_DIR = osp.dirname(osp.abspath(__file__))

# Auto-detect GPU arch if not set
if not os.environ.get("TORCH_CUDA_ARCH_LIST"):
    import torch
    if torch.cuda.is_available():
        major, minor = torch.cuda.get_device_capability()
        os.environ["TORCH_CUDA_ARCH_LIST"] = f"{major}.{minor}"

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
        # removed optional=True — we WANT this to fail loudly
    ),
]

setup(
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension},
    zip_safe=False,
)