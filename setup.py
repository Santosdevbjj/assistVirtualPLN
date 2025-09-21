from setuptools import setup, find_packages

# Lendo o conteúdo do arquivo README.md para a descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Lendo as dependências do arquivo requirements.txt
def get_requirements(file_path):
    with open(file_path, 'r') as f:
        requirements = f.read().splitlines()
    return requirements

setup(
    name='assistvirtual-pln',
    version='0.1.0',
    author='Seu Nome de Usuário',
    author_email='seu.email@exemplo.com',
    description='Um sistema de assistência virtual utilizando Processamento de Linguagem Natural (PLN).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Santosdevbjj/assistVirtualPLN',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires='>=3.6',
    keywords='machine-learning, nlp, natural-language-processing, virtual-assistant, speech-to-text, text-to-speech',
)

