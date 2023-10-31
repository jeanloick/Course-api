from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

# Documentation
from documentation.description import api_description
from documentation.tags import tags_metadata

import routers.router_recipes
import routers.router_chiefs
import routers.router_auth
import routers.router_stripe
from routers.router_auth import get_current_user

app= FastAPI( 
    title="MasterChief Recipes !",
    description=api_description,
    openapi_tags=tags_metadata # tagsmetadata definit au dessus
    )

app.include_router(routers.router_recipes.router)
app.include_router(routers.router_chiefs.router)
app.include_router(routers.router_auth.router)
#app.include_router(routers.router_stripe.router)

