import addressbook_pb2
import sys

# Iterates though all people in the AddressBook and prints info about them.
def ListPeople(address_book_msg):
  for person in address_book_msg.people:
    print("Person ID:", person.id)
    print("Name:", person.name)
    if person.HasField('email'):
      print("E-mail address:", person.email)

    for phone_number in person.phones:
      if phone_number.type == addressbook_pb2.Person.PhoneType.MOBILE:
        print("Mobile phone #: ")
      elif phone_number.type == addressbook_pb2.Person.PhoneType.HOME:
        print("Home phone #: ")
      elif phone_number.type == addressbook_pb2.Person.PhoneType.WORK:
        print("Work phone #: ")
      print(phone_number.number)

# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.

address_book = addressbook_pb2.AddressBook()

# Read the existing address book.
f = open("addressbook.bin", "rb")
address_book_msg = addressbook_pb2.AddressBook().FromString(f.read())
f.close()

ListPeople(address_book_msg)