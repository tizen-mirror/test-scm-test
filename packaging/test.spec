Summary:    Test package
Name:       test
Version:    0.1
Release:    1
Source0:     test-0.1.tar.gz
Source1001: packaging/test.manifest 
License:    MIT
Packager:   tester
Group:      Application
 
%description
 Just a test package. Test line
 Test line2
 
%build
cp %{SOURCE1001} .
 
%install
 
%files
