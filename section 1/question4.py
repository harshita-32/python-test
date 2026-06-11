class UnderAgeError(Exception):
    pass
class InvalidAgeError(Exception):
    pass 
class AgeVerification:
    def set_age(self, age):
        try:
            if age < 0:
                raise ValueError("Age cannot be negative")
            elif age < 18:
                raise UnderAgeError("person is under age")

            elif age > 100:
                raise InvalidAgeError("invalid age entered")
            else:
                print("valid age!")
        except ValueError as e:
           print("ValueError:",e)
        except UnderAgeError as e:
            print("UnderAgeError:",e)
        except InvalidAgeError as e:
            print("InvalidAgeError:",e)
        finally:
            print("Age verification completed.")
obj = AgeVerification()
obj.set_age(15)                       