def validate_bool(value):
    if str(value) == "True":
        return "True"
    else:
        return "False"

def validate_real_bool(value):
    if str(value) == "True":
        return True
    elif str(value) == "False":
        return False
    else:
        return "ERROR"