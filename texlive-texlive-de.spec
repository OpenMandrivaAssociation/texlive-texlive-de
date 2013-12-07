# revision 31848
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-de
Version:	20131009
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
%doc %{_texmfdistdir}/doc/texlive/texlive-de/Makefile
%doc %{_texmfdistdir}/doc/texlive/texlive-de/install-lnx-main.png
%doc %{_texmfdistdir}/doc/texlive/texlive-de/lmsy10-40.png
%doc %{_texmfdistdir}/doc/texlive/texlive-de/psview.png
%doc %{_texmfdistdir}/doc/texlive/texlive-de/stdcoll.png
%doc %{_texmfdistdir}/doc/texlive/texlive-de/texlive-de-html.css
%doc %{_texmfdistdir}/doc/texlive/texlive-de/texlive-de-html.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-de/texlive-de.css
%doc %{_texmfdistdir}/doc/texlive/texlive-de/texlive-de.html
%doc %{_texmfdistdir}/doc/texlive/texlive-de/texlive-de.pdf
%doc %{_texmfdistdir}/doc/texlive/texlive-de/texlive-de.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-de/tlmgr-general-options.png
%doc %{_texmfdistdir}/doc/texlive/texlive-de/tlmgr-gui.png
%doc %{_texmfdistdir}/doc/texlive/texlive-de/tlmgr-paper-options.png
%doc %{_texmfdistdir}/doc/texlive/texlive-de/tray-menu.png
%doc %{_texmfdistdir}/doc/texlive/texlive-de/wizard-w32.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
