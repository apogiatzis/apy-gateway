from functools import wraps, partial

# WIP

class ApiFunctions():
    def __init__(self):
        self._functions = {}

    @property
    def functions(self):
        return self._functions

    def _get_or_add_function(self, func):
        """
        Returns function spec of given func and adds it to the function spec dictionary
        if it is not already there.
        """
        func_spec = self._functions.get(func.__hash__(), None)
        if func_spec == None:
            func_spec = {
                "Type": "AWS::Lambda::Function",
                "Properties": {
                    "FunctionName": func.__name__,
                    "Handler": func.__code__.co_filename[:-3].replace("/",".") + "." + func.__name__
                }
            }
            self._functions[func.__hash__()] = func_spec
        return func_spec

    def custom(self, key, value):
        """
        Decorator that updates a specific property of the decorated
        function in the function spec
        """
        def wrap(orig_func):
            func_spec = self._get_or_add_function(orig_func)
            func_spec["Properties"].update({key: value})
            print(self.functions)
            @wraps(orig_func)
            def wrapper(event, context):
                return orig_func(event, context)
            # Make sure hash remains the same as the original function 
            # such that function dictionary is updated correctly
            wrapper.__hash__ = orig_func.__hash__
            return wrapper
        return wrap

    def name(self, value):
        return self.custom("FunctionName", value)

    def description(self, value):
        return self.custom("Description", value)
    
    def memory(self, value):
        return self.custom("MemorySize", value)

    def role(self, value):
        return self.custom("Role", value)
    
    def runtime(self, value):
        return self.custom("Runtime", value)
    
    def timeout(self, value):
        return self.custom("Timeout", value)

class ApiMethods():
    def __init__(self):
        self._methods = {}

    @property
    def methods(self):
        return self._methods

class ApiResources():
    def __init(self)::
        self._resources = {}

    @property
    def resources(self):
        return self._resources


class ApiTemplate():

    def __init__(self):
        self.function = ApiFunctions()
        self.methods = ApiMethods()

    
        