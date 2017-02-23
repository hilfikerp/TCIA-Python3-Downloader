from tciaclient import TCIAClient
import urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error, sys


####################################  Function to print server response #######
def printServerResponse(response):
    if response.getcode() == 200:
        print("Server Returned:\n")
        print(response.read())
        print("\n")
    else:
        print("Error: " + str(response.getcode()))
        

def main():

   print("\n")
   print ("Welcome to the TCIA Request Application.")
   print("\n")
   api_key_string = input("Please supply an API_KEY to access the TCIA data:")
   if (api_key_string == ""):
      print("\n")
      return 0
  
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
   print("\n")
   
   actionString = input("Which action? ")
   if (actionString == "" or actionString == "quit"):
      print("Thank you.  You have exited the TCIA Request Application.")
      print("\n")
      return 0
  
   action = int(actionString)
   
   if action == 11 or action == 12:
      dateString = input("Enter the First Date (YYYY-MM-DD) to be included in this search: ")
      if (dateString == ""):
         dateString = None
         
   if action == 2 or action == 3 or action == 4 or action == 5 or action == 6 or action == 7 or action == 8 or action == 11 or action == 12 or action == 16:
      collectionString = input("Enter the Collection: ")
      if (collectionString == ""):
         collectionString = None

   if action == 7 or action == 8:
      studyInstanceUIDString = input("Enter the Study Instance UID: ")
      if (studyInstanceUIDString == ""):
         studyInstanceUIDString = None
         
   if action == 7 or action == 8:
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
         
   if action != 10 and action != 13 and action != 14 and action != 16:
      outputFormatString = input("Enter the desired Output Format (CSV, HTML, XML, JSON): ")
      if (outputFormatString == ""):
         outputFormatString = "JSON"
         
   if action == 10 or action == 14:
      filePath = input("Enter the desired path of the download file: ")
      if (filePath == ""):
         filePath = "./"
         
   if action == 10:
      fileName = input("Enter the desired name of the download file: ")
      if (fileName == ""):
         fileName = "TCIA_Images.zip"
         
   if action == 14:
      fileName = input("Enter the desired name of the download file: ")
      if (fileName == ""):
         fileName = "TCIA_SingleImage.dcm"
         
   if action == 16:
      rootDirectoryString = input("Enter the root directory containing the images for the Collection: ")
      if (rootDirectoryString == ""):
         rootDirectoryString = None
         
         
   
   if action == 1 :
       
      # Execute get_collection_values
      try:
          response = tcia_client.get_collection_values(outputFormat = outputFormatString)
          #print("\nQuery TCIA - getCollectionValues(outputFormat)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
          
   elif action == 2:
       
      # Execute get_modality_values with query Parameter
      try:
          response = tcia_client.get_modality_values(collection = collectionString,bodyPartExamined = bodyPartExaminedString,outputFormat = outputFormatString)
          #print("\nQuery TCIA - getModalityValues(null, BRAIN, JSON)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 3:
       
      # Execute get_body_part_values with query Parameter
      try:
          response = tcia_client.get_body_part_values(collection = collectionString,modality = modalityString,outputFormat = outputFormatString)
          #print("\nQuery TCIA - getBodyPartValues(TCA-GBM, null, JSON)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 4:
       
      # Execute get_manufacturer_values no query parameters
      try:
          response = tcia_client.get_manufacturer_values(collection = collectionString,
                                                         bodyPartExamined = bodyPartExaminedString,
                                                         modality = modalityString,
                                                         outputFormat = outputFormatString)
          #print("\nQuery TCIA - getManufacturerValues(Null, Null, Null, JSON)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 5:
       
      # Execute get_patient with collection query parameter
      try:
          response = tcia_client.get_patient(collection = collectionString,
                                             outputFormat = outputFormatString)
          #print("\nQuery TCIA - getPatient(TCGA-GBM, JSON)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 6:
       
      # Execute patients_by_modality with collection and modality query parameter
      try:
          response = tcia_client.patients_by_modality(collection = collectionString,
                                                      modality = modalityString,
                                                      outputFormat = outputFormatString)
          #print("\nQuery TCIA - PatientsByModality(TCGA-GBM, MR, JSON)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 7:
       
      # Execute get_patient_study with collection and patientId query parameter
      try:
          response = tcia_client.get_patient_study(collection = collectionString,
                                                   patientId = patientIDString,
                                                   studyInstanceUid = studyInstanceUIDString,
                                                   outputFormat = outputFormatString)
          #print("\nQuery TCIA - getPatientStudy(TCGA-GBM, TCGA-08-0244, Null, JSON)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

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
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 9:
       
      # Execute get_series_size
      try:
          response = tcia_client.get_series_size(SeriesInstanceUID=seriesInstanceUIDString, outputFormat = outputFormatString)
          #print("\nQuery TCIA - getSeriesSize(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 10:
       
      # Execute get_image.
      # NOTE: Image response consumed differently
      try:
          response = tcia_client.get_image(seriesInstanceUid = seriesInstanceUIDString, downloadPath = filePath, zipFileName = fileName);
          #print("\nQuery TCIA - getImage(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440, DownloadPath, FileLocation)")
          print(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 11:
       
      # Execute new_patients_in_collection with collection and date query parameter
      try:
          response = tcia_client.new_patients_in_collection(collection = collectionString, date = dateString, outputFormat = outputFormatString)
          #print("\nQuery TCIA - NewPatientsInCollection(TCGA-GBM, 2014-06-01, JSON)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 12:
       
      # Execute new_studies_in_patient_collection with collection and date query parameter
      try:
          response = tcia_client.new_studies_in_patient_collection(collection = collectionString, date = dateString, patientId = patientIDString, outputFormat = outputFormatString)
          #print("\nQuery TCIA - NewStudiesInPatientCollection(TCGA-GBM, 2014-06-01, JSON)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 13:
       
      # Execute get_sop_instance_uids with SeriesInstanceUID query parameter
      try:
          response = tcia_client.get_sop_instance_uids(SeriesInstanceUID = seriesInstanceUIDString, outputFormat = outputFormatString)
          #print("\nQuery TCIA - getSeriesInstanceUIDs(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440, JSON)")
          printServerResponse(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())

   elif action == 14:
       
      # Execute get_single_image with SeriesInstanceUID and SOPInstanceUID query parameter
      try:
          response = tcia_client.get_single_image(SeriesInstanceUID = seriesInstanceUIDString,
                                                  SOPInstanceUID = sopInstanceUIDString, 
                                                  downloadPath = filePath, 
                                                  fileName = fileName)
          #print("\nQuery TCIA - getSingleImage(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440, 1.3.6.1.4.1.14519.5.2.1.7695.4001.152032524561037056647374573281, SingleImage.dcm)")
          print(response);
      except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
   elif action == 15:
       
       # Execute content_by_name
       try:
          response = tcia_client2.contents_by_name(name = nameString)
          #print("\nQuery TCIA - getContentsByName(sharedListApiUnitTest)")
          printServerResponse(response);
       except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
          
   elif action == 16:
       
       # Execute update_collection
       try:
          response = tcia_client.update_collection(collection = collectionString,
                                                   rootDirectory = rootDirectoryString)
          print('Update is complete.')
       except urllib.error.HTTPError as err:
          print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())


   return 1

main()
