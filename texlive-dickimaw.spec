%global tl_name dickimaw
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Books and tutorials from the Dickimaw LaTeX Series
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/dickimaw
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dickimaw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dickimaw.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides some of the books and tutorials that form part of
the "Dickimaw LaTeX Series". Only the A4 PDF of each book is detailed
here. Other formats, such as HTML or screen optimized PDF, are available
from the package home page. Books included are: "LaTeX for Complete
Novices": an introductory guide to LaTeX. "Using LaTeX to Write a PhD
Thesis": a follow-on from "LaTeX for Complete Novices" geared towards
students who want to use LaTeX to write their PhD thesis. "Creating a
LaTeX minimal example": describes how to create a minimal example, which
can be used as a debugging aid when you encounter errors in your LaTeX
documents.

