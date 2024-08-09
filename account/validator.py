def validate_phone(value: str):
    if not value.isdigit():
        raise ValueError("Phone number must be all digits")
    if len(value) != 10:
        raise ValueError("Phone number must be 10 digits long")


def validate_pincode(value: str):
    if not value.isdigit():
        raise ValueError("Pincode must be all digits")
    if len(value) != 6:
        raise ValueError("Pincode must be 6 digits long")
