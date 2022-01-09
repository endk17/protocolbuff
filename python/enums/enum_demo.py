
import enum_example_pb2 as enum_example_pb2

enum_message = enum_example_pb2.EnumMessage()
enum_message.id = 234
enum_message.day_of_the_week = enum_example_pb2.THURSDAY

print(enum_message)

with open("enums.bin", "wb") as f:
    f.write(enum_message.SerializeToString())
    print("write to file")

with open("enums.bin", "rb") as f:
    enum_msg_read = enum_example_pb2.EnumMessage().FromString(f.read())
    print("read file")

print(enum_msg_read)