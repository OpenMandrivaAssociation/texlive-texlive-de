# revision 23053
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-de
Version:	20111103
Release:	1
Summary:	TeX Live manual (German)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
