#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab_widgets
Version  : 1.0.2
Release  : 10
URL      : https://files.pythonhosted.org/packages/27/f1/0d3a09c0069467ed9636faf3a9b5b758378216bb891066a0bc24799681e3/jupyterlab_widgets-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/27/f1/0d3a09c0069467ed9636faf3a9b5b758378216bb891066a0bc24799681e3/jupyterlab_widgets-1.0.2.tar.gz
Summary  : A JupyterLab extension.
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: jupyterlab_widgets-data = %{version}-%{release}
Requires: jupyterlab_widgets-license = %{version}-%{release}
Requires: jupyterlab_widgets-python = %{version}-%{release}
Requires: jupyterlab_widgets-python3 = %{version}-%{release}
Requires: jupyter-packaging
BuildRequires : buildreq-distutils3
BuildRequires : jupyter-packaging

%description
Jupyter Widgets JupyterLab Extension
====================================
A JupyterLab 3.0 extension for Jupyter/IPython widgets.

%package data
Summary: data components for the jupyterlab_widgets package.
Group: Data

%description data
data components for the jupyterlab_widgets package.


%package license
Summary: license components for the jupyterlab_widgets package.
Group: Default

%description license
license components for the jupyterlab_widgets package.


%package python
Summary: python components for the jupyterlab_widgets package.
Group: Default
Requires: jupyterlab_widgets-python3 = %{version}-%{release}

%description python
python components for the jupyterlab_widgets package.


%package python3
Summary: python3 components for the jupyterlab_widgets package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlab_widgets)

%description python3
python3 components for the jupyterlab_widgets package.


%prep
%setup -q -n jupyterlab_widgets-1.0.2
cd %{_builddir}/jupyterlab_widgets-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631721595
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyterlab_widgets
cp %{_builddir}/jupyterlab_widgets-1.0.2/LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab_widgets/1a410cd75c35603554d91880a9aba11f9c322b59
cp %{_builddir}/jupyterlab_widgets-1.0.2/jupyterlab_widgets/labextension/static/638.f3e5e34a28f3334d4f08.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab_widgets/91c0a8c54b0074f38b65a7ed44f743dbe3613f0f
cp %{_builddir}/jupyterlab_widgets-1.0.2/jupyterlab_widgets/labextension/static/95.b5a5ff10000a6051fa99.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/jupyterlab_widgets/23f8330f4dbbb325e59355b4b4a97c0749b2efd7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/install.json
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/package.json
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/schemas/@jupyter-widgets/jupyterlab-manager/package.json.orig
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/schemas/@jupyter-widgets/jupyterlab-manager/plugin.json
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/1.6c3ab69171002cbfa04f.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/18.5fbcd9c56ded92ea9df9.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/243.6c384ff2649ef572a18a.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/272.9d70a85a9abe209402d0.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/279.aa88a78c8bf62c65db54.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/466.ad8615bb2a7c38ad415a.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/523.cf94b68f6edde7eefd61.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/638.f3e5e34a28f3334d4f08.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/638.f3e5e34a28f3334d4f08.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/803.b7b75bd6e7977a648c67.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/868.c125b968409ba9295199.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/95.b5a5ff10000a6051fa99.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/95.b5a5ff10000a6051fa99.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/remoteEntry.f6574b55a223d23e7a04.js
/usr/share/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/static/style.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyterlab_widgets/1a410cd75c35603554d91880a9aba11f9c322b59
/usr/share/package-licenses/jupyterlab_widgets/23f8330f4dbbb325e59355b4b4a97c0749b2efd7
/usr/share/package-licenses/jupyterlab_widgets/91c0a8c54b0074f38b65a7ed44f743dbe3613f0f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
