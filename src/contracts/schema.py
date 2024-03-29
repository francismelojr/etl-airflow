from pydantic import BaseModel


class WeatherSchema(BaseModel):
    name: str
    country: str
    temp_c: float
    temp_f: float
