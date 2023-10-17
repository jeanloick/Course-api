from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

# Documentation
from documentation.description import api_description
from documentation.tags import tags_metadata

import routers.router_recipes

app= FastAPI( 
    title="Course API",
    description=api_description,
    openapi_tags=tags_metadata # tagsmetadata definit au dessus
    )

app.include_router(routers.router_recipes.router)

