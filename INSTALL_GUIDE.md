1. Need to install Pangolin. Anaconda causes and error with some C libraries.
Make a new enviornment and update `libgcc`

~~~
conda uninstall libgcc
conda install libgcc
~~~

2. Need to install OpenCV to the system path, i.e. `/usr/local` instead of the Anaconda environment.
You can just change the `MAKE_INSTALL_PATH=/usr/local` from the script
