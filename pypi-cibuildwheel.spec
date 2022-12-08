#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cibuildwheel
Version  : 2.11.3
Release  : 24
URL      : https://files.pythonhosted.org/packages/c0/0d/dce08024cb2fbdd277af5a4b7bb029e957f417a507b517f6386e3d28a127/cibuildwheel-2.11.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/0d/dce08024cb2fbdd277af5a4b7bb029e957f417a507b517f6386e3d28a127/cibuildwheel-2.11.3.tar.gz
Summary  : Build Python wheels on CI with minimal configuration.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-cibuildwheel-bin = %{version}-%{release}
Requires: pypi-cibuildwheel-python = %{version}-%{release}
Requires: pypi-cibuildwheel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(bashlex)
BuildRequires : pypi(bracex)
BuildRequires : pypi(certifi)
BuildRequires : pypi(filelock)
BuildRequires : pypi(packaging)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(setuptools)

%description
cibuildwheel
============
[![PyPI](https://img.shields.io/pypi/v/cibuildwheel.svg)](https://pypi.python.org/pypi/cibuildwheel)
[![Documentation Status](https://readthedocs.org/projects/cibuildwheel/badge/?version=stable)](https://cibuildwheel.readthedocs.io/en/stable/?badge=stable)
[![Actions Status](https://github.com/pypa/cibuildwheel/workflows/Test/badge.svg)](https://github.com/pypa/cibuildwheel/actions)
[![Travis Status](https://img.shields.io/travis/com/pypa/cibuildwheel/main?logo=travis)](https://travis-ci.com/pypa/cibuildwheel)
[![Appveyor status](https://ci.appveyor.com/api/projects/status/gt3vwl88yt0y3hur/branch/main?svg=true)](https://ci.appveyor.com/project/joerick/cibuildwheel/branch/main)
[![CircleCI Status](https://img.shields.io/circleci/build/gh/pypa/cibuildwheel/main?logo=circleci)](https://circleci.com/gh/pypa/cibuildwheel)
[![Azure Status](https://dev.azure.com/joerick0429/cibuildwheel/_apis/build/status/pypa.cibuildwheel?branchName=main)](https://dev.azure.com/joerick0429/cibuildwheel/_build/latest?definitionId=4&branchName=main)
[![Cirrus CI Status](https://img.shields.io/cirrus/github/pypa/cibuildwheel/main?logo=cirrusci)](https://cirrus-ci.com/github/pypa/cibuildwheel)

%package bin
Summary: bin components for the pypi-cibuildwheel package.
Group: Binaries

%description bin
bin components for the pypi-cibuildwheel package.


%package python
Summary: python components for the pypi-cibuildwheel package.
Group: Default
Requires: pypi-cibuildwheel-python3 = %{version}-%{release}

%description python
python components for the pypi-cibuildwheel package.


%package python3
Summary: python3 components for the pypi-cibuildwheel package.
Group: Default
Requires: python3-core
Provides: pypi(cibuildwheel)
Requires: pypi(bashlex)
Requires: pypi(bracex)
Requires: pypi(certifi)
Requires: pypi(filelock)
Requires: pypi(packaging)
Requires: pypi(platformdirs)

%description python3
python3 components for the pypi-cibuildwheel package.


%prep
%setup -q -n cibuildwheel-2.11.3
cd %{_builddir}/cibuildwheel-2.11.3
pushd ..
cp -a cibuildwheel-2.11.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670496138
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cibuildwheel

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
