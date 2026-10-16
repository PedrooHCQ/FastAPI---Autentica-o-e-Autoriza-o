from pydantic import BaseModel, HttpUrl, ConfigDict

from typing import Optional

class ArtigoSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int] = None

class ArtigoSchemaUp(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    url_fonte: Optional[HttpUrl]
    usuario_id: Optional[int] = None
