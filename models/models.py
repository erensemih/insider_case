from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional

class RequestModel(BaseModel):
    """Model for incoming requests. Expects data as a dictionary."""
    data: Dict[str, Any]

class ResponseModel(BaseModel):
    """Model for outgoing responses. Includes success status, optional recommendations, and an optional error message."""
    success: bool
    recommendations: List[str] = Field(default_factory=list, description="List of recommendations, if any.")
    error: Optional[str] = Field(None, description="Error message, if any.")