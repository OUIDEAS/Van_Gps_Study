import pymongo
import json
import numpy as np
import matplotlib.pyplot as plt
import csv
import time


################################
########### OPTIONS ############
################################

# ENTER IN THE DATABASE NAME HERE! 
# db_name = 'cyber1'
# db_name = 'cyber2'
# db_name = 'cyber3'
# db_name = 'cyber4'
# db_name = 'cyber5'
# db_name = 'cyber6'
# db_name = 'cyber7'
db_name = 'cyber8'

# ENTER IN THE EPOCH TIME STAMP OF DATA COLLECTION DATE (makes referenceing which data goes to which data set way easier)
# collection_time = '1674155613'
# collection_time = '1684354335'
# collection_time = '1692815820'
# collection_time = '1694450559'
# collection_time = '1695054362'
# collection_time = '1695931464'
# collection_time = '1696265320'
collection_time = '1696869055'



################################
########### VAR INIT ###########
################################

epoch_time = str(time.time())
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient[db_name]
mycol = mydb[db_name]
metadID = mydb['metadata'].find_one({'experimentID': 13})

# topics =[ 
    # "/apollo/sensor/gnss/best_pose",
    # "/apollo/sensor/gnss/corrected_imu",
    # "/apollo/sensor/gnss/ins_stat",
    # "/apollo/sensor/gnss/rtk_eph", # EMPTY???
    # "/apollo/sensor/gnss/rtk_obs", # EMPTY???
    # "/apollo/sensor/gnss/heading", # EMPTY???
    # "/apollo/sensor/gnss/imu", # EMPTY???
    # "/apollo/sensor/gnss/odometry",
    # "/apollo/sensor/gnss/raw_data" # BINARY GIBERISH
#     ]


################################
########### BEST POS ###########
################################

query = {f'topic': '/apollo/sensor/gnss/best_pose'}
print('Now exporting {query}')

latitude = []
longitude = []
latitudeStdDev = []
longitudeStdDev = []
heightStdDev = []
galileoBeidouUsedMask = []
solutionAge = []
extendedSolutionStatus = []
solStatus = []
heightMsl = []
baseStationId = []
numSatsTracked = []
numSatsInSolution = []
solType = []
datumId = []
numSatsL1 = []
differentialAge = []
timestamp = []


if mycol.find_one(query) is not None:
    cursor = mycol.find(query)#, {"latitude": 1, "longitude": 1, "altitude": 1})

    for data in cursor:
        latitude.append(data['latitude'])
        longitude.append(data['longitude'])
        latitudeStdDev.append(data['latitudeStdDev'])
        longitudeStdDev.append(data['longitudeStdDev'])
        heightStdDev.append(data['heightStdDev'])
        galileoBeidouUsedMask.append(data['galileoBeidouUsedMask'])
        solutionAge.append(data['solutionAge'])
        extendedSolutionStatus.append(data['extendedSolutionStatus'])
        solStatus.append(data['solStatus'])
        heightMsl.append(data['heightMsl'])
        baseStationId.append(data['baseStationId'])
        numSatsTracked.append(data['numSatsTracked'])
        numSatsInSolution.append(data['numSatsInSolution'])
        solType.append(data['solType'])
        datumId.append(data['datumId'])
        numSatsL1.append(data['numSatsL1'])
        differentialAge.append(data['differentialAge'])
        timestamp.append(data['header']['timestampSec'])

to_bestpos_csv = {
    'latitude': latitude,
    'longitude': longitude,
    'latitudeStdDev': latitudeStdDev,
    'longitudeStdDev': longitudeStdDev,
    'heightStdDev': heightStdDev,
    'galileoBeidouUsedMask': galileoBeidouUsedMask,
    'solutionAge': solutionAge,
    'extendedSolutionStatus': extendedSolutionStatus,
    'solStatus': solStatus,
    'heightMsl': heightMsl,
    'baseStationId': baseStationId,
    'numSatsTracked': numSatsTracked,
    'numSatsInSolution': numSatsInSolution,
    'solType': solType,
    'datumId': datumId,
    'numSatsL1': numSatsL1,
    'differentialAge': differentialAge,
    'timestamp': timestamp
}

# Export data to csv
bestpos_csv_file = db_name + '_best_pose_' + str(epoch_time) + '.csv'

with open(bestpos_csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=to_bestpos_csv.keys())  # Use data.keys() to specify column names
    writer.writeheader()
    for idx in range(len(latitude)):
        row_data = {key: value[idx] for key, value in to_bestpos_csv.items()}
        writer.writerow(row_data)

print(f'Data has been exported to {bestpos_csv_file}')


################################
######## CORRECTED IMU #########
################################

query = {f'topic': '/apollo/sensor/gnss/corrected_imu'}
print('Now exporting {query}')

linearAccelerationX = []
linearAccelerationY = []
linearAccelerationZ = []
angularVelocityX = []
angularVelocityY = []
angularVelocityZ = []
eulerAnglesX = []
eulerAnglesY = []
eulerAnglesZ = []
timestamp = []

