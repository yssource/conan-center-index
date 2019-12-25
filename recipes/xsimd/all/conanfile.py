import os
from conans import ConanFile, CMake, tools


class XsimdConan(ConanFile):
    name = "xsimd"
    license = "BSD 3-Clause"
    url = "https://github.com/conan-io/conan-center-index"
    repo_url = "https://github.com/xtensor-stack/xsimd"
    description = "C++ wrappers for SIMD intrinsics and parallelized, optimized mathematical functions (SSE, AVX, NEON, AVX512)"
    topics = ("conan", "simd-intrinsics", "vectorization", "simd")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_folder = self.name + "-" + self.version
        os.rename(extracted_folder, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        self.info.header_only()