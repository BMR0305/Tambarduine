def validate_bool(value):
    if str(value) == "true":
        return "true"
    else:
        return "false"

def validate_real_bool(value):
    if str(value) == "true":
        return True
    elif str(value) == "false":
        return False
    else:
        return "ERROR"