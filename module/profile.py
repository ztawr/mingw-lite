import argparse
from packaging.version import Version
from typing import Dict, Optional
class BranchVersions:
  gcc: str
  rev: str

  mcfgthread: str
  mingw: str

  binutils: str
  expat: str
  gdb: str
  gmp: str
  iconv: str
  make: str
  mpc: str
  mpfr: str
  pdcurses: str
  pkgconf: str
  python: str
  z: str

  xmake = '3.0.1'

  def __init__(
    self,

    gcc: str,
    rev: str,

    mcfgthread: str,
    mingw: str,

    binutils: str,
    expat: str,
    gdb: str,
    gmp: str,
    iconv: str,
    make: str,
    mpc: str,
    mpfr: str,
    pdcurses: str,
    pkgconf: str,
    python: str,
    z: str,
  ):
    self.gcc = gcc
    self.rev = rev

    self.mcfgthread = mcfgthread
    self.mingw = mingw

    self.binutils = binutils
    self.expat = expat
    self.gdb = gdb
    self.gmp = gmp
    self.iconv = iconv
    self.make = make
    self.mpc = mpc
    self.mpfr = mpfr
    self.pdcurses = pdcurses
    self.pkgconf = pkgconf
    self.python = python
    self.z = z

class ProfileInfo:
  arch: str
  fpmath: Optional[str]
  march: str
  target: str
  optimize_for_size: bool

  default_crt: str
  exception: str
  thread: str

  win32_winnt: int
  min_os: Version

  def __init__(
    self,

    arch: str,
    fpmath: Optional[str],
    march: str,
    target: str,
    optimize_for_size: bool,

    default_crt: str,
    exception: str,
    thread: str,

    win32_winnt: int,
    min_os: Version,
  ):
    self.arch = arch
    self.fpmath = fpmath
    self.march = march
    self.target = target
    self.optimize_for_size = optimize_for_size

    self.default_crt = default_crt
    self.exception = exception
    self.thread = thread

    self.win32_winnt = win32_winnt
    self.min_os = min_os

class BranchProfile(BranchVersions):
  arch: str
  fpmath: Optional[str]
  march: str
  target: str
  optimize_for_size: bool

  default_crt: str
  exception: str
  thread: str

  win32_winnt: int
  min_os: Version
  min_winnt: int

  def __init__(
    self,
    ver: BranchVersions,
    info: ProfileInfo,
  ):
    BranchVersions.__init__(self, **ver.__dict__)

    self.arch = info.arch
    self.fpmath = info.fpmath
    self.march = info.march
    self.target = info.target
    self.optimize_for_size = info.optimize_for_size

    self.default_crt = info.default_crt
    self.exception = info.exception
    self.thread = info.thread

    self.win32_winnt = info.win32_winnt
    self.min_os = info.min_os

    if info.min_os.major < 4:
      self.min_winnt = 0x0400
    else:
      self.min_winnt = info.min_os.major * 0x100 + info.min_os.minor

BRANCHES: Dict[str, BranchVersions] = {
  '16': BranchVersions(
    gcc = '16-20251012',
    rev = '1',

    mcfgthread = '2.2-ga.1',
    mingw = '13.0.0',

    binutils = '2.45',
    expat = '2.7.2',
    gdb = '16.3',
    gmp = '6.3.0',
    iconv = '1.18',
    make = '4.4.1',
    mpc = '1.3.1',
    mpfr = '4.2.2',
    pdcurses = '3.9',
    pkgconf = '2.5.1',
    python = '3.13.7',
    z = '1.3.1',
  ),
  '15': BranchVersions(
    gcc = '15.2.0',
    rev = '4',

    # ABI critical: 2025-08-08
    mcfgthread = '2.2-ga.1',
    mingw = '13.0.0',

    binutils = '2.45',
    expat = '2.7.2',
    gdb = '16.3',
    gmp = '6.3.0',
    iconv = '1.18',
    make = '4.4.1',
    mpc = '1.3.1',
    mpfr = '4.2.2',
    pdcurses = '3.9',
    pkgconf = '2.5.1',
    python = '3.13.7',
    z = '1.3.1',
  ),
  '14': BranchVersions(
    gcc = '14.3.0',
    rev = '4',

    # ABI critical: 2024-08-01
    mcfgthread = '2.2-ga.1',
    mingw = '13.0.0',

    # freeze: 2024-12-21
    binutils = '2.45',
    expat = '2.7.2',
    gdb = '16.3',
    gmp = '6.3.0',
    iconv = '1.18',
    make = '4.4.1',
    mpc = '1.3.1',
    mpfr = '4.2.2',
    pdcurses = '3.9',
    pkgconf = '2.5.1',
    python = '3.13.7',
    z = '1.3.1',
  ),
  '13': BranchVersions(
    gcc = '13.4.0',
    rev = '4',

    # trace back: 2023-12-22
    binutils = '2.41',
    expat = '2.5.0',
    gdb = '14.2',
    gmp = '6.3.0',
    iconv = '1.17',
    make = '4.4.1',
    # postponed until 1.8-ga.3 (2024-08-01)
    # - bootstrapping from scratch made easy
    # - gcc runtime library exception added
    mcfgthread = '1.8-ga.4',
    mingw = '11.0.1',
    mpc = '1.3.1',
    mpfr = '4.2.2',
    pdcurses = '3.9',
    pkgconf = '2.1.1',
    python = '3.12.11',
    z = '1.3.1',
  ),
}

