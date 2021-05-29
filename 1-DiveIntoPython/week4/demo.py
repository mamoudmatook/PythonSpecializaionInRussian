import tempfile
a = tempfile.TemporaryFile()
print(type(a))
print(a.name)