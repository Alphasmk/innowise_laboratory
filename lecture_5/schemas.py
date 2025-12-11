"""Pydantic schemas for API validation."""
from pydantic import BaseModel


class BookCreate(BaseModel):
    """Schema for creating a new book."""
    title: str
    author: str
    year: int | None = None


class BookUpdate(BaseModel):
    """Schema for updating an existing book."""
    title: str | None = None
    author: str | None = None
    year: int | None = None


class BookResponse(BaseModel):
    """Schema for book API responses."""
    id: int
    title: str
    author: str
    year: int | None
    
    model_config = {"from_attributes": True}