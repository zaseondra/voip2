from pydantic import BaseModel

class ManagedCall(BaseModel):
    from_ext: int | str
    to_ext: int | str
