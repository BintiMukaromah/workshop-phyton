(base) C:\Users\NABIJI>conda --version
conda 4.12.0

(base) C:\Users\NABIJI>conda update conda
Collecting package metadata (current_repodata.json): done
Solving environment: done

# All requested packages already installed.


(base) C:\Users\NABIJI>conda create --name snowflakes biopython
WARNING: A conda environment already exists at 'C:\Users\NABIJI\anaconda3\envs\snowflakes'
Remove existing environment (y/[n])? y

Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\NABIJI\anaconda3\envs\snowflakes

  added / updated specs:
    - biopython


The following NEW packages will be INSTALLED:

  biopython          pkgs/main/win-64::biopython-1.78-py39h2bbff1b_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_1
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
  numpy              pkgs/main/win-64::numpy-1.21.5-py39h7a0a035_1
  numpy-base         pkgs/main/win-64::numpy-base-1.21.5-py39hca35cd5_1
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snowflakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\NABIJI>conda activate snowflakes

(snowflakes) C:\Users\NABIJI>conda activate

(base) C:\Users\NABIJI>conda info --envs
# conda environments:
#
base                  *  C:\Users\NABIJI\anaconda3
snowflakes               C:\Users\NABIJI\anaconda3\envs\snowflakes
                         C:\Users\NABIJI\miniconda3
                         C:\Users\NABIJI\miniconda3\envs\my_first_env_python=3.10.2


(base) C:\Users\NABIJI>conda create --name snakes python=3.9
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\NABIJI\anaconda3\envs\snakes

  added / updated specs:
    - python=3.9


The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_1
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\NABIJI>conda activate snakes

(snakes) C:\Users\NABIJI>conda info --envs
# conda environments:
#
base                     C:\Users\NABIJI\anaconda3
snakes                *  C:\Users\NABIJI\anaconda3\envs\snakes
snowflakes               C:\Users\NABIJI\anaconda3\envs\snowflakes
                         C:\Users\NABIJI\miniconda3
                         C:\Users\NABIJI\miniconda3\envs\my_first_env_python=3.10.2


(snakes) C:\Users\NABIJI>$
'$' is not recognized as an internal or external command,
operable program or batch file.

(snakes) C:\Users\NABIJI>python --version
Python 3.9.12

(snakes) C:\Users\NABIJI>conda search beautifulsoup4
Loading channels: done
# Name                       Version           Build  Channel
beautifulsoup4                 4.6.0          py27_1  pkgs/main
beautifulsoup4                 4.6.0  py27hc287451_1  pkgs/main
beautifulsoup4                 4.6.0          py35_1  pkgs/main
beautifulsoup4                 4.6.0  py35h61fcdcc_1  pkgs/main
beautifulsoup4                 4.6.0          py36_1  pkgs/main
beautifulsoup4                 4.6.0  py36hd4cc5e8_1  pkgs/main
beautifulsoup4                 4.6.0          py37_1  pkgs/main
beautifulsoup4                 4.6.1          py27_0  pkgs/main
beautifulsoup4                 4.6.1          py35_0  pkgs/main
beautifulsoup4                 4.6.1          py36_0  pkgs/main
beautifulsoup4                 4.6.1          py37_0  pkgs/main
beautifulsoup4                 4.6.3          py27_0  pkgs/main
beautifulsoup4                 4.6.3          py35_0  pkgs/main
beautifulsoup4                 4.6.3          py36_0  pkgs/main
beautifulsoup4                 4.6.3          py37_0  pkgs/main
beautifulsoup4                 4.7.1          py27_1  pkgs/main
beautifulsoup4                 4.7.1          py36_1  pkgs/main
beautifulsoup4                 4.7.1          py37_1  pkgs/main
beautifulsoup4                 4.8.0          py27_0  pkgs/main
beautifulsoup4                 4.8.0          py36_0  pkgs/main
beautifulsoup4                 4.8.0          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py27_0  pkgs/main
beautifulsoup4                 4.8.1          py36_0  pkgs/main
beautifulsoup4                 4.8.1          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py38_0  pkgs/main
beautifulsoup4                 4.8.2          py27_0  pkgs/main
beautifulsoup4                 4.8.2          py36_0  pkgs/main
beautifulsoup4                 4.8.2          py37_0  pkgs/main
beautifulsoup4                 4.8.2          py38_0  pkgs/main
beautifulsoup4                 4.9.0          py36_0  pkgs/main
beautifulsoup4                 4.9.0          py37_0  pkgs/main
beautifulsoup4                 4.9.0          py38_0  pkgs/main
beautifulsoup4                 4.9.1          py36_0  pkgs/main
beautifulsoup4                 4.9.1  py36haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py37_0  pkgs/main
beautifulsoup4                 4.9.1  py37haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py38_0  pkgs/main
beautifulsoup4                 4.9.1  py38haa95532_0  pkgs/main
beautifulsoup4                 4.9.1  py39haa95532_0  pkgs/main
beautifulsoup4                 4.9.3    pyha847dfd_0  pkgs/main
beautifulsoup4                 4.9.3    pyhb0f4dca_0  pkgs/main
beautifulsoup4                4.10.0    pyh06a4308_0  pkgs/main
beautifulsoup4                4.11.1 py310haa95532_0  pkgs/main
beautifulsoup4                4.11.1  py37haa95532_0  pkgs/main
beautifulsoup4                4.11.1  py38haa95532_0  pkgs/main
beautifulsoup4                4.11.1  py39haa95532_0  pkgs/main

(snakes) C:\Users\NABIJI>conda install beautifulsoup4
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\NABIJI\anaconda3\envs\snakes

  added / updated specs:
    - beautifulsoup4


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    beautifulsoup4-4.11.1      |   py39haa95532_0         190 KB
    soupsieve-2.3.1            |     pyhd3eb1b0_0          34 KB
    ------------------------------------------------------------
                                           Total:         224 KB

The following NEW packages will be INSTALLED:

  beautifulsoup4     pkgs/main/win-64::beautifulsoup4-4.11.1-py39haa95532_0
  soupsieve          pkgs/main/noarch::soupsieve-2.3.1-pyhd3eb1b0_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
soupsieve-2.3.1      | 34 KB     | ################################### | 100%
beautifulsoup4-4.11. | 190 KB    | ################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(snakes) C:\Users\NABIJI>conda list
# packages in environment at C:\Users\NABIJI\anaconda3\envs\snakes:
#
# Name                    Version                   Build  Channel
beautifulsoup4            4.11.1           py39haa95532_0
ca-certificates           2022.3.29            haa95532_1
certifi                   2021.10.8        py39haa95532_2
openssl                   1.1.1n               h2bbff1b_0
pip                       21.2.4           py39haa95532_0
python                    3.9.12               h6244533_0
setuptools                61.2.0           py39haa95532_0
soupsieve                 2.3.1              pyhd3eb1b0_0
sqlite                    3.38.2               h2bbff1b_0
tzdata                    2022a                hda174b7_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
wheel                     0.37.1             pyhd3eb1b0_0
wincertstore              0.2              py39haa95532_2

(snakes) C:\Users\NABIJI>conda create --name myclone --clone myenv

EnvironmentNameNotFound: Could not find conda environment: myenv
You can list all discoverable environments with `conda info --envs`.


(snakes) C:\Users\NABIJI>