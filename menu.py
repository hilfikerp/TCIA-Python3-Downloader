from tciaclient import TCIAClient
import os, urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error, sys


####################################  Function to print server response #######
def printServerResponse(response):
    if response.getcode() == 200:
        print("Server Returned:\n")
        print(response.read())
        print("\n")
    else:
        print("Error: " + str(response.getcode()))
        
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD.\n")
        
def find_dir_by_name(rootDirectory = None, directoryName = None):    
    if rootDirectory == None or rootDirectory == "": 
        rootDirectory = os.getcwd()
    if directoryName == None:
        return None
    for dirName, subdirList, fileList in os.walk(rootDirectory):
        if directoryName == os.path.basename(dirName):
            print('Found directory: %s' % dirName)
            return os.path.join(dirName,'')
    print("Not found.")
    return None

def load_tcia_properties():    
    tciaHome = find_tcia_home()
    print("\nSearching for TCIA properties file in '" + tciaHome + "'.")
        
    for (path, dirs, files) in os.walk(tciaHome, topdown=True, onerror=False):
       for name in files: #Read the current directory
          if name.endswith('.properties'): #Check for .properties files    
             tciaPropertyFile = os.path.join(path, name)
             tcia_properties = {}
             with open(tciaPropertyFile) as f:
                for line in f:
                   tokens = line.split('=')
                   tcia_properties[tokens[0].lower()] = '='.join(tokens[1:])
             print("TCIA properties loaded from '" + tciaPropertyFile + "'.")
             return tcia_properties  
    print("Property file not found.\n")
    return None

def find_tcia_home():
    tcia_home = os.path.expandvars("%TCIA_HOME%")
    if (tcia_home == "%TCIA_HOME%"):
       print("\nSearching in current working directory = '" + os.getcwd() + "'")
       return os.getcwd()
    else:
       print("\nSearching in %TCIA_HOME% = '" + tcia_home + "'")
       return tcia_home
        

def main():

   print("\n")
   print ("Welcome to the TCIA Request Application.")
   print ("Please refer to the ReadMe file for useful tips on how to simplify repetitive requests.")
   print("\n")
   api_key_found = 0
   while api_key_found == 0:
      api_key_string = input("Please supply an API_KEY to access the TCIA data (Press <Enter> key to load from properties file):")
      if (api_key_string == None or api_key_string == ""):
         tcia_properties = load_tcia_properties()
         if tcia_properties == None:
            print("Unable to locate an API_KEY value.\n")
         else:
            api_key_string = tcia_properties["api_key"].strip()
            print("API_KEY successfully loaded from properties file.")
            api_key_found = 1
      else:
         api_key_found = 1

   while menu(api_key_string) == 1: pass
   print

def menu(api_key_string = None):

   tcia_client = TCIAClient(apiKey = api_key_string,baseUrl="https://services.cancerimagingarchive.net/services/v3",resource = "TCIA")
   tcia_client2 = TCIAClient(apiKey = api_key_string,baseUrl="https://services.cancerimagingarchive.net/services/v3",resource="SharedList")

   print("\n")
   print ("1) Get Collection Values")
   print ("2) Get Modality Values")
   print ("3) Get Body Part Values")
   print ("4) Get Manufacturer Values")
   print ("5) Get Patient")
   print ("6) Patients By Modality")
   print ("7) Get Patient Study")
   print ("8) Get Series")
   print ("9) Get Series Size")
   print ("10) Get Image")
   print ("11) New Patients in Collection")
   print ("12) New Studies in Patient Collection")
   print ("13) Get SOP Instance UIDs")
   print ("14) Get Single Image")
   print ("15) Contents By Name")
   print ("16) Update Collection")
   print ("17) Update Patient")
   print ("18) Update All Collections (No Prompts)") 
   print ("19) Update All Patients (No Prompts)") 
   print("\n")
   
   actionString = input("Which action (Type 'q' to quit)? ")
   if (actionString == "" or actionString.lower() == 'q' or actionString.lower() == "quit"):
      print("Thank you.  You have exited the TCIA Request Application.")
      print("\n")
      return 0
  
   try:
      action = int(actionString)
      if action < 1 or action > 19:
         raise ValueError("Invalid action.")
   except:
      print("Not a valid action. Press <Enter> or type 'quit' to exit TCIA menu.")
      return 1
   
   if action == 11 or action == 12:
      validDate = 0
      while validDate == 0:
         dateString = input("Enter the First Date (YYYY-MM-DD) to be included in this search: ")
         try:
            validate(date_text)
            validDate = 1
         except ValueError as err:
            print(err.read) 
         
   if action == 2 or action == 3 or action == 4 or action == 5 or action == 6 or action == 7 or action == 8 or action == 11 or action == 12 or action == 16:
      collectionString = input("Enter the Collection: ")
      if (collectionString == ""):
         collectionString = None

   if action == 7 or action == 8:
      studyInstanceUIDString = input("Enter the Study Instance UID: ")
      if (studyInstanceUIDString == ""):
         studyInstanceUIDString = None
         
   if action == 7 or action == 8 or action == 17:
      patientIDString = input("Enter the Patient ID: ")
      if (patientIDString == ""):
         patientIDString = None
         
   if action == 8 or action == 9 or action == 10 or action == 13 or action == 14:
      seriesInstanceUIDString = input("Enter the Series Instance UID: ")
      if (seriesInstanceUIDString == ""):
         seriesInstanceUIDString = None
         
   if action == 3 or action == 4 or action == 6 or action == 8:
      modalityString = input("Enter the Modality: ")
      if (modalityString == ""):
         modalityString = None
         
   if action == 2 or action == 4 or action == 8:
      bodyPartExaminedString = input("Enter the Body Part Examined: ")
      if (bodyPartExaminedString == ""):
         bodyPartExaminedString = None
         
   if action == 8:
      manufacturerModelNameString = input("Enter the Manufacturer Model Name: ")
      if (manufacturerModelNameString == ""):
         manufacturerModelNameString = None
   
   if action == 8:
      manufacturerString = input("Enter the Manufacturer: ")
      if (manufacturerString == ""):
         manufacturerString = None
   
   if action == 14:
      sopInstanceUIDString = input("Enter the SOP Instance UID: ")
      if (sopInstanceUIDString == ""):
         sopInstanceUIDString = None
   
   if action == 15:
      nameString = input("Enter the Name: ")
      if (nameString == ""):
         nameString = None
         
   if action != 10 and action != 13 and action != 14 and action < 16:
      outputFormatString = input("Enter the desired Output Format (CSV, HTML, XML, JSON): ")
      if (outputFormatString == ""):
         outputFormatString = "JSON"
         
   if action == 10 or action == 14:
      filePath = input("Enter the desired path of the download file: ")
      if (filePath == ""):
         filePath = os.getcwd()
      else:
         filePath = os.path.join(filePath.translate({ord(i):None for i in '\"\''}).strip(), '')
         
   if action == 10:
      fileName = input("Enter the desired name of the download file: ")
      if (fileName == ""):
         fileName = "TCIA_Images.zip"
         
   if action == 14:
      fileName = input("Enter the desired name of the download file: ")
      if (fileName == ""):
         fileName = "TCIA_SingleImage.dcm"
         
   if action == 16:
      validDir = 0
      while validDir == 0:
         rootDirectoryString = input("Enter the root directory containing the images for the Collection (Press <Enter> key to search for directory): ")
         if (rootDirectoryString == None or rootDirectoryString == ""):
            print("\nSearching for directory with the name '" + collectionString + "'.")
            tcia_home = find_tcia_home()
            collectionDir = find_dir_by_name(rootDirectory = tcia_home, directoryName = collectionString)
            if collectionDir == None or collectionDir == "":
               print("Unable to locate a directory with the name '" + collectionString + "'.")
            else:
               rootDirectoryString = collectionDir
               validDir = 1
         else:
            try:
               print(rootDirectoryString)
               rootDirectoryString = os.path.join(rootDirectoryString.translate({ord(i):None for i in '\"\''}).strip(), '')
               validDir = 1
            except:
               print("Invalid directory.\n")
         
   if action == 17:
      validDir = 0
      while validDir == 0:
         rootDirectoryString = input("Enter the root directory containing the images for the Patient (Press <Enter> key to search for directory): ")
         if (rootDirectoryString == None or rootDirectoryString == ""):
            print("\nSearching for directory with the name '" + patientIDString + "'.")
            tcia_home = find_tcia_home()
            patientDir = find_dir_by_name(rootDirectory = tcia_home, directoryName = patientIDString)
            if patientDir == None or patientDir == "":
               print("Unable to locate a directory with the name '" + patientIDString + "'.\n")
            else:
               rootDirectoryString = patientDir
               validDir = 1
         else:
            try:
               print(rootDirectoryString)
               rootDirectoryString = os.path.join(rootDirectoryString.translate({ord(i):None for i in '\"\''}).strip(), '')
               validDir = 1
            except:
               print("Invalid directory.\n")
         
         
   
   if action == 1 :
       
      # Execute get_collection_values
      try:
          response = tcia_client.get_collection_values(outputFormat = outputFormatString)
          #print("\nQuery TCIA - getCollectionValues(outputFormat)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")
          
   elif action == 2:
       
      # Execute get_modality_values with query Parameter
      try:
          response = tcia_client.get_modality_values(collection = collectionString,bodyPartExamined = bodyPartExaminedString,outputFormat = outputFormatString)
          #print("\nQuery TCIA - getModalityValues(null, BRAIN, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 3:
       
      # Execute get_body_part_values with query Parameter
      try:
          response = tcia_client.get_body_part_values(collection = collectionString,modality = modalityString,outputFormat = outputFormatString)
          #print("\nQuery TCIA - getBodyPartValues(TCA-GBM, null, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 4:
       
      # Execute get_manufacturer_values no query parameters
      try:
          response = tcia_client.get_manufacturer_values(collection = collectionString,
                                                         bodyPartExamined = bodyPartExaminedString,
                                                         modality = modalityString,
                                                         outputFormat = outputFormatString)
          #print("\nQuery TCIA - getManufacturerValues(Null, Null, Null, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 5:
       
      # Execute get_patient with collection query parameter
      try:
          response = tcia_client.get_patient(collection = collectionString,
                                             outputFormat = outputFormatString)
          #print("\nQuery TCIA - getPatient(TCGA-GBM, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 6:
       
      # Execute patients_by_modality with collection and modality query parameter
      try:
          response = tcia_client.patients_by_modality(collection = collectionString,
                                                      modality = modalityString,
                                                      outputFormat = outputFormatString)
          #print("\nQuery TCIA - PatientsByModality(TCGA-GBM, MR, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 7:
       
      # Execute get_patient_study with collection and patientId query parameter
      try:
          response = tcia_client.get_patient_study(collection = collectionString,
                                                   patientId = patientIDString,
                                                   studyInstanceUid = studyInstanceUIDString,
                                                   outputFormat = outputFormatString)
          #print("\nQuery TCIA - getPatientStudy(TCGA-GBM, TCGA-08-0244, Null, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 8:
       
      # Execute get_series with collection and patientId query parameter
      try:
          response = tcia_client.get_series(collection = collectionString,
                                            studyInstanceUid = studyInstanceUIDString, 
                                            patientId = patientIDString,
                                            seriesInstanceUid = seriesInstanceUIDString,
                                            modality = modalityString,
                                            bodyPartExamined = bodyPartExaminedString,
                                            manufacturerModelName = manufacturerModelNameString,
                                            manufacturer = manufacturerString,
                                            outputFormat = outputFormatString)
          #print("\nQuery TCIA - getSeries(TCGA-GBM, TCGA-08-0244, Null, Null, Null, Null, Null, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 9:
       
      # Execute get_series_size
      try:
          response = tcia_client.get_series_size(SeriesInstanceUID=seriesInstanceUIDString, outputFormat = outputFormatString)
          #print("\nQuery TCIA - getSeriesSize(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 10:
       
      # Execute get_image.
      # NOTE: Image response consumed differently
      try:
          response = tcia_client.get_image(seriesInstanceUid = seriesInstanceUIDString, downloadPath = filePath, zipFileName = fileName);
          #print("\nQuery TCIA - getImage(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440, DownloadPath, FileLocation)")
          print(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 11:
       
      # Execute new_patients_in_collection with collection and date query parameter
      try:
          response = tcia_client.new_patients_in_collection(collection = collectionString, date = dateString, outputFormat = outputFormatString)
          #print("\nQuery TCIA - NewPatientsInCollection(TCGA-GBM, 2014-06-01, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 12:
       
      # Execute new_studies_in_patient_collection with collection and date query parameter
      try:
          response = tcia_client.new_studies_in_patient_collection(collection = collectionString, date = dateString, patientId = patientIDString, outputFormat = outputFormatString)
          #print("\nQuery TCIA - NewStudiesInPatientCollection(TCGA-GBM, 2014-06-01, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 13:
       
      # Execute get_sop_instance_uids with SeriesInstanceUID query parameter
      try:
          response = tcia_client.get_sop_instance_uids(SeriesInstanceUID = seriesInstanceUIDString, outputFormat = outputFormatString)
          #print("\nQuery TCIA - getSeriesInstanceUIDs(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440, JSON)")
          printServerResponse(response);
      except:
          print("Error executing program.  Please verify input.\n")

   elif action == 14:
       
      # Execute get_single_image with SeriesInstanceUID and SOPInstanceUID query parameter
      try:
          response = tcia_client.get_single_image(SeriesInstanceUID = seriesInstanceUIDString,
                                                  SOPInstanceUID = sopInstanceUIDString, 
                                                  downloadPath = filePath, 
                                                  fileName = fileName)
          #print("\nQuery TCIA - getSingleImage(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440, 1.3.6.1.4.1.14519.5.2.1.7695.4001.152032524561037056647374573281, SingleImage.dcm)")
          print(response);
      except:
          print("Error executing program.  Please verify input.\n")
    
   elif action == 15:
       
       # Execute content_by_name
       try:
          response = tcia_client2.contents_by_name(name = nameString)
          #print("\nQuery TCIA - getContentsByName(sharedListApiUnitTest)")
          printServerResponse(response);
       except:
          print("Error executing program.  Please verify input.\n")
          
   elif action == 16:
       
       # Execute update_collection
       try:
          missingSeries = tcia_client.find_missing_series_collection(collection = collectionString,
                                                                     rootDirectory = rootDirectoryString)
          if (len(missingSeries) < 1):          
             print("Collection '" + collectionString + "' is up-to-date.")
             return 1

          proceedWithDownload = input("Would you like to download the " + str(len(missingSeries)) + " missing series to '" + rootDirectoryString + "' (Y or N)? ")
          if (proceedWithDownload.lower() != "y" and proceedWithDownload.lower() != "yes"):
             print("Collection update request has been cancelled.")
          else:           
             downloadedSeries = tcia_client.downloadAndExtractToCollection(rootDirectory = rootDirectoryString, seriesInstanceUids = missingSeries)
             print("\n" + str(downloadedSeries) + " new series have been added to your collection.")
             print('Update is complete.')
       except:
          print("Error executing program.  Please verify input.\n")
          
   elif action == 17:
       
       # Execute update_patient
       try:
          missingSeries = tcia_client.find_missing_series_patient(patientID = patientIDString,
                                                                  rootDirectory = rootDirectoryString)
          if (len(missingSeries) < 1):          
             print("Patient '" + patientIDString + "' is up-to-date.")
             return 1
         
          proceedWithDownload = input("Would you like to download the " + str(len(missingSeries)) + " missing series to '" + rootDirectoryString + "' (Y or N)? ")
          if (proceedWithDownload.lower() != "y" and proceedWithDownload.lower() != "yes"):
             print("Collection update request has been cancelled.")
          else:           
             downloadedSeries = tcia_client.downloadAndExtractToPatient(rootDirectory = rootDirectoryString, seriesInstanceUids = missingSeries)
             print("\n" + str(downloadedSeries) + " new series have been added to your collection.")
             print('Update is complete.')
       except:
          print("Error executing program.  Please verify input.\n")
          
   elif action == 18:
      tcia_properties = load_tcia_properties()
      if tcia_properties == None:
        print("Unable to locate a Collections list. Please refer to ReadMe file to use this feature.\n")
      else:
        collections_string = tcia_properties["collections"]
        print("Collections successfully loaded from properties file.")
        
      tcia_home = find_tcia_home()
      print("Searching in '" + tcia_home + "'")
      
      collection_list = collections_string.split(",")  
      for collection in collection_list:
         collectionString = collection.strip()
         print("\nCurrent collection = '" + collectionString + "'")
         print("Searching for directory with the name '" + collectionString + "'.")

         collectionDir = find_dir_by_name(rootDirectory = tcia_home, directoryName = collectionString)
         if collectionDir == None or collectionDir == "":
            print("Unable to locate a directory with the name '" + collectionString + "'.")
            print("Update not executed for collection '" + collectionString + "'")
            continue
         else:
            rootDirectoryString = collectionDir
            try:
               print(rootDirectoryString)
               rootDirectoryString = os.path.join(rootDirectoryString.translate({ord(i):None for i in '\"\''}).strip(), '')
            except:
               print("Invalid directory: '" + rootDirectoryString + "'")
               print("Update not executed for collection '" + collectionString + "'")
               continue
                  
         # Execute update_collection
         try:
            missingSeries = tcia_client.find_missing_series_collection(collection = collectionString,
                                                                       rootDirectory = rootDirectoryString)
            if (len(missingSeries) > 0):
               print("Downloading the " + str(len(missingSeries)) + " missing series to '" + rootDirectoryString + "'...")
               downloadedSeries = tcia_client.downloadAndExtractToCollection(rootDirectory = rootDirectoryString, seriesInstanceUids = missingSeries)
               print("\n" + str(downloadedSeries) + " new series have been added to your collection.")
               print("Update is complete for collection '" + collectionString + "'")
            else:           
               print("Collection '" + collectionString + "' is up-to-date.")
         except:
            print("Error executing program. Update not executed for collection '" + collectionString + "'")
      print("\nUpdate request is complete.")
            
   elif action == 19:
      tcia_properties = load_tcia_properties()
      if tcia_properties == None:
        print("Unable to locate a Patients list. Please refer to ReadMe file to use this feature.\n")
      else:
        patients_string = tcia_properties["patients"]
        print("Patients successfully loaded from properties file.")
        
      tcia_home = find_tcia_home()
      print("Searching in '" + tcia_home + "'")
      
      patient_list = patients_string.split(",")  
      for patient in patient_list:
         patientIDString = patient.strip()
         print("\nCurrent patient = '" + patientIDString + "'")
         print("Searching for directory with the name '" + patientIDString + "'.")

         patientDir = find_dir_by_name(rootDirectory = tcia_home, directoryName = patientIDString)
         if patientDir == None or patientDir == "":
            print("Unable to locate a directory with the name '" + patientIDString + "'.")
            print("Update not executed for patient '" + patientIDString + "'")
            continue
         else:
            rootDirectoryString = patientDir
            try:
               print(rootDirectoryString)
               rootDirectoryString = os.path.join(rootDirectoryString.translate({ord(i):None for i in '\"\''}).strip(), '')
            except:
               print("Invalid directory: '" + rootDirectoryString + "'")
               print("Update not executed for patient '" + patientIDString + "'")
               continue
                  
         # Execute update_patient
         try:
            missingSeries = tcia_client.find_missing_series_patient(patientID = patientIDString,
                                                                    rootDirectory = rootDirectoryString)
            if (len(missingSeries) > 0):
               print("Downloading the " + str(len(missingSeries)) + " missing series to '" + rootDirectoryString + "'...")
               downloadedSeries = tcia_client.downloadAndExtractToPatient(rootDirectory = rootDirectoryString, seriesInstanceUids = missingSeries)
               print("\n" + str(downloadedSeries) + " new series have been added to your collection.")
               print("Update is complete for patient '" + patientIDString + "'")
            else:           
               print("Patient '" + patientIDString + "' is up-to-date.")
         except:
            print("Error executing program. Update not executed for patient '" + patientIDString + "'")
      print("\nUpdate request is complete.")


   return 1

main()
