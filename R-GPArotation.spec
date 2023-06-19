#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-GPArotation
Version  : 2023.3.1
Release  : 49
URL      : https://cran.r-project.org/src/contrib/GPArotation_2023.3-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/GPArotation_2023.3-1.tar.gz
Summary  : Gradient Projection Factor Rotation
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n GPArotation
cd %{_builddir}/GPArotation

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679414545

%install
export SOURCE_DATE_EPOCH=1679414545
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/GPArotation/CITATION
/usr/lib64/R/library/GPArotation/DESCRIPTION
/usr/lib64/R/library/GPArotation/INDEX
/usr/lib64/R/library/GPArotation/Meta/Rd.rds
/usr/lib64/R/library/GPArotation/Meta/data.rds
/usr/lib64/R/library/GPArotation/Meta/features.rds
/usr/lib64/R/library/GPArotation/Meta/hsearch.rds
/usr/lib64/R/library/GPArotation/Meta/links.rds
/usr/lib64/R/library/GPArotation/Meta/nsInfo.rds
/usr/lib64/R/library/GPArotation/Meta/package.rds
/usr/lib64/R/library/GPArotation/Meta/vignette.rds
/usr/lib64/R/library/GPArotation/NAMESPACE
/usr/lib64/R/library/GPArotation/NEWS
/usr/lib64/R/library/GPArotation/R/GPArotation
/usr/lib64/R/library/GPArotation/R/GPArotation.rdb
/usr/lib64/R/library/GPArotation/R/GPArotation.rdx
/usr/lib64/R/library/GPArotation/data/Rdata.rdb
/usr/lib64/R/library/GPArotation/data/Rdata.rds
/usr/lib64/R/library/GPArotation/data/Rdata.rdx
/usr/lib64/R/library/GPArotation/doc/GPAguide.R
/usr/lib64/R/library/GPArotation/doc/GPAguide.Stex
/usr/lib64/R/library/GPArotation/doc/GPAguide.pdf
/usr/lib64/R/library/GPArotation/doc/GPArotateDF.R
/usr/lib64/R/library/GPArotation/doc/GPArotateDF.Stex
/usr/lib64/R/library/GPArotation/doc/GPArotateDF.pdf
/usr/lib64/R/library/GPArotation/doc/index.html
/usr/lib64/R/library/GPArotation/help/AnIndex
/usr/lib64/R/library/GPArotation/help/GPArotation.rdb
/usr/lib64/R/library/GPArotation/help/GPArotation.rdx
/usr/lib64/R/library/GPArotation/help/aliases.rds
/usr/lib64/R/library/GPArotation/help/paths.rds
/usr/lib64/R/library/GPArotation/html/00Index.html
/usr/lib64/R/library/GPArotation/html/R.css
/usr/lib64/R/library/GPArotation/tests/Harman.R
/usr/lib64/R/library/GPArotation/tests/Jennrich2002.R
/usr/lib64/R/library/GPArotation/tests/MASSoblimin.R
/usr/lib64/R/library/GPArotation/tests/Revelle.R
/usr/lib64/R/library/GPArotation/tests/Thurstone.R
/usr/lib64/R/library/GPArotation/tests/WansbeekMeijer.R
/usr/lib64/R/library/GPArotation/tests/print-GPArotation.R
/usr/lib64/R/library/GPArotation/tests/rotations.R
/usr/lib64/R/library/GPArotation/tests/varimaxVarimax.R
