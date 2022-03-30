#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	EditObj can create a dialog box to edit ANY Python object
Summary(pl.UTF-8):	EditObj - tworzenie okien dialogowych do edycji dowolnego obiektu Pythona
Name:		python-editobj
Version:	0.5.3
Release:	12
License:	GPL
Group:		Libraries/Python
Source0:	http://oomadness.nekeme.net/downloads/EditObj-%{version}.tar.gz
# Source0-md5:	b933eac5959e2e269a806bd7c2ff0bee
Patch0:		prefix.patch
URL:		http://oomadness.nekeme.net/en/editobj/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel >= 1:2.3.4-2
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EditObj can create and display a Tkinter dialog box for editing any
Python object (similarly to what Java call a Bean editor, but for
Python object). EditObj is a useful tool for writing (text or
non-text) editors of all kinds, including GUI editor, 3D editor,...

In terms of MVC (Model View Controler), EditObj is a generic View
coupled with a universal Controler.

%description -l pl.UTF-8
EditObj potrafi stworzyć i wyświetlić okno dialogowe Tkinter do edycji
dowolnego obiektu Pythona (podobnie do tego, co w Javie nazywa się
edytorem Bean, ale dla obiektów Pythona). EditObj to narzędzie
przydatne do pisania (tekstowych i nietekstowych) edytorów wszelkiego
rodzaju, włącznie z edytorami GUI, edytorami 3D...

W terminologii MVC (Model View Controller - model-widok-kontroler),
EditObj to ogólny widok połączony z uniwersalnym kontrolerem.

%package -n python3-editobj
Summary:	EditObj can create a dialog box to edit ANY Python object
Summary(pl.UTF-8):	EditObj - tworzenie okien dialogowych do edycji dowolnego obiektu Pythona
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-editobj
EditObj can create and display a Tkinter dialog box for editing any
Python object (similarly to what Java call a Bean editor, but for
Python object). EditObj is a useful tool for writing (text or
non-text) editors of all kinds, including GUI editor, 3D editor,...

In terms of MVC (Model View Controler), EditObj is a generic View
coupled with a universal Controler.

%description -n python3-editobj -l pl.UTF-8
EditObj potrafi stworzyć i wyświetlić okno dialogowe Tkinter do edycji
dowolnego obiektu Pythona (podobnie do tego, co w Javie nazywa się
edytorem Bean, ale dla obiektów Pythona). EditObj to narzędzie
przydatne do pisania (tekstowych i nietekstowych) edytorów wszelkiego
rodzaju, włącznie z edytorami GUI, edytorami 3D...

W terminologii MVC (Model View Controller - model-widok-kontroler),
EditObj to ogólny widok połączony z uniwersalnym kontrolerem.

%prep
%setup -qn EditObj-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/editobj
%{py_sitescriptdir}/EditObj-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-editobj
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/editobj
%{py3_sitescriptdir}/EditObj-%{version}-py*.egg-info
%endif
