from setuptools import setup, find_packages

setup(
    name="eqlink",
    version="2.0.1",
    keywords=("eqlink", "Registration Center", "eqsmart"),
    description="注册中心组件",
    long_description="更新2.0版本，使用json作为配置文件。",
    license="MIT license",

    url="https://github.com/enqiangjing/eqlink",
    author="enqiang",
    author_email="enqiangjing@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    # install_requires=['PyYAML==6.0']
)

"""
项目打包
python setup.py bdist_egg     # 生成类似 eqlink-0.0.1-py2.7.egg，支持 easy_install 
# 使用此方式
python setup.py sdist         # 生成类似 eqlink-0.0.1.tar.gz，支持 pip
# twine 需要安装
twine upload dist/eqlink-0.0.16.tar.gz
"""
