from __future__ import absolute_import, division, print_function, unicode_literals
from .quantize import *
from .observer import *
from .qconfig import *
from .fake_quantize import *
from .fuse_modules import fuse_modules
from .stubs import *
from .quantize_jit import *

def default_eval_fn(model, calib_data):
    r"""
    Default evaluation function takes a torch.utils.data.Dataset or a list of
    input Tensors and run the model on the dataset
    """
    for data, target in calib_data:
        model(data)

_all__ = [
    'QuantWrapper', 'QuantStub', 'DeQuantStub',
    # Top level API for eager mode quantization
    'quantize', 'quantize_dynamic', 'quantize_qat',
    'prepare', 'convert', 'prepare_qat',
    # Top level API for graph mode quantization
    'quantize_jit', 'quantize_dynamic_jit',
    # Sub functions for `prepare` and `swap_module`
    'propagate_qconfig_', 'add_quant_dequant', 'add_observer_', 'swap_module',
    'default_eval_fn', 'get_observer_dict',
    'register_activation_post_process_hook',
    # Observers
    'ObserverBase', 'WeightObserver', 'observer', 'default_observer',
    'default_weight_observer',
    # QConfig
    'QConfig', 'default_qconfig', 'default_dynamic_qconfig', 'float16_dynamic_qconfig',
    # QAT utilities
    'default_qat_qconfig', 'prepare_qat', 'quantize_qat',
    # module transformations
    'fuse_modules',
]