_MINGW_ARCH_2_TRIPLET_MAP: dict[str, str] = {
  '64': 'x86_64-w64-mingw32',
  'arm64': 'aarch64-w64-mingw32',
  '32': 'i686-w64-mingw32',
}

_ARCH_VARIANT_2_MARCH_MAP: dict[str, str] = {
  '64_v2': 'x86-64-v2',
  '64': 'x86-64',
  'arm64': 'armv8-a',
  '32': 'pentium4',
  '32_686': 'i686',
  '32_486': 'i486',
}

_ARCH_VARIANT_2_FPMATH_MAP: dict[str, Optional[str]] = {
  '64_v2': None,
  '64': None,
  'arm64': None,
  '32': 'sse',
  '32_686': None,
  '32_486': None,
}

_ARCH_VARIANT_2_OPTIMIZE_FOR_SIZE_MAP: dict[str, bool] = {
  '64_v2': False,
  '64': True,
  'arm64': False,
  '32': True,
  '32_686': True,
  '32_486': True,
}

def _create_profile(arch: str, crt: str, thread: str, min_os: str) -> ProfileInfo:
  mingw_arch = arch.split('_')[0]
  exception = 'dwarf' if mingw_arch == '32' else 'seh'
  triplet = _MINGW_ARCH_2_TRIPLET_MAP[mingw_arch]
  march = _ARCH_VARIANT_2_MARCH_MAP[arch]
  fpmath = _ARCH_VARIANT_2_FPMATH_MAP[arch]
  optimize_for_size = _ARCH_VARIANT_2_OPTIMIZE_FOR_SIZE_MAP[arch]

  return ProfileInfo(
    arch = mingw_arch,
    fpmath = fpmath,
    march = march,
    target = triplet,
    optimize_for_size = optimize_for_size,

    default_crt = crt,
    exception = exception,
    thread = thread,

    win32_winnt = 0x0A00,
    min_os = Version(min_os),
  )

PROFILES: Dict[str, ProfileInfo] = {
  '64-mcf':    _create_profile('64', 'ucrt',   'mcf',   '6.1'),
  '64-win32':  _create_profile('64', 'ucrt',   'win32', '6.0'),
  '64-ucrt':   _create_profile('64', 'ucrt',   'posix', '6.0'),
  '64-msvcrt': _create_profile('64', 'msvcrt', 'posix', '6.0'),

  'arm64-mcf':   _create_profile('arm64', 'ucrt', 'mcf',   '10.0.16299'),
  'arm64-win32': _create_profile('arm64', 'ucrt', 'win32', '10.0.16299'),
  'arm64-ucrt':  _create_profile('arm64', 'ucrt', 'posix', '10.0.16299'),

  '32-mcf':    _create_profile('32', 'ucrt',   'mcf',   '6.1'),
  '32-win32':  _create_profile('32', 'ucrt',   'win32', '6.0'),
  '32-ucrt':   _create_profile('32', 'ucrt',   'posix', '6.0'),
  '32-msvcrt': _create_profile('32', 'msvcrt', 'posix', '6.0'),

  ############################################
  # profile variants for micro architectures #
  ############################################

  '64_v2-mcf':    _create_profile('64_v2', 'ucrt',   'mcf',   '6.1'),
  '64_v2-win32':  _create_profile('64_v2', 'ucrt',   'win32', '6.0'),
  '64_v2-ucrt':   _create_profile('64_v2', 'ucrt',   'posix', '6.0'),
  '64_v2-msvcrt': _create_profile('64_v2', 'msvcrt', 'posix', '6.0'),

  #################################################
  # profile variants for earlier Windows versions #
  #################################################

  '64-ucrt_ws2003':   _create_profile('64', 'ucrt',   'posix', '5.2'),
  '64-msvcrt_ws2003': _create_profile('64', 'msvcrt', 'posix', '5.2'),

  '32-ucrt_winxp':     _create_profile('32', 'ucrt',   'posix', '5.1'),
  '32-msvcrt_win2000': _create_profile('32', 'msvcrt', 'posix', '5.0'),

  '32_686-msvcrt_winnt40': _create_profile('32_686', 'msvcrt', 'posix', '4.0'),

  '32_486-msvcrt_winnt40': _create_profile('32_486', 'msvcrt', 'posix', '4.0'),
}

def resolve_profile(config: argparse.Namespace) -> BranchProfile:
  return BranchProfile(
    ver = BRANCHES[config.branch],
    info = PROFILES[config.profile],
  )
