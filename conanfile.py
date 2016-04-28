from conans import ConanFile, CMake
from conans.tools import download, unzip
import os
import shutil

class CppRestSdkConan(ConanFile):
    name = 'CppRestSdk'
    version = '2.8.0'
    license = 'Apache License 2.0'
    settings = 'os', 'compiler', 'build_type', 'arch'
    exports = 'CMakeLists.txt'
    generators = "cmake"
    requires = ('Boost/1.59.0@lasote/stable',
                'OpenSSL/1.0.2g@viavisolutions/testing')

    def config(self):
        self.options["OpenSSL"].shared = True

    def source(self):
        zip_name = 'cpprestsdk-{}.zip'.format(self.version)
        url = 'https://github.com/Microsoft/cpprestsdk/archive/v{}.zip'.format(self.version)
        download(url, zip_name)
        unzip(zip_name)
        shutil.move('cpprestsdk-{}'.format(self.version), 'cpprestsdk')
        os.unlink(zip_name)
        shutil.move(
            'cpprestsdk/Release/CMakeLists.txt',
            'cpprestsdk/Release/CMakeListsOriginal.cmake')
        shutil.move('CMakeLists.txt', 'cpprestsdk/Release/CMakeLists.txt')

    def build(self):
        cmake = CMake(self.settings)
        self.run('cd cpprestsdk/Release && cmake . %s' % cmake.command_line)
        self.run('printenv')
        self.run('cd cpprestsdk/Release && cmake --build . %s' % cmake.build_config)

    def package(self):
        self.copy("*", dst="include/cpprest", src="cpprestsdk/Release/include/cpprest", keep_path=False)
        self.copy("*", dst="include/cpprest/details", src="cpprestsdk/Release/include/cpprest/details", keep_path=False)
        self.copy("*", dst="include/pplx", src="cpprestsdk/Release/include/pplx", keep_path=False)
        libraries = [
            'libcommon_utilities.so',
            'libcpprest.so',
            'libcpprest.so.2.8',
            'libhttptest_utilities.so',
            'libunittestpp.so',
            'libwebsockettest_utilities.so'
            ]
        for lib in libraries:
            self.copy(lib, dst="lib", src="cpprestsdk/Release/Binaries/")

    def package_info(self):
        self.cpp_info.cppflags = ["-std=c++11"]
        self.cpp_info.libs = ["libcpprest.so"]
