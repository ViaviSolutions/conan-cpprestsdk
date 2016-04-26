from conans import ConanFile, CMake
from conans.tools import download, unzip
import os
import shutil

class HelloConan(ConanFile):
    name = 'CppRestSdk'
    version = '2.8.0'
    settings = 'os', 'compiler', 'build_type', 'arch'
    exports = 'CMakeLists.txt'
    generators = "cmake"
    requires = ('Boost/1.60.0@lasote/stable',
                'OpenSSL/1.0.2g@lasote/stable')

    def source(self):
        zip_name = 'cpprestsdk-2.8.0.zip'
        download('https://github.com/Microsoft/cpprestsdk/archive/v2.8.0.zip', zip_name)
        unzip(zip_name)
        shutil.move('cpprestsdk-2.8.0', 'cpprestsdk')
        os.unlink(zip_name)
        shutil.move('cpprestsdk/Release/CMakeLists.txt', 'cpprestsdk/Release/CMakeListsOriginal.cmake')
        shutil.move('CMakeLists.txt', 'cpprestsdk/Release/CMakeLists.txt')

    def build(self):
        cmake = CMake(self.settings)
        self.run('cd cpprestsdk/Release && cmake . %s' % cmake.command_line)
        self.run('printenv')
        self.run('cd cpprestsdk/Release && cmake --build . %s' % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*.lib", dst="lib", src="hello/lib")
        self.copy("*.a", dst="lib", src="hello/lib")

    def package_info(self):
        self.cpp_info.libs = ["hello"]
