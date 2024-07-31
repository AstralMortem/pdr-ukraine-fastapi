from enum import Enum


DriverLicense = Enum(
    "DriverLicense",
    ["A", "A1", "BE", "B", "B1", "CE", "C", "C1", "C1E", "DE", "D", "D1", "D1E", "T"],
)

Language = Enum("Language", ["uk", "ru", "en"])
