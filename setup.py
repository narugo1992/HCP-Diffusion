import os
import re

import setuptools

def _load_req(file: str):
    with open(file, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

requirements = _load_req('requirements.txt')

_REQ_PATTERN = re.compile(r'^requirements-(\w+)\.txt$')
group_requirements = {
    item.group(1):_load_req(item.group(0))
    for item in [_REQ_PATTERN.fullmatch(reqpath) for reqpath in os.listdir()] if item
}

def get_data_files(data_dir, prefix=''):
    file_dict = {}
    for root, dirs, files in os.walk(data_dir, topdown=False):
        for name in files:
            if prefix+root not in file_dict:
                file_dict[prefix+root] = []
            file_dict[prefix+root].append(os.path.join(root, name))
    return [(k, v) for k, v in file_dict.items()]

setuptools.setup(
    name="hcpdiff",
    py_modules=["hcpdiff"],
    version="0.9.1",
    author="Ziyi Dong",
    author_email="dzy7eu7d7@gmail.com",
    description="A universal Stable-Diffusion toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/7eu7d7/HCP-Diffusion",
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.7',

    entry_points={
        'console_scripts':[
            'hcpinit = hcpdiff.tools.init_proj:main'
        ]
    },

    data_files=[
        *get_data_files('prompt_tuning_template', prefix='hcpdiff/'),
        *get_data_files('cfgs', prefix='hcpdiff/'),
    ],

    install_requires=requirements,
    extras_require=group_requirements,
)
