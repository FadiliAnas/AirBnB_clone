import json
from models.base_model import BaseModel


class  FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return self.__objects
    def new(self, obj):
        keyequal = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[keyequal] = obj
    def save(self):
        json_dict = {}
        for k,v in FileStorage.__objects.items():
            json_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as filejson: 
            json.dump(json_dict, filejson, indent=4)
    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as filejsonload:
                dict_load = json.load(filejsonload)
                for k,v in dict_load.items():
                    FileStorage.__objects[k] = eval(v["__class__"])(**v)
        except FileNotFoundError :
            return