class PetEndpoints:
    ADD_PET = "/pet"
    UPDATE_PET = "/pet"
    GET_PET_BY_ID = "/pet/{pet_id}"
    DELETE_PET = "/pet/{pet_id}"
    FIND_BY_STATUS = "/pet/findByStatus"


class UserEndpoints:
    CREATE_USER = "/user"
    GET_USER = "/user/{username}"
    UPDATE_USER = "/user/{username}"
    DELETE_USER = "/user/{username}"
    LOGIN = "/user/login"
    LOGOUT = "/user/logout"
