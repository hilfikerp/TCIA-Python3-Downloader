                                 README
                        The Cancer Imaging Archive
                          TCIA Interactive Menu
                                Version 3
Contents
--------

   * Introduction
   * TCIA Menu Setup
   * Useful Tips
   * Sample Property File
   * User Requirements
   * Sample Test Cases
   * Troubleshooting
   * Bug Reports and Feedback


Introduction
------------

   The TCIA interactive menu is designed to provide users of The Cancer Imaging
   Archive with the ability to easily interact with the TCIA Programmatic Interface 
   (REST API).  This version is designed to be compatible with version 3 of the API.
   Users of the TCIA menu will be able to call any existing method available in the 
   API, as well as keep existing TCIA Collections and Patients synchronized locally.

   The TCIA menu uses the same directory structure as the Java Web Start download
   options currently available on the TCIA wiki site found at:
   
   https://wiki.cancerimagingarchive.net/display/Public/Wiki
   
   To make best use of the TCIA menu, it's recommended to configure a %TCIA_HOME%
   system environment variable and create a TCIA properties file, as described below.


TCIA Menu Setup
-------------------------------------------------------

   1. Checkout all files available on the TCIA GitHub page.
   2. Follow instructions below in User Requirements section.
   3. To take advantage of certain features of the TCIA menu, configure a system
      environment variable called "TCIA_HOME" and point it at the directory
      that contains all of your local TCIA directories and files.
   4. To reduce the need to enter repetitive user input, create a properties
      file in your TCIA_HOME directory as described below in Useful Tips.
      
      
Useful Tips
-------------------------------------------------------

   1. Configure a system environment variable called "TCIA_HOME" and point it at 
      the directory that contains all of your local TCIA directories and files.
      When the menu asks for a directory, just click the <Enter> key, and the 
      application will automatically search for a directory with the name of the
      Collection or Patient to be updated.
      If no %TCIA_HOME% environment variable is configured, the application will
      use the current working directory as the home directory.
   2. Create a properties file in your %TCIA_HOME% directory. Use this file to
      store repetitive information to avoid having to manually enter.  The only
      name requirements for the file are the ".properties" extension.
      Optional properties:
      (a) api_key: When asked to enter an API_KEY, just hit the <Enter> key, and
          the application will automatically search for one in your properties file.
      (b) collections: For #18 in the menu, this property is expected to be configured 
	      with a comma-delimited list of valid Collection names to be updated.
      (c) patients: For #19 in the menu, this property is expected to be configured 
	      with a comma-delimited list of valid Patient IDs to be updated.
          
          
Sample Property File
-------------------------------------------------------

#TCIA User Configuration File;
#Tue Apr 11 03:29:31 EST 2017
#Key below is not valid

api_key=12345678-1234-9876-a5a5-1h84hd84j234
collections=Lung Phantom,RIDER Breast MRI
patients=4482356,RIDER-2217584661


User Requirements
-----------------

   1. Install Python 3.3 or later
   2. Install pip 9.0.1
   3. Install pydicom 0.9.9
      Use command:  pip install pydicom


Sample Test Cases
-----------------

   Coming Soon.


Troubleshooting
------------------------

   Coming Soon.


Bug Reports and Feedback
------------------------

   Please report any bugs and feedback to:
   * Phone (voice or text): +1 385-275-8242 (ASK-TCIA)
   * Email:help@cancerimagingarchive.net




