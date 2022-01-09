import addressbook_pb2 as addressbook_pb2

person_message = addressbook_pb2.Person()
# person_message.multiple_dummy.add(
#     id = 1234,
#     name = "John Doe",
#     email = "jdoe@example.com"
# )
person_message.id = 1234
person_message.name = "John Doe"
person_message.email = "jdoe@example.com"

phone = person_message.phones.add()
phone.number = "555-4566"
phone.type = addressbook_pb2.Person.HOME

print(person_message)