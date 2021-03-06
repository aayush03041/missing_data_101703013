from distutils.core import setup
setup(
  name = 'missing_data_101703013',         # How you named your package folder (MyLib)3
  packages = ['missing_data_101703013'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'fill the missing values',   # Give a short description about your library
  author = 'Aayush Singla',                   # Type in your name
  author_email = 'singlaaayush0@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/aayush03041/missing_data_101703013', 
download_url = 'https://github.com/aayush03041/missing_data_101703013/archive/v_01.tar.gz',  # Provide either the link to your github or to your website
  keywords = ['missing_data'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
