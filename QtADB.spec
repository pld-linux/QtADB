Summary:	Android Debug Bridge GUI
Name:		QtADB
Version:	0.8.1
Release:	1
License:	Apache v2.0
Group:		Applications/Communications
Source0:	http://qtadb.com/qtadb/%{name}_%{version}_src
# Source0-md5:	062481737ef27f7377bc52ad5a6db06f
URL:		http://qtadb.wordpress.com/
BuildRequires:	QtCore-devel
BuildRequires:	QtDeclarative-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Android Debug Bridge GUI.

%prep
%setup -q -n trunk

%build
qmake-qt4 %{name}.pro
%{__make} \
	CXXFLAGS='%{rpmcflags} $(DEFINES)'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc otherfiles/* tmp/*
%attr(755,root,root) %{_bindir}/%{name}
