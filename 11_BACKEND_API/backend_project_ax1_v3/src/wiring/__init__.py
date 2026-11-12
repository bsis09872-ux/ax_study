from fastapi import FastAPI
from wiring.user import wire_user_dependencies
from wiring.auth import wire_auth_dependeices

# FastAPI Dependency Overrides 와이어링
def wire_dependencies(app: FastAPI) -> None:
    wire_auth_dependeices(app)
    wire_user_dependencies(app)