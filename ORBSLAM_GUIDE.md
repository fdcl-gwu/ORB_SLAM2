## Instructions to use ORBSLAM

1. First you need to run a blender simulation and save the hdf5 file someplace

2. Run the function `blender.write_h5py_to_png` to convert the images to a sequence of PNG files 

3. Copy these files to the ORBSLAM directory - I tend to use `./Examples/Monocular/directory_of_images`

4. A version of the monocular code is copied to `./Examples/Monocular/shankar.cc` 
    * To build this run `./build.sh`

5. Ensure camera properties are set correctly in `./Examples/Monocular/shankar.yml`

6. Save listing of filenames to a text file. This file should list in order the numerical names associated with the image files copied above. You can create such a list by running

    ~~~
    ls -v ./path/to/images | sed -e 's/\.png$//' > name_of_text_file.txt
    ~~~

    This assumes the files are named as `0.png, 1.png, etc.`

7. Run ORBSLAM using

    ~~~
    ./Examples/Monocular/mono_shankar Vocabular/ORBvoc.txt Examples/Monocular/shankar.yml ./Examples/Monocular/asteroid_fixed_circumnavigate Examples/Monocular/asteroid_fixed_circumnavigate.txt
    ~~~

8. Hopefully it works and the keyframe trajectory is saved to `KeyFrameTrajectory.txt`

9. Copy this file back to `asteroid_dumbbell` to run the comparisons using ...
