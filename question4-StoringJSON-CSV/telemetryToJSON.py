# Unit 5 question 4 part 1A

# save telemetry data to json

import json

telemetry = [
    {
        "timestamp": "2024-03-30T07:58:27.999065",
        "temperature": 24.15,
        "pressure": 1082.28,
        "velocity": 2157.35,
        "altitude": 579.64,
        "power_level": 68.97,
        "orientation": {
            "roll": 63.34,
            "pitch": -174.83,
            "yaw": 220.57
        }
    },
    {
        "timestamp": "2024-03-30T07:47:56.999065",
        "temperature": -35.17,
        "pressure": 892.84,
        "velocity": 9366.16,
        "altitude": 821.66,
        "power_level": 25.56,
        "orientation": {
            "roll": -48.75,
            "pitch": -167.37,
            "yaw": 181.04
        }
    },
    {
        "timestamp": "2024-03-30T07:53:45.999065",
        "temperature": -5.28,
        "pressure": 1028.31,
        "velocity": 6538.57,
        "altitude": 729.16,
        "power_level": 88.36,
        "orientation": {
            "roll": 160.25,
            "pitch": 101.33,
            "yaw": 16.67
        }
    }
]

# write
with open('question4-StoringJSON-CSV/telemetry.json', 'w') as file:
    json.dump(telemetry, file)

# read
with open('question4-StoringJSON-CSV/telemetry.json', 'r') as file:
    storedTelemetry = json.load(file)

# output
aircraftCount = 0
print("\n- - - TELEMETRY - - - \n")
for row in storedTelemetry:
    aircraftCount+=1
    print('TELEMETRY FOR CRAFT #',aircraftCount)
    print("timestamp:",row['timestamp'])
    print("temperature:",row['temperature'])
    print("pressure:",row['pressure'])
    print("velocity:",row['velocity'])
    print("altitude:",row['altitude'])
    print("power_level:",row['power_level'])
    print("orientation:")
    print("\t |___ roll:",row['orientation']['roll'])
    print("\t |___ pitch:",row['orientation']['pitch'])
    print("\t |___ yaw:",row['orientation']['yaw'])
