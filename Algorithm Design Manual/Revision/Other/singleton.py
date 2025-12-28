class Config:

    # Stores single shared instance
    _instance = None # class level storage

    # __new__ controls object creation (runs before __init__)
    def __new__(cls):
        # Only creates object once
        if cls._instance is None:
            # Actually allocates mem. for obj.
            cls._instance = super().__new__(cls)
            cls._instance.debug = False # init once.
        
        # Always returns same obj.
        return cls._instance
    
c1 = Config()
c2 = Config()

print (c1 is c2) # True
c1.debug = True
print(c2.debug) # True (same obj)