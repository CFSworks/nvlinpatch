from .signature import *
from .patch import Patch
from .version import Version
from .patcher import Patcher, PatchError
from .scanner import Scanner

# PATCHES
uncap_pclk_dvi_64 = Patch('uncap_pclk_dvi_64',
                          sig_hex('C7 86 ?? ?? 00 00 80 1A 06 00'),
                          sig_hex('?? ?? ?? ?? ?? ?? FF FF FF 7F'), True)

uncap_pclk_dp_64 = Patch('uncap_pclk_dp_64',
                         sig_hex('C7 86 ?? ?? 00 00 60 3D 08 00'),
                         sig_hex('?? ?? ?? ?? ?? ?? FF FF FF 7F'), True)

uncap_pclk_fermi_64 = Patch('uncap_pclk_fermi_64',
                            sig_hex('25 80 1A 06 00'),
                            sig_hex('90 90 90 90 90'))


# VERSIONS
versions = []

v = Version('331.17_64', sig_raw('NVIDIA UNIX x86_64 Kernel Module  331.17'))
v.add_patch(uncap_pclk_dvi_64)
v.add_patch(uncap_pclk_dp_64)
v.add_patch(uncap_pclk_fermi_64)
versions.append(v)

v = Version('331.13_64', sig_raw('NVIDIA UNIX x86_64 Kernel Module  331.13'))
v.add_patch(uncap_pclk_dvi_64)
v.add_patch(uncap_pclk_dp_64)
v.add_patch(uncap_pclk_fermi_64)
versions.append(v)

v = Version('325.15_64', sig_raw('NVIDIA UNIX x86_64 Kernel Module  325.15'))
v.add_patch(uncap_pclk_dvi_64)
v.add_patch(uncap_pclk_dp_64)
v.add_patch(uncap_pclk_fermi_64)
versions.append(v)

v = Version('325.08_64', sig_raw('NVIDIA UNIX x86_64 Kernel Module  325.08'))
v.add_patch(uncap_pclk_dvi_64)
v.add_patch(uncap_pclk_dp_64)
v.add_patch(uncap_pclk_fermi_64)
versions.append(v)

v = Version('319.32_64', sig_raw('NVIDIA UNIX x86_64 Kernel Module  319.32'))
v.add_patch(uncap_pclk_dvi_64)
v.add_patch(uncap_pclk_dp_64)
v.add_patch(uncap_pclk_fermi_64)
versions.append(v)

v = Version('319.23_64', sig_raw('NVIDIA UNIX x86_64 Kernel Module  319.23'))
v.add_patch(uncap_pclk_dvi_64)
v.add_patch(uncap_pclk_dp_64)
v.add_patch(uncap_pclk_fermi_64)
versions.append(v)

v = Version('319.17_64', sig_raw('NVIDIA UNIX x86_64 Kernel Module  319.17'))
v.add_patch(uncap_pclk_dvi_64)
v.add_patch(uncap_pclk_dp_64)
v.add_patch(uncap_pclk_fermi_64)
versions.append(v)

v = Version('310.19_64', sig_raw('NVIDIA UNIX x86_64 Kernel Module  310.19'))
v.add_patch(uncap_pclk_dvi_64)
v.add_patch(uncap_pclk_fermi_64)
versions.append(v)

def detect_version(file):
    s = Scanner()
    for v in versions:
        s.add_signature(v)
    results = list(s.scan(file))
    if len(results) != 1:
        return None
    return results[0][1]

def main(file, ver=None):
    if ver is None:
        print 'Detecting version...'
        version = detect_version(file)
        if version is None:
            print 'Could not detect version!'
            return 1
    else:
        for v in versions:
            if v.ver == ver:
                version = v
                break
        else:
            print 'Unrecognized version %s' % ver
            return 1

    print 'Version: ' + version.ver

    p = Patcher()
    for patch in version._patches:
        p.add_patch(patch)
    print 'Patching...'
    try:
        p.patch(file)
    except PatchError as e:
        print 'Error: %s' % e.message
        return 1

    return 0
