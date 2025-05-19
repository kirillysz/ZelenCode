from enum import Enum

class UserRole(str, Enum):
    participant = "participant"
    moderator = "moderator"
    admin = "admin"