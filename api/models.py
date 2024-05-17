from sqlalchemy import Boolean, CheckConstraint, Float, Integer, String, ForeignKey, Date, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

from api.database import Base


class User(Base):
    """Пользователь."""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    bookings: Mapped[List["Booking"]] = relationship(
        "Booking", back_populates="user")
    reviews: Mapped[List["Review"]] = relationship(
        "Review", back_populates="user")
    sent_messages: Mapped[List["Message"]] = relationship(
        "Message", foreign_keys="[Message.sender_id]", back_populates="sender")
    received_messages: Mapped[List["Message"]] = relationship(
        "Message", foreign_keys="[Message.recipient_id]", back_populates="recipient")
    payments: Mapped[List["Payment"]] = relationship(
        "Payment", back_populates="user")


class Property(Base):
    """Объект."""
    __tablename__ = 'properties'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    price_per_night: Mapped[int] = mapped_column(Integer, nullable=False)

    images: Mapped[List["Image"]] = relationship(
        "Image", back_populates="property")
    bookings: Mapped[List["Booking"]] = relationship(
        "Booking", back_populates="property")
    reviews: Mapped[List["Review"]] = relationship(
        "Review", back_populates="property")
    calendar_blocks: Mapped[List["CalendarBlock"]] = relationship(
        "CalendarBlock", back_populates="property")
    property_amenities: Mapped[List["PropertyAmenity"]] = relationship(
        "PropertyAmenity", back_populates="property")


class Image(Base):
    """Изображение."""
    __tablename__ = 'images'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    file_path: Mapped[str] = mapped_column(String, nullable=False)

    property_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('properties.id'))

    property: Mapped["Property"] = relationship(
        "Property", back_populates="images")


class Booking(Base):
    """Бронирование."""
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    check_in_date: Mapped[Date] = mapped_column(Date, nullable=False)
    check_out_date: Mapped[Date] = mapped_column(Date, nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    property_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('properties.id'))

    user: Mapped["User"] = relationship("User", back_populates="bookings")
    property: Mapped["Property"] = relationship(
        "Property", back_populates="bookings")
    payments: Mapped[List["Payment"]] = relationship(
        "Payment", back_populates="booking")
    cancellations: Mapped[List["Cancellation"]] = relationship(
        "Cancellation", back_populates="booking")


class Review(Base):
    """Отзыв."""
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[Optional[str]] = mapped_column(String)
    date_posted: Mapped[Date] = mapped_column(
        Date, nullable=False, server_default=func.current_date())

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    property_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('properties.id'))

    user: Mapped["User"] = relationship("User", back_populates="reviews")
    property: Mapped["Property"] = relationship(
        "Property", back_populates="reviews")

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 10', name='rating_check'),
    )


class Message(Base):
    """Сообщение."""
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String)
    date_sent: Mapped[Date] = mapped_column(Date, nullable=False)

    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    recipient_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))

    sender: Mapped["User"] = relationship(
        "User", foreign_keys=[sender_id], back_populates="sent_messages")
    recipient: Mapped["User"] = relationship(
        "User", foreign_keys=[recipient_id], back_populates="received_messages")


class Amenity(Base):
    """Удобства."""
    __tablename__ = 'amenities'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    property_amenities: Mapped[List["PropertyAmenity"]] = relationship(
        "PropertyAmenity", back_populates="amenity")


class PropertyAmenity(Base):
    "Объект-Удобства."
    __tablename__ = 'property_amenities'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    property_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('properties.id'))
    amenity_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('amenities.id'))

    property: Mapped["Property"] = relationship(
        "Property", back_populates="property_amenities")
    amenity: Mapped["Amenity"] = relationship(
        "Amenity", back_populates="property_amenities")


class CalendarBlock(Base):
    """Блокировка календаря."""
    __tablename__ = 'calendar_blocks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_date: Mapped[Date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Date] = mapped_column(Date, nullable=False)

    property_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('properties.id'))

    property: Mapped["Property"] = relationship(
        "Property", back_populates="calendar_blocks")


class Payment(Base):
    """Оплата."""
    __tablename__ = 'payments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    payment_date: Mapped[Date] = mapped_column(Date, nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    booking_id: Mapped[int] = mapped_column(Integer, ForeignKey('bookings.id'))

    user: Mapped["User"] = relationship("User", back_populates="payments")
    booking: Mapped["Booking"] = relationship(
        "Booking", back_populates="payments")


class Cancellation(Base):
    "Отмена."
    __tablename__ = 'cancellations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    reason: Mapped[Optional[str]] = mapped_column(String)
    cancelled_by_user: Mapped[bool] = mapped_column(Boolean, nullable=False)

    booking_id: Mapped[int] = mapped_column(Integer, ForeignKey('bookings.id'))

    booking: Mapped["Booking"] = relationship(
        "Booking", back_populates="cancellations")
