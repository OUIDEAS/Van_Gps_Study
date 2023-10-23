# MONGODB Data Pull

Use datainsert.py from the ADS-Apollo something or other repo with the following channelList configuration:

```"channelList":{
        "deny": [
            "/apollo/sensor/gnss/stream_status",
            "/apollo/drive_event",
            "/apollo/control/pad",
            "/apollo/sensor/camera/front_25mm/image/compressed",
            "/apollo/hmi/status",
            "/apollo/control",
            "/apollo/sensor/gnss/rtcm_data",
            "/apollo/planning",
            "/apollo/canbus/chassis_detail",
            "/apollo/sensor/camera/front_25mm/image",
            "/apollo/sensor/velodyne32/PointCloud2",
            "/apollo/monitor/system_status",
            "/apollo/routing_response_history",
            "/apollo/localization/msf_status",
            "/apollo/prediction/perception_obstacles",
            "/apollo/sensor/camera/front_6mm/image/compressed",
            "/apollo/routing_response",
            "/apollo/perception/obstacles",
            "/apollo/canbus/chassis",
            "/apollo/navigation",
            "/apollo/sensor/velodyne32/VelodyneScan",
            "/apollo/perception/traffic_light",
            "/tf_static",
            "/tf",
            "/apollo/prediction",
            "/apollo/sensor/camera/front_6mm/image",
            "/apollo/monitor",
            "/apollo/routing_request"
        ]
    }```

Use pull_localization_data.py to pull the data from the database and export to csv.
