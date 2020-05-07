import hashlib


def get_hash_password(password):
    '''

    :param password: the password to hash
    :return: a string which is the md5-hash of the password
    '''
    return hashlib.md5(password.encode()).hexdigest()
