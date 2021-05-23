# vmrunPacked

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![PyPI](https://img.shields.io/pypi/v/vmrunpacked.svg)](https://pypi.org/project/vmrunPacked)
[![downloads](https://img.shields.io/pypi/dm/vmrunpacked.svg)](https://pypistats.org/packages/vmrunpacked)

## Installation
```
pip install vmrunPacked
```
### About
python vmrun commands and actions execute `power` actions. `snapshot` actions. `recoard` actions. `guest os control` actions. `vprobe` actions. `general commands` actions

### Import Pkg

``` python
import vmrunPacked

vmobj = vmrunPacked.Pack("/vmx_file_path/vm.vmx",userName="admin",passWord="admin@123")
# "product" this prams defualt "ws" options ["fusion", "player"]
```
