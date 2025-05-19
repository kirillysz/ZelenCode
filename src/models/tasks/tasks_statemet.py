from enum import Enum

class Statement(str, Enum):
    text_only = "text_only"
    markdown = "markdown"