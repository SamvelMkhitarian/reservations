from fastapi import FastAPI
import uvicorn

from api.users.routers import router as users_router
from api.reviews.routers import router as reviews_router
from api.properties.routers import router as users_properties
from api.payments.routers import router as users_payments
from api.messages.routers import router as users_messages
from api.images.routers import router as users_images
from api.cancellations.routers import router as users_cancellations
from api.calendars_blocks.routers import router as users_calendars_blocks
from api.bookings.routers import router as users_bookings
from api.amenities.routers import router as users_amenities


app = FastAPI()


app.include_router(users_router, prefix="/api", tags=["users"])
app.include_router(reviews_router, prefix="/api", tags=["reviews"])
app.include_router(users_properties, prefix="/api", tags=["properties"])
app.include_router(users_payments, prefix="/api", tags=["payments"])
app.include_router(users_messages, prefix="/api", tags=["messages"])
app.include_router(users_images, prefix="/api", tags=["images"])
app.include_router(users_cancellations, prefix="/api", tags=["cancellations"])
app.include_router(users_calendars_blocks, prefix="/api",
                   tags=["calendars_blocks"])
app.include_router(users_bookings, prefix="/api", tags=["bookings"])
app.include_router(users_amenities, prefix="/api", tags=["amenities"])


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
