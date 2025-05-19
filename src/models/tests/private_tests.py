from pydantic import BaseModel

class PrivateTest(BaseModel):
    input: str
    expected_output: str