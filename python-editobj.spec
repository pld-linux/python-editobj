Summary:	EditObj can create a dialog box to edit ANY Python object
Summary(pl):	EditObj - tworzenie okien dialogowych do edycji dowolnego obiektu Pythona
Name:		python-editobj
Version:	0.5.3
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://oomadness.nekeme.net/downloads/EditObj-%{version}.tar.gz
# Source0-md5:	b933eac5959e2e269a806bd7c2ff0bee
URL:		http://oomadness.nekeme.net/en/editobj/
BuildRequires:	python-devel >= 1:2.3.4-2
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

%description -l pl
EditObj potrafi stworzy� i wy�wietli� okno dialogowe Tkinter do edycji
dowolnego obiektu Pythona (podobnie do tego, co w Javie nazywa si�
edytorem Bean, ale dla obiekt�w Pythona). EditObj to narz�dzie
przydatne do pisania (tekstowych i nietekstowych) edytor�w wszelkiego
rodzaju, w��cznie z edytorami GUI, edytorami 3D...

W terminologii MVC (Model View Controller - model-widok-kontroler),
EditObj to og�lny widok po��czony z uniwersalnym kontrolerem.

%prep
%setup -qn EditObj-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/editobj
%{py_sitescriptdir}/editobj/*.py[co]
%{py_sitescriptdir}/editobj/icons