if mycol.find_one(query) is not None:
    cursor = mycol.find(query)#, {"latitude": 1, "longitude": 1, "altitude": 1})

    for data in cursor:
        linearAccelerationX.append(data['imu']['linearAcceleration']['x'])
        linearAccelerationY.append(data['imu']['linearAcceleration']['y'])
        linearAccelerationZ.append(data['imu']['linearAcceleration']['z'])
        angularVelocityX.append(data['imu']['angularVelocity']['x'])
        angularVelocityY.append(data['imu']['angularVelocity']['y'])
        angularVelocityZ.append(data['imu']['angularVelocity']['z'])
        eulerAnglesX.append(data['imu']['eulerAngles']['x'])
        eulerAnglesY.append(data['imu']['eulerAngles']['y'])
        eulerAnglesZ.append(data['imu']['eulerAngles']['z'])
        timestamp.append(data['header']['timestampSec'])
        

# print(len(latitude))

to_corrected_imu_csv = {
    'linearAccelerationX':linearAccelerationX,
    'linearAccelerationY':linearAccelerationY,
    'linearAccelerationZ':linearAccelerationZ,
    'angularVelocityX':angularVelocityX,
    'angularVelocityY':angularVelocityY,
    'angularVelocityZ':angularVelocityZ,
    'eulerAnglesX':eulerAnglesX,
    'eulerAnglesY':eulerAnglesY,
    'eulerAnglesZ':eulerAnglesZ,
    'timestamp':timestamp
}

# Export data to csv
corrected_imu_csv_file = db_name + '_corrected_imu_' + str(epoch_time) + '.csv'

with open(corrected_imu_csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=to_corrected_imu_csv.keys())  # Use data.keys() to specify column names
    writer.writeheader()
    for idx in range(len(linearAccelerationX)):
        row_data = {key: value[idx] for key, value in to_corrected_imu_csv.items()}
        writer.writerow(row_data)

print(f'Data has been exported to {corrected_imu_csv_file}')



################################
########## INS STATUS ##########
################################


query = {f'topic': '/apollo/sensor/gnss/ins_stat'}
print('Now exporting {query}')

insStatus = []
posType = []
timestamp = []

if mycol.find_one(query) is not None:
    cursor = mycol.find(query)
    
    for data in cursor:
        insStatus.append(data['insStatus'])
        posType.append(data['posType'])
        timestamp.append(data['header']['timestampSec'])


to_ins_status_csv = {
    'insStatus': insStatus,
    'posType': posType,
    'timestamp':timestamp
}

# Export data to csv
ins_status_csv_file = db_name + '_ins_status_' + str(epoch_time) + '.csv'

with open(ins_status_csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=to_ins_status_csv.keys())  # Use data.keys() to specify column names
    writer.writeheader()
    for idx in range(len(insStatus)):
        row_data = {key: value[idx] for key, value in to_ins_status_csv.items()}
        writer.writerow(row_data)

print(f'Data has been exported to {ins_status_csv_file}')



################################
########## ODEMTETRY ###########
################################

query = {f'topic': '/apollo/sensor/gnss/odometry'}

print('Now exporting {query}')

positionX = []
positionY = []
positionZ = []
orientationQX = []
orientationQY = []
orientationQZ = []
orientationQW = []
linearVelocityX = []
linearVelocityY = []
linearVelocityZ = []
timestamp = []

if mycol.find_one(query) is not None:
    cursor = mycol.find(query)
    
    for data in cursor:
        positionX.append(data['localization']['linearVelocity']['x'])
        positionY.append(data['localization']['linearVelocity']['y'])
        positionZ.append(data['localization']['linearVelocity']['z'])
        orientationQX.append(data['localization']['orientation']['qx'])
        orientationQY.append(data['localization']['orientation']['qy'])
        orientationQZ.append(data['localization']['orientation']['qz'])
        orientationQW.append(data['localization']['orientation']['qw'])
        linearVelocityX.append(data['localization']['linearVelocity']['x'])
        linearVelocityY.append(data['localization']['linearVelocity']['y'])
        linearVelocityZ.append(data['localization']['linearVelocity']['z'])
        timestamp.append(data['header']['timestampSec'])

to_odometry_csv = {
    'positionX': positionX,
    'positionY': positionY,
    'positionZ': positionZ,
    'orientationQX': orientationQX,
    'orientationQY': orientationQY,
    'orientationQZ': orientationQZ,
    'orientationQW': orientationQW,
    'linearVelocityX': linearVelocityX,
    'linearVelocityY': linearVelocityY,
    'linearVelocityZ': linearVelocityZ,
    'timestamp':timestamp
}


# Export data to csv
odometry_csv_file = db_name + '_odometry_' + str(epoch_time) + '.csv'

with open(odometry_csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=to_odometry_csv.keys())  # Use data.keys() to specify column names
    writer.writeheader()
    for idx in range(len(positionX)):
        row_data = {key: value[idx] for key, value in to_odometry_csv.items()}
        writer.writerow(row_data)

print(f'Data has been exported to {odometry_csv_file}')

