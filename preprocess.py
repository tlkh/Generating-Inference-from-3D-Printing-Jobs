import numpy as np

def generate_purpose_vector(raw_data):
    purpose = [0,0,0,0,0,0,0]
    purpose[0]=raw_data.count("Test Fit (tolerances)")
    purpose[1]=raw_data.count("Test Strength")
    purpose[2]=raw_data.count("Test Ergonomics")
    purpose[3]=raw_data.count("Wearout")
    purpose[4]=raw_data.count("Integration")
    purpose[5]=raw_data.count("Ornamental / Design" or "Ornamental / Gift")
    purpose[6]=raw_data.count("Others:")
    return purpose

def generate_filament_use(raw_data):
    try:
        filament = float(raw_data)
    except:
        filament = raw_data
        words_to_remove = [" ", "m", "meters", "meter", "metre", "metres"]
        for word in words_to_remove:
            filament.replace(word,"")
        filament = float(raw_data)
    return filament

def generate_time_taken(raw_data):
    try:
        time = float(raw_data)
    except:
        time = str(raw_data)
        words_to_remove = [" ","hour","minute","min","hr","h","s","m"]
        for word in words_to_remove:
            time = time.replace(word,"")
        time = float(time)
    return time

def generate_feedback(raw_data):
    feedback = 0 #uncertain
    if (raw_data.count("fail" or "Fail") > 0):
        feedback = -1 #fail
    elif (raw_data.count("good" or "well") > 0):
        feedback = 1 #success
    return feedback

def obtain_data_matrix(data):
    matrix = np.matrix([0,(0,0,0,0,0,0,0),0,0,0,0], dtype=object)

    for raw in data:
        stu_id = int(raw[2]) - 1000000
        if stu_id > 9999:
            stu_id = int(str(stu_id)[-4:])
        elif stu_id < 0:
            stu_id +=1000000
            stu_id = int(str(stu_id)[-4:])

        purpose = generate_purpose_vector(raw[4])
        filament = generate_filament_use(raw[6])
        time = generate_time_taken(raw[7])
        satisfaction = int(raw[8])
        feedback = generate_feedback(raw[9])

        point = np.array([stu_id, purpose, filament, time, satisfaction, feedback], dtype=object)
        matrix = np.vstack([matrix, point])

    matrix = np.delete(matrix, (0), axis=0)
    return matrix
