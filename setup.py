import setuptools

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='gym_electric_motor',
      version='0.1.0',
      description='An OpenAI gym environment for electric motor control.',
      packages=setuptools.find_packages(),
      install_requires=requirements,
      extras_require={'examples': 
                      ['keras_rl2>=1.0.3']
                     },
      author='Praneeth Balakrishna, Gerrit Book, Wilhelm Kirchgässner, Maximilian Schenke, Arne Traue, Oliver Wallscheid',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/upb-lea/gym-electric-motor",
      )
