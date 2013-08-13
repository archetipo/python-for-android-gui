Python for Android-Gui
======================

Python for android Gui is a graphics interface in Kivy for python-for-android 
for create your own Python distribution including the modules you want, 
and create an apk including python, libs, and your application whit a graphical toolkit.
Written in kivy :
 automatic search and found your first device connected
 Tabbed Pannel for simplify work sequence 
 Logcat integrate (very experimental)


- Italian Website: http://www.thinkstudio.it
- Documentation:



Global overview
---------------

#. Download Android NDK, SDK
 
 * NDK: http://dl.google.com/android/ndk/android-ndk-r8e-linux-x86.tar.bz2
 
 * More details at: http://developer.android.com/tools/sdk/ndk/index.html
 
 * SDK: http://dl.google.com/android/android-sdk_r21.0.1-linux.tgz
 
 * More details at:http://developer.android.com/sdk/index.html
 
 * Py4A: https://github.com/kivy/python-for-android
 
 * More details at: http://python-for-android.rtfd.org/
 
 * Kivy: https://github.com/kivy/kivy
 
 * More details: http://kivy.org/
  
#. Launch "android", and download latest Android platform, here API 14, which would be Android 4.0

#. Clone Kivy::

    git clone https://github.com/kivy/kivy.git
    

#. Clone python-for-android::

    git clone git://github.com/kivy/python-for-android


#. Clone Python for Android Gui::

    git clone https://github.com/archetipo/python-for-android-gui    

#. In Py4A folder create a files nemad settings.txt and add this sequence::

            /your/path/android/sdk
            /your/path/android/android-ndk-ndkver
            ndkver
            ANDROIDAPI
            /your/path/python-for-android

 (the data must be added in this sequence)
 (ANDROIDAPI is a number e.g. 14 ndkver is a version ndk e.g. r8e )



#. start Applicatyion::

    cd python-for-android-gui
    sudo chmod +x main.py
    ./main.py

#. In Distribute Tab::

    Select: modules to add a project, this modules is a list of recipes that
            you have in recipes folder for python-for-android
    
    Click Distribuite 
    

#. In Build & install Tab::
    Left Side:
    
        insert a proj data:
        e.g.
        version:1.0
        name : prj_name
        base package: org.test
        
        Treview Folder
            The directory containing public files for the project.
            
        select deploy type: debug or releas
    Rigth Side:
        select list of permission for your app
        
    Click Build and later Install
    
    
#. Have Fun!


Troubleshooting
---------------


