# min(arg1, arg2, arg3) : =====================================================|
>>> always_10 = min(5 + 10, 10)
>>> print always_10
10


# hasattr() & getattr()_: =====================================================|
class Attrium:
    pass

attributeless = Attrium()

>>> hasattr(attributeless, "fake_attribute")
# returns False

>>> getattr(attributeless, "other_fake_attribute", "No such attribute.")
# returns 800, the default value
