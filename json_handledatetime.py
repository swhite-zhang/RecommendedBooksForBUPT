import json
import datetime
import init


class obj_to_json(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, init.Book):
            return obj.to_str()
        elif isinstance(obj, init.Reader):
            return obj.to_str()
        else:
            return json.JSONEncoder.default(self, obj)


class json_to_obj(json.JSONDecoder):
    def default(obj):
        if isinstance(obj, obj.strftime('%Y-%m-%d %H:%M:%S')):
            return datetime.datetime
        elif isinstance(obj, obj.strftime("%Y-%m-%d")):
            return datetime.date
        else:
            return obj
