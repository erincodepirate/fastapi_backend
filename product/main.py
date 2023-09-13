from fastapi import FastAPI, status, Response, HTTPException

import models
from database import engine
from routers import product, seller

app = FastAPI(
    title = "Products API",
    description = "Get details about all the products",
    terms_of_service = "http://www.duckduckgo.com",
    contact = {
        "Developer name":"Sonic the Hedgehog",
        "website":"http://www.duckduckgo.com",
        "email":"demo@gmail.com"
    },
    license_info={
        "name":"blah",
        "url":"http://www.duckduckgo.com"
    },
    #docs_url="/documentation", redoc_url=None
)

app.include_router(product.router)
app.include_router(seller.router)

models.Base.metadata.create_all(engine)

