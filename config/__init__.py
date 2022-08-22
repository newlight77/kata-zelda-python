# import os
from dotenv import dotenv_values


class defDictToObject(object):

    def __init__(self, myDict):
        for key, value in myDict.items():
            print(f"{key} : {value}")
            if type(value) == dict:
                setattr(self, key, defDictToObject(value))
            else:
                setattr(self, key, value)


env = defDictToObject({
    **dotenv_values("config/default.env"),  # load shared development variables
    # **os.environ,  # override loaded values with environment variables
})
