# revision 26888
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-de
Version:	20120808
Release:	2
Summary:	TeX Live manual (German)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-de package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/texlive/texlive-de/Makefile
%doc %{_texmfdir}/doc/texlive/texlive-de/lmsy10-40.png
%doc %{_texmfdir}/doc/texlive/texlive-de/texlive-de.css
%doc %{_texmfdir}/doc/texlive/texlive-de/texlive-de.html
%doc %{_texmfdir}/doc/texlive/texlive-de/texlive-de.pdf
%doc %{_texmfdir}/doc/texlive/texlive-de/texlive-de.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
