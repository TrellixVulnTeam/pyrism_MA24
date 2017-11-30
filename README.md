# pyrism
I am aiming for pyrism to be a fast, feature-packed but lightweight real-time non-euclidean raytracing engine written in python.

## developer's note

### Pycharm:
If you are using pycharm you have to install a plugin called "EnvFile".

EnvFile lets you set global environment variables for your projects in .env files.

#### The variables this project needs are:

- **PYSDL2_DLL_PATH**: *path to an SDL2 devel dll.*
- **VS140COMNTOOLS**: *path to Visual C++ 2015 compiler tools. 
This may already been set by the installer.*

#### Extra info
If you decide to use a python interpreter version `earlier than 3.5` and get errors, 
you probably have the wrong Visual C++ tools version installed.

If you get the following error, the path variable probably **isn't set**. 

    SystemExit: error: Unable to find vcvarsall.bat

A blog post explaining how to fix the error can be found
[here](https://blogs.msdn.microsoft.com/pythonengineering/2016/04/11/unable-to-find-vcvarsall-bat/).


The default compiler for pyrism is msvc.
If you wish to change that go to `venv/Lib/distutils/distutils.cfg` and under `[Build]` add the line:

    compiler=mingw32

If you change the compiler you might also need to add it's path to the .env file or your system PATH variable.