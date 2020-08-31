import setuptools

setuptools.setup(
    name="demo_reader",
    version="1.0.0",
    description="Tools for reading various file formats",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'demo_reader.compression_plugins': [
            'bz2 = demo_reader_bz2.bzipped',
            'gz = demo_reader_gz.gzipped'
        ]
    }
)