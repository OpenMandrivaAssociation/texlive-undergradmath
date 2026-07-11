%global tl_name undergradmath
%global tl_revision 57286

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX Math for Undergraduates cheat sheet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/undergradmath
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/undergradmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/undergradmath.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a cheat sheet for writing mathematics with LaTeX. It is aimed at
US undergraduates.

