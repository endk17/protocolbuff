
import enum_example_pb2 as enum_example_pb2

enum_message = enum_example_pb2.EnumMessage()
enum_message.id = 234
enum_message.day_of_the_week = enum_example_pb2.THURSDAY

print(enum_message)