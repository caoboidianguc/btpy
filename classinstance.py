class MyClass:
    def method(self):
        return 'instance method called'

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


me = MyClass()
metho = me.method()
print(metho)

