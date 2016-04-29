[![Build Status](https://travis-ci.org/ViaviSolutions/conan-cpprestsdk.svg?branch=master)](https://travis-ci.org/ViaviSolutions/conan-cpprestsdk)

# conan-cpprestsdk

[Conan.io](https://conan.io) package for Microsoft's [C++ REST SDK](https://github.com/Microsoft/cpprestsdk)

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/CppRestSdk/2.8.0/ViaviSolutions/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload CppRestSdk/2.8.0@ViaviSolutions/stable --all

## Reuse the packages

### Basic setup

    $ conan install CppRestSdk/2.8.0@ViaviSolutions/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    CppRestSdk/2.8.0@ViaviSolutions/stable

    [options]
    CppRestSdk:shared=true # false

    [generators]
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
