import os
import json
import builtins
from datetime import datetime


class Var:
    __slots__ = (
        "title",
        "required",
        "type",
        "default",
        "description",
        "verbose",
        "added_at",
    )

    def __init__(self, *args, **kwargs):
        obj = self.__get_obj(*args, **kwargs)

        self.title = self.__get_title(obj)
        self.required = self.__get_required(obj)
        self.type = self.__get_type(obj)
        self.default = self.__get_default(obj)
        self.description = self.__get_description(obj)
        self.verbose = self.__get_verbose(obj)
        self.added_at = self.__get_milestone(obj)

        self.value
        self.__log()

    def __get_obj(self, *args, **kwargs):
        if args:
            if not kwargs:
                if len(args) == 1:
                    try:
                        obj = json.loads(args[0])
                    except TypeError:
                        obj = args[0]
                else:
                    raise ValueError(
                        "Only one abject as a positional argument " "can be accepted"
                    )
            else:
                raise ValueError(
                    "Either positional or keyword arguments can be " "passed, not both"
                )
        elif kwargs:
            obj = kwargs
        return obj

    def __get_title(self, obj):
        title = obj.get("title")
        if not title:
            raise ValueError("Environment variables have to have a title")
        return title

    def __get_required(self, obj):
        return obj.get("required", False)

    def __get_type(self, obj):
        return obj.get("type", "str")

    def __get_default(self, obj):
        default = obj.get("default")
        if default is not None:
            return self.__cast_type(default)
        return default

    def __bool_cast(self, value):
        if value in ["0", "false", "False", "null", "None", ""]:
            return False
        return bool(value)

    def __cast_type(self, value):
        try:
            type_ = getattr(builtins, self.type)
            if type_ == bool:
                return self.__bool_cast(value)
            return type_(value)
        except (ValueError, TypeError):
            raise ValueError(
                "Can't cast ENV: %s = %s (type: %s) to type %s"
                % (self.title, value, type(value), self.type)
            )

    def __get_description(self, obj):
        return obj.get("description")

    def __get_verbose(self, obj):
        return obj.get("verbose", True)

    def __get_milestone(self, obj):
        return obj.get("added_at", datetime.now().timestamp())

    def __log(self):
        if self.verbose and self.description is None:
            print(
                "[%s] ENV WARNING: %s is not described! "
                'If you wish to mute this warning - set "verbose" property to False '
                "or give the variable a description."
                % (datetime.now().isoformat().replace("T", " "), self.title)
            )

    def to_dict(self):
        obj = {}
        for k in self.__slots__:
            obj[k] = getattr(self, k)
        return obj

    def get(self, default=None):
        value = os.environ.get(self.title)
        if value is not None:
            return self.__cast_type(value)
        if default is not None:
            return self.__cast_type(default)
        if self.default is not None:
            return self.__cast_type(self.default)
        if self.required:
            raise ValueError(
                "Environment variable %s is required " "to be passed a value",
                self.title,
            )
        return None

    @property
    def value(self):
        return self.get()

    @value.setter
    def value(self, value):
        os.environ[self.title] = str(value)
