
import complex_pb2 as complex_pb2

complex_message = complex_pb2.ComplexMessage()

## Incorrect
# one_dummy_message = complex_pb2.DummyMessage()
# one_dummy_message.id = 234
# one_dummy_message.name = "Dummy 101"
# one_dummy_message.one_dummy = one_dummy_message

complex_message.one_dummy.id = 234
complex_message.one_dummy.name = "Dummy 101"

first_multiple = complex_message.multiple_dummy.add()
first_multiple.id = 432
first_multiple.name =  "First array element"

# Preferred method
complex_message.multiple_dummy.add(
    id=678,
    name="Second array element"
)

"""
- When using an extend method and adding an array this is effectively a copy
- Cannot overwrite once declared
i.e. third_dummy_message.id = 777

This does not change the originally declared item
"""
third_dummy_message = complex_pb2.DummyMessage()
third_dummy_message.id = 767
third_dummy_message.name = "Last element"
complex_message.multiple_dummy.extend([third_dummy_message])

third_dummy_message.id = 777

print(third_dummy_message)
print(complex_message)