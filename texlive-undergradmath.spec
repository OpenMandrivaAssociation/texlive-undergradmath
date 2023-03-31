Name:		texlive-undergradmath
Version:	57286
Release:	2
Summary:	LaTeX Math for Undergraduates cheat sheet
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/undergradmath
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/undergradmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/undergradmath.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a cheat sheet for writing mathematics with LaTeX. It is
aimed at US undergraduates.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/undergradmath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
