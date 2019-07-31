from model import user_register
from repo.user_repo import UserRepo
from service.service import Service
from utils import generate_uuid, timestamp, password_hash, password_verify
import traceback


class AccountService(Service):

    def signin(self, email, password):
        try:
            use_repo = UserRepo()
            user_detail = use_repo.signin(email)
            if user_detail is None:
                return None
            else:
                if password_verify(password, user_detail["password"]):
                    return user_detail["user"],user_detail["role"]
                else:
                    return None
        except Exception:
            traceback.print_exc()
            return None

    def signup(self, teacher):
        user = user_register.user
        password = user_register.password
        user.user_id = generate_uuid()
        user.created_at = timestamp()
        try:
            use_repo = UserRepo()
            if use_repo.save(user, password_hash(password)):
                return user
        except Exception:
            traceback.print_exc()
            return None