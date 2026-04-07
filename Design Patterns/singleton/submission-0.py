class Singleton:
    _instance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def getValue(self) -> str:
        return getattr(self,"value",None)

    def setValue(self, value: str):
        self.value = value
        

s = Singleton()
s.getValue()
s.setValue("a value string")
s.getValue()

s2 = Singleton()

s2.getValue()