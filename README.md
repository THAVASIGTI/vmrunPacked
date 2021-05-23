# vmrunPacked

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/THAVASIGTI/vmrunPacked)
[![PyPI](https://img.shields.io/pypi/v/vmrunPacked)](https://pypi.org/project/vmrunPacked)
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

### Power Commands

In this Power command support
- start
- stop
- reset
- suspend
- pause
- unpause

# start
``` python
import vmrunPacked

vmobj = vmrunPacked.Pack("/vmx_file_path/vm.vmx",userName="admin",passWord="admin@123")
vmobj.start()

```
Starts a virtual machine (.vmx file) or team (.vmtm file). The default gui option starts the machine interactively, including startup dialog box, to allow noninteractive scripting.

# stop

stop command Parameters two `soft` and `hard`

``` python
vmobj.stop() #that call normal
vmobj.stop(soft=True) #that call soft "quick close" vm
vmobj.stop(hard=True) #that call hard "force close" vm
# Exception 
# vmobj.stop(soft=True,hard=True)
# tha case defualt "soft" parms call
```

# reset (reboot)

``` python
vmobj.reset() #that call normal
vmobj.reset(soft=True) #that call soft "quick close" vm
vmobj.reset(hard=True) #that call hard "force close" vm
# Exception 
# vmobj.reset(soft=True,hard=True)
# tha case defualt "soft" parms call
```

# suspend

``` python
vmobj.suspend() #that call normal
vmobj.suspend(soft=True) #that call soft "quick close" vm
vmobj.suspend(hard=True) #that call hard "force close" vm
# Exception 
# vmobj.suspend(soft=True,hard=True)
# tha case defualt "soft" parms call
```