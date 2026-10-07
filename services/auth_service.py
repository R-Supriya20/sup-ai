from datetime import datetime, timedelta, timezone

from argon2 import PasswordHasher
from jose import jwt
from bson import ObjectId

from config.settings import settings
from repositories.user_repository import UserRepository


password_hasher = PasswordHasher()

user_repository = UserRepository()


class AuthService:


    def register_user(
        self,
        email: str,
        password: str
    ):

        existing_user = user_repository.find_by_email(
            email
        )

        if existing_user:

            raise ValueError(
                "User already exists"
            )


        hashed_password = password_hasher.hash(
            password
        )


        user_data = {
            "email": email,
            "password": hashed_password,
            "role": "user",
            "created_at": datetime.now(timezone.utc)
        }


        user_id = user_repository.create_user(
            user_data
        )


        return {
            "id": str(user_id),
            "email": email,
            "role": "user"
        }


    def authenticate_user(
        self,
        email: str,
        password: str
    ):

        user = user_repository.find_by_email(
            email
        )

        if not user:

            return None


        try:

            password_hasher.verify(
                user["password"],
                password
            )

        except Exception:

            return None


        return user


    def create_access_token(
        self,
        user_id: str
    ):

        expire = (
            datetime.now(timezone.utc)
            + timedelta(
                minutes=settings.access_token_expire_minutes
            )
        )


        payload = {
            "sub": user_id,
            "exp": expire
        }


        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm
        )


        return token