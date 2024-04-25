"""
Purpose
-------
review the python rules for determining if something is a subclass or instance

1) to check if a variable is an instance of a certain class
a) type(instance) is class # checking the type of a variable (could throw TypeError)
b) isinstance(instance,class)

Key distinction: isinstance will return true if the object is an instance of a subclass (whereas type won't)

issubclass(cls1,cls2) can only be used with class objects
"""