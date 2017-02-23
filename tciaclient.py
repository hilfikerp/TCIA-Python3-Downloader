import os
import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error
import shutil
import dicom
import json
import zipfile
import errno


#
# Refer https://wiki.cancerimagingarchive.net/display/Public/REST+API+Usage+Guide for complete list of API
#
class TCIAClient:
    GET_COLLECTION_VALUES = "getCollectionValues" 
    GET_MODALITY_VALUES = "getModalityValues" 
    GET_BODY_PART_VALUES = "getBodyPartValues" 
    GET_MANUFACTURER_VALUES = "getManufacturerValues" 
    GET_PATIENT = "getPatient" 
    PATIENTS_BY_MODALITY = "PatientsByModality" 
    GET_PATIENT_STUDY = "getPatientStudy" 
    GET_SERIES = "getSeries" 
    GET_SERIES_SIZE = "getSeriesSize" 
    GET_IMAGE = "getImage" 
    NEW_PATIENTS_IN_COLLECTION = "NewPatientsInCollection" 
    NEW_STUDIES_IN_PATIENT_COLLECTION = "NewStudiesInPatientCollection" 
    GET_SOP_INSTANCE_UIDS = "getSOPInstanceUIDs" 
    GET_SINGLE_IMAGE = "getSingleImage" 
    CONTENTS_BY_NAME = "ContentsByName"
    

    def __init__(self, apiKey , baseUrl, resource):
        self.apiKey = apiKey
        self.baseUrl = baseUrl + "/" + resource

    def execute(self, url, queryParameters={}):
        queryParameters = dict((k, v) for k, v in queryParameters.items() if v)
        headers = {"api_key" : self.apiKey }
        queryString = "?%s" % urllib.parse.urlencode(queryParameters)
        requestUrl = url + queryString
        print(requestUrl)
        request = urllib.request.Request(url=requestUrl , headers=headers)
        resp = urllib.request.urlopen(request)
        return resp
    
    def execute_download(self, url, fileName, queryParameters={}):
        try:
            queryParameters = dict((k, v) for k, v in queryParameters.items() if v)
            headers = {"api_key" : self.apiKey }
            queryString = "?%s" % urllib.parse.urlencode(queryParameters)
            requestUrl = url + queryString
            print(requestUrl)
            request = urllib.request.Request(url=requestUrl , headers=headers)
            # Download the file from `url` and save it locally under `file_name`:
            with urllib.request.urlopen(request) as response, open(fileName, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            out_file.close
        except urllib.error.HTTPError as e:
            print("HTTP Error:",e.code , requestUrl)
            return False
        except urllib.error.URLError as e:
            print("URL Error:",e.reason , requestUrl)
            return False
        return True



    def get_collection_values(self,outputFormat = "json" ):
        serviceUrl = self.baseUrl + "/query/" + self.GET_COLLECTION_VALUES
        queryParameters = { "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp
    
    
    def get_modality_values(self,collection = None , bodyPartExamined = None , modality = None , outputFormat = "json" ):
        serviceUrl = self.baseUrl + "/query/" + self.GET_MODALITY_VALUES
        queryParameters = {"Collection" : collection , "BodyPartExamined" : bodyPartExamined , "Modality" : modality , "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp
    
    
    def get_body_part_values(self,collection = None , bodyPartExamined = None , modality = None , outputFormat = "json" ):
        serviceUrl = self.baseUrl + "/query/" + self.GET_BODY_PART_VALUES
        queryParameters = {"Collection" : collection , "BodyPartExamined" : bodyPartExamined , "Modality" : modality , "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp
    

    def get_manufacturer_values(self,collection = None , bodyPartExamined = None, modality = None , outputFormat = "json"):
        serviceUrl = self.baseUrl + "/query/" + self.GET_MANUFACTURER_VALUES
        queryParameters = {"Collection" : collection , "BodyPartExamined" : bodyPartExamined , "Modality" : modality , "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp
    
    
    def get_patient(self,collection = None , outputFormat = "json" ):
        serviceUrl = self.baseUrl + "/query/" + self.GET_PATIENT
        queryParameters = {"Collection" : collection , "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp 
    
    
    def patients_by_modality(self,collection = None , modality = None, outputFormat = "json" ):
        serviceUrl = self.baseUrl + "/query/" + self.PATIENTS_BY_MODALITY
        queryParameters = {"Collection" : collection , "Modality" : modality, "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp
    
    
    def get_patient_study(self,collection = None , patientId = None , studyInstanceUid = None , outputFormat = "json" ):
        serviceUrl = self.baseUrl + "/query/" + self.GET_PATIENT_STUDY
        queryParameters = {"Collection" : collection , "PatientID" : patientId , "StudyInstanceUID" : studyInstanceUid , "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp
    
    
    def get_series(self, 
                   collection = None , 
                   studyInstanceUid = None , 
                   patientId = None , 
                   seriesInstanceUid = None , 
                   modality = None , 
                   bodyPartExamined = None , 
                   manufacturerModelName = None, 
                   manufacturer = None, 
                   outputFormat = "json" ):
        serviceUrl = self.baseUrl + "/query/" + self.GET_SERIES
        queryParameters = {"Collection" : collection , 
                           "StudyInstanceUID" : studyInstanceUid , 
                           "PatientID" : patientId , 
                           "SeriesInstanceUID" : seriesInstanceUid , 
                           "Modality" : modality , 
                           "BodyPartExamined" : bodyPartExamined , 
                           "ManufacturerModelName" : manufacturerModelName , 
                           "Manufacturer" : manufacturer ,
                           "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp

    
    def get_series_size(self, SeriesInstanceUID = None, outputFormat = "json"):
        serviceUrl = self.baseUrl + "/query/" + self.GET_SERIES_SIZE
        queryParameters = {"SeriesInstanceUID" : SeriesInstanceUID, "format" :
                           outputFormat}
        resp = self.execute(serviceUrl, queryParameters)
        return resp


    def get_image(self , seriesInstanceUid , downloadPath, zipFileName):
        serviceUrl = self.baseUrl + "/query/" + self.GET_IMAGE
        queryParameters = { "SeriesInstanceUID" : seriesInstanceUid }
        os.umask(0o002)
        try:
            file = os.path.join(downloadPath, zipFileName)
            resp = self.execute( serviceUrl , queryParameters)
            downloaded = 0
            CHUNK = 256 * 10240
            with open(file, 'wb') as fp:
                while True:
                    chunk = resp.read(CHUNK)
                    downloaded += len(chunk)
                    if not chunk: break
                    fp.write(chunk)
        except urllib.error.HTTPError as e:
            print("HTTP Error:",e.code , serviceUrl)
            return False
        except urllib.error.URLError as e:
            print("URL Error:",e.reason , serviceUrl)
            return False
        return True
    
    
    def new_patients_in_collection(self,
                                   date = None ,  
                                   collection = None , 
                                   outputFormat = "json" ):
        serviceUrl = self.baseUrl + "/query/" + self.NEW_PATIENTS_IN_COLLECTION
        queryParameters = {"Date" : date , 
                           "Collection" : collection , 
                           "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp
    
    
    def new_studies_in_patient_collection(self,
                                          date = None ,  
                                          collection = None , 
                                          patientId = None , 
                                          outputFormat = "json" ):
        serviceUrl = self.baseUrl + "/query/" + self.NEW_STUDIES_IN_PATIENT_COLLECTION
        queryParameters = {"Date" : date , 
                           "Collection" : collection , 
                           "PatientID" : patientId , 
                           "format" : outputFormat }
        resp = self.execute(serviceUrl , queryParameters)
        return resp
    
    
    def get_sop_instance_uids(self, SeriesInstanceUID = None, outputFormat = "json"):
        serviceUrl = self.baseUrl + "/query/" + self.GET_SOP_INSTANCE_UIDS
        queryParameters = {"SeriesInstanceUID" : SeriesInstanceUID, "format" :
                           outputFormat}
        resp = self.execute(serviceUrl, queryParameters)
        return resp
    
    
    def get_single_image(self, SeriesInstanceUID, SOPInstanceUID, downloadPath, fileName):
        serviceUrl = self.baseUrl + "/query/" + self.GET_SINGLE_IMAGE
        queryParameters = {"SeriesInstanceUID" : SeriesInstanceUID, 
                           "SOPInstanceUID" : SOPInstanceUID}
        file = os.path.join(downloadPath, fileName)
        resp = self.execute_download(url=serviceUrl, fileName=file, queryParameters=queryParameters)
        return resp
    

    def contents_by_name(self, name = None):
        serviceUrl = self.baseUrl + "/query/" + self.CONTENTS_BY_NAME
        queryParameters = {"name" : name}
        resp = self.execute(serviceUrl,queryParameters)
        return resp
    
    
    def dump(self, obj):
        for attr in dir(obj):
            if hasattr( obj, attr ):
                print( "obj.%s = %s" % (attr, getattr(obj, attr)))
                
    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

    def safe_open_w(self, path):
        ''' Open "path" for writing, creating any parent directories as needed.
        '''
        self.mkdir_p(path = os.path.dirname(path))
        return path
    
    
    def get_collection(self, rootDirectory = None):
        print('Reading .dcm files...')
        if rootDirectory == None:
            rootDirectory = os.getcwd()
        for (path, dirs, files) in os.walk(rootDirectory, topdown=True, onerror=False):
            for name in files: #Read the current directory
                if name.endswith('.dcm'): #Check for .dcm files
                    dcmfile = dicom.read_file(path + "\\" + name) #if found, then read data
                    print(type(dcmfile))
                    #print (dcmfile.SeriesInstanceUID)
                    #print(dcmfile.SOPInstanceUID)
                    self.dump(obj=dcmfile)
                    return None
        return None
    
    
    def get_series_path(self, rootDirectory = None, downloadPath = None):   
        for (path, dirs, files) in os.walk(downloadPath, topdown=True, onerror=False):
            for name in files: #Read the current directory
                if name.endswith('.dcm'): #Check for .dcm files
                    dcmfile = dicom.read_file(path + "\\" + name) #if found, then read data
                    return rootDirectory + dcmfile.PatientID + "\\" + dcmfile.StudyInstanceUID + "\\"
              
    
    def get_local_series(self, rootDirectory = None):   
        localSeries = []       
        for (path, dirs, files) in os.walk(rootDirectory, topdown=True, onerror=False):
            for name in files: #Read the current directory
                if name.endswith('.dcm'): #Check for .dcm files
                    dcmfile = dicom.read_file(path + "\\" + name) #if found, then read data
                    localSeries.append(dcmfile.SeriesInstanceUID)
                    break
        localSeries = list(set(localSeries)) #Remove duplicates from list
        localSeries.sort()
        return localSeries
    
    def get_remote_series(self, collection = None):   
        response = self.get_series(collection = collection,
                                   studyInstanceUid = None, 
                                   patientId = None,
                                   seriesInstanceUid = None,
                                   modality = None,
                                   bodyPartExamined = None,
                                   manufacturerModelName = None,
                                   manufacturer = None,
                                   outputFormat = "json")
        remoteSeriesObj = json.load(response)
        remoteSeries = []
        for series in remoteSeriesObj:
            remoteSeries.append(series["SeriesInstanceUID"])
        remoteSeries = list(set(remoteSeries)) #Remove duplicates from list
        remoteSeries.sort()
        return remoteSeries
    
    def downloadMissing(self, rootDirectory = "./", seriesInstanceUids = None):   
        for seriesInstanceUid in seriesInstanceUids:
            response = self.get_sop_instance_uids(seriesInstanceUid)
            responseSopObj = json.load(response)
            sopInstanceUids = []

            for uid in responseSopObj:
                sopInstanceUids.append(uid["sop_instance_uid"])
            sopInstanceUids = list(set(sopInstanceUids))
            sopInstanceUids.sort()
            print(sopInstanceUids)
            
            response = self.get_series(seriesInstanceUid = seriesInstanceUid)
            seriesLst = json.load(response)
            series = seriesLst[0]
            print(series)
            
            print('Downloading ' + series["SeriesDate"] + '-' + series["SeriesDescription"] + '...')
            numberOfImages = len(sopInstanceUids)
            for idx, sopInstanceUid in enumerate(sopInstanceUids):
                print('Downloading ' + str(idx) + ' of ' + str(numberOfImages) + '...')

                #downloadPath = rootDirectory + series[PatientID] + '/' + series[StudyDate] + '-' + series[StudyDescription] + '/' + series[SeriesDate] + '-' + series[SeriesDescription] + '/'
                downloadPath = rootDirectory + series["SeriesDate"] + '_' + series["SeriesDescription"] + '\\'
                self.get_single_image(SeriesInstanceUID = seriesInstanceUid, 
                                      SOPInstanceUID = sopInstanceUid, 
                                      downloadPath = downloadPath, 
                                      fileName = format(idx, '06d') + '.dcm')
        return len(seriesInstanceUids)
    
    def downloadMissingZipAndExtract(self, rootDirectory = "./", seriesInstanceUids = None):   
        for seriesInstanceUid in seriesInstanceUids:          
            print("\nDownloading " + seriesInstanceUid + "...")
            downloadPath = rootDirectory + seriesInstanceUid + "\\"
            zipFileName = seriesInstanceUid + '.zip'
            self.get_image(seriesInstanceUid = seriesInstanceUid, 
                           downloadPath = self.safe_open_w(path = downloadPath), 
                           zipFileName = zipFileName)
            zipf = os.path.join(downloadPath, zipFileName)
            print("Extracting to " + downloadPath)
            with zipfile.ZipFile(zipf, "r") as z:
              z.extractall(downloadPath + seriesInstanceUid)
            os.remove(zipf)
            print("Extracted " + seriesInstanceUid)
            
            seriesPath = self.get_series_path(rootDirectory = rootDirectory, downloadPath = downloadPath)
            self.safe_open_w(path = seriesPath)
            destPath = shutil.move(src = downloadPath + seriesInstanceUid, dst = seriesPath)
            shutil.rmtree(downloadPath)
            print("Files have been moved to " + destPath)

        return len(seriesInstanceUids)
    
    def update_collection(self, rootDirectory = "./", collection = None):
        try:
            if collection == None : #If user doesn't specify a collection, find it in a DCM file 
                #collection = self.get_collection(rootDirectory)
                return None
                
            print("\nCollecting remote series...")
            remoteSeries = self.get_remote_series(collection)
            print(str(len(remoteSeries)) + " remote series found.")
            
            print("\nCollecting local series...")
            localSeries = self.get_local_series(rootDirectory = rootDirectory)
            print(str(len(localSeries)) + " local series found.\n")
            
            missingSeries = list(set(remoteSeries) - set(localSeries))
            missingSeries.sort()
            
            print("\n" + str(self.downloadMissingZipAndExtract(rootDirectory = rootDirectory, seriesInstanceUids = missingSeries)) + " new series have been added to your collection.")
            
        except urllib.error.HTTPError as err:
            print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
            
        return 'true'