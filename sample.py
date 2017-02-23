from tciaclient import TCIAClient
import urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error,sys
import json


####################################  Function to print server response #######
def printServerResponse(response):
    if response.getcode() == 200:
        print("Server Returned:\n")
        print(response.read())
        print("\n")
    else:
        print("Error: " + str(response.getcode()))

####################################  Create Clients for Two Different Resources  ####
tcia_client = TCIAClient(apiKey = "7ad8c98d-74f9-4ebf-a59c-c3de09550db4",baseUrl="https://services.cancerimagingarchive.net/services/v3",resource = "TCIA")
tcia_client2 = TCIAClient(apiKey ="7ad8c98d-74f9-4ebf-a59c-c3de09550db4",baseUrl="https://services.cancerimagingarchive.net/services/v3",resource="SharedList")



# Test get_collection_values
try:
    response = tcia_client.get_collection_values()
    print("\nQuery TCIA - getCollectionValues()")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_modality_values with query Parameter
try:
    response = tcia_client.get_modality_values(collection = None,bodyPartExamined = "BRAIN",outputFormat = "json")
    print("\nQuery TCIA - getModalityValues(null, BRAIN, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_modality_values with query Parameter
try:
    response = tcia_client.get_modality_values(collection = "TCGA-GBM",bodyPartExamined = None,outputFormat = "json")
    print("\nQuery TCIA - getModalityValues(TCA-GBM, null, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    

# Test get_body_part_values with query Parameter
try:
    response = tcia_client.get_body_part_values(collection = "TCGA-GBM",modality = None,outputFormat = "json")
    print("\nQuery TCIA - getBodyPartValues(TCA-GBM, null, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_body_part_values with query Parameter
try:
    response = tcia_client.get_body_part_values(collection = None,modality = "MR",outputFormat = "json")
    print("\nQuery TCIA - getBodyPartValues(null, MR, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_manufacturer_values no query parameters
try:
    response = tcia_client.get_manufacturer_values(collection =
                                                   None,bodyPartExamined =
                                                   None,modality =
                                                   None,outputFormat = "json")
    print("\nQuery TCIA - getManufacturerValues(Null, Null, Null, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_manufacturer_values with collection query parameter
try:
    response = tcia_client.get_manufacturer_values(collection = "TCGA-GBM",
                                                   bodyPartExamined = None,
                                                   modality = None,
                                                   outputFormat = "json")
    print("\nQuery TCIA - getManufacturerValues(TCGA-GBM, Null, Null, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_manufacturer_values with modality query parameter
try:
    response = tcia_client.get_manufacturer_values(collection = None,
                                                   bodyPartExamined = None,
                                                   modality = "MR",
                                                   outputFormat = "json")
    print("\nQuery TCIA - getManufacturerValues(Null, Null, MR, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_manufacturer_values with body_part_examined query parameter
try:
    response = tcia_client.get_manufacturer_values(collection = None,
                                                   bodyPartExamined = "BRAIN",
                                                   modality = None,
                                                   outputFormat = "json")
    print("\nQuery TCIA - getManufacturerValues(Null, BRAIN, Null, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_patient with collection query parameter
try:
    response = tcia_client.get_patient(collection = "TCGA-GBM",
                                       outputFormat = "json")
    print("\nQuery TCIA - getPatient(TCGA-GBM, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test patients_by_modality with collection and modality query parameter
try:
    response = tcia_client.patients_by_modality(collection = "TCGA-GBM",
                                                modality = "MR",
                                                outputFormat = "json")
    print("\nQuery TCIA - PatientsByModality(TCGA-GBM, MR, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    


# Test get_patient_study with collection and patientId query parameter
try:
    response = tcia_client.get_patient_study(collection = "TCGA-GBM",
                                             patientId = "TCGA-08-0244",
                                             studyInstanceUid = None,
                                             outputFormat = "json")
    print("\nQuery TCIA - getPatientStudy(TCGA-GBM, TCGA-08-0244, Null, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_series with collection and patientId query parameter
try:
    response = tcia_client.get_series(collection = "TCGA-GBM",
                                      studyInstanceUid = None, 
                                      patientId = "TCGA-08-0244",
                                      seriesInstanceUid = None,
                                      modality = None,
                                      bodyPartExamined = None,
                                      manufacturerModelName = None,
                                      manufacturer = None,
                                      outputFormat = "json")
    print("\nQuery TCIA - getSeries(TCGA-GBM, TCGA-08-0244, Null, Null, Null, Null, Null, JSON)")
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    print(json_obj.pop()['SeriesInstanceUID'])
    #data = json.load(response)
    #print(list(data.keys))
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_series_size
try:
    response = tcia_client.get_series_size(SeriesInstanceUID="1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440")
    print("\nQuery TCIA - getSeriesSize(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_image.
# NOTE: Image response consumed differently
try:
    response = tcia_client.get_image(seriesInstanceUid ="1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440" , downloadPath  ="./", zipFileName ="images.zip");
    print("\nQuery TCIA - getImage(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440, DownloadPath, FileLocation)")
    print(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())



# Test new_patients_in_collection with collection and date query parameter
try:
    response = tcia_client.new_patients_in_collection(collection = "TCGA-GBM", date = "2014-06-01", outputFormat = "json")
    print("\nQuery TCIA - NewPatientsInCollection(TCGA-GBM, 2014-06-01, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())



# Test new_studies_in_patient_collection with collection and date query parameter
try:
    response = tcia_client.new_studies_in_patient_collection(collection = "TCGA-GBM", date = "2014-06-01", patientId = None, outputFormat = "json")
    print("\nQuery TCIA - NewStudiesInPatientCollection(TCGA-GBM, 2014-06-01, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test new_studies_in_patient_collection with collection, date, and patientId query parameter
try:
    response = tcia_client.new_studies_in_patient_collection(collection = "TCGA-GBM", date = "2014-06-01", patientId = "TCGA-08-0244", outputFormat = "json")
    print("\nQuery TCIA - NewStudiesInPatientCollection(TCGA-GBM, 2014-06-01, TCGA-08-0244, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test get_sop_instance_uids with SeriesInstanceUID query parameter
try:
    response = tcia_client.get_sop_instance_uids(SeriesInstanceUID="1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440", outputFormat = "json")
    print("\nQuery TCIA - getSeriesInstanceUIDs(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440, JSON)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    

    
# Test get_single_image with SeriesInstanceUID and SOPInstanceUID query parameter
try:
    response = tcia_client.get_single_image(SeriesInstanceUID="1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440",
                                            SOPInstanceUID="1.3.6.1.4.1.14519.5.2.1.7695.4001.152032524561037056647374573281", 
                                            downloadPath  ="./", 
                                            fileName ="SingleImage.dcm")
    print("\nQuery TCIA - getSingleImage(1.3.6.1.4.1.14519.5.2.1.7695.4001.306204232344341694648035234440, 1.3.6.1.4.1.14519.5.2.1.7695.4001.152032524561037056647374573281, SingleImage.dcm)")
    print(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
    
    
    
# Test content_by_name
try:
    response = tcia_client2.contents_by_name(name = "sharedListApiUnitTest")
    print("\nQuery TCIA - getContentsByName(sharedListApiUnitTest)")
    printServerResponse(response);
except urllib.error.HTTPError as err:
    print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())