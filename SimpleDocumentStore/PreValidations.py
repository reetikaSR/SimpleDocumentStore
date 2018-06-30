modes = ['r', 'w', 'a', 'r+']


def validate_file_name(file_name):
    if file_name > '':
        return True
    return False


def validate_bucket_name(bucket_name):
    if bucket_name > '':
        return True
    return False


def validate_location(location):
    if location > '':
        return True
    return False


def validate_mode(mode):
    if mode in modes:
        return True
    return False
