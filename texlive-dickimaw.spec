Name:		texlive-dickimaw
Version:	32925
Release:	2
Summary:	Books and tutorials from the "Dickimaw LaTeX Series"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/dickimaw
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dickimaw.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dickimaw.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The package provides are some of the books and tutorials that
form part of the "Dickimaw LaTeX Series". Only the A4 PDF is
included here. Other formats, such as HTML or a screen
optimized PDF, are available from the package home page. Books
included are: "LaTeX for Complete Novices": an introductory
guide to LaTeX. "Using LaTeX to Write a PhD Thesis": a follow-
on from "LaTeX for Complete Novices" geared towards students
who want to use LaTeX to write their PhD thesis. "Creating a
LaTeX minimal example": describes how to create a minimal
example, which can be used as a debugging aid when you
encounter errors in your LaTeX documents.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/dickimaw/ERRATA
%doc %{_texmfdistdir}/doc/latex/dickimaw/README
%doc %{_texmfdistdir}/doc/latex/dickimaw/dickimaw-minexample.pdf
%doc %{_texmfdistdir}/doc/latex/dickimaw/dickimaw-novices.pdf
%doc %{_texmfdistdir}/doc/latex/dickimaw/dickimaw-thesis.pdf
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/fdl.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/minexample/dickimaw-minexample.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/minexample/minexample.sty
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/dickimaw-novices.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/glsentries.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/keywords.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/novices-a4paper.sty
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/novices-index.ist
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/novices.bib
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/novices.cls
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/acrobat.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/backtic.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/circle.pdf
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom3.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom4.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom5.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom6.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom7.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dinglist.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dirviewer1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dirviewer2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dirviewer3.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dirviewer4.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/draftimage.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/entersymbol.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/errormessage.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/exsamp.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/incgraph.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/incgraph2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/letterbox.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/maths.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/miktex1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/newdoc-1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/newdoc-2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/notepad1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/notepad2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/rectangle.pdf
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/reflbox.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/resizbox.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/rotbox.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/scalbox.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/shapes.pdf
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/tds.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal-texdoc.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal10.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal11.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal3.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal4.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal5.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal6.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal7.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal8.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal9.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-latexmk.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-preferences.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-toolconfig1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-toolconfig2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-toolconfig3.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-toolconfig4.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks3.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks4.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks5-annote.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks5.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks6.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks7.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks8.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks9.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/yap1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/argument.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/auxiliary.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/cls.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/command.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/declaration.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/dvi.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/environment.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/fragile.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/group.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/hyphenation.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/intersentencespacing.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/introduction.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/length.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/mandatory.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/optional.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/output.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/perl.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/preamble.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/robust.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/short.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/source.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/terminal.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/tex.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/dickimaw-thesis.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/dickimawthesis.cls
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/glsentries.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/imgsource/titlepage.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/listing-samples/helloworld.c
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/listing-samples/sqrt.c
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/arara-installer.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/bibertool.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/doibutton.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/generatekey.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-dataprop-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-dataprop.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-pref-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-pref.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport1-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport2-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport3-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport3.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref1-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref1.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref10-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref10.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref11.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref12-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref12.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref3-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref3.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref4-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref4.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref5-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref5.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref6-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref6.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref7-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref7.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref8-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref8.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref9-thumbnail.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref9.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/pagestyle.tex
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-addbutton.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-arara.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-arara2.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-bibtex.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-latexmk.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-latexmkbibtex.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-makeglossaries.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-pdflatex.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-pref.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-texindy.png
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/titlepage.pdf
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/thesis-a4paper.sty
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/thesis-index.ist
%doc %{_texmfdistdir}/doc/latex/dickimaw/src/thesis/thesis.bib

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
