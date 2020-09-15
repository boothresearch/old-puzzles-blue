from re import sub

class Phone(object):
    """
    This program cleans up user-entered phone numbers so that they can be sent as SMS messages.
    The expected format is: (NXX)-NXX-XXXX where N is any digit from 2 through 9 and X is any digit from 0 through 9.

    For example, the inputs

        +1 (613)-995-0253
        613-995-0253
        1 613 995 0253
        613.995.0253

    produce the output

    6139950253
    """

def __init__(self, phone_number):
        number = sub("[^0-9]", "", phone_number)
        length = len(number) 
        # ensuring phone numbers entered are in the correct NA format by providing various parameters. 
        if length < 10:
            raise ValueError("Not enough digits.") 
        if length > 10:
            if number[0] != '1':
                raise ValueError("Only 1 is considered a valid country code")
            number = number[1:]
        if int(number[0]) < 2 or int(number[3]) < 2:
            raise ValueError("(NXX)-NXX-XXXX - N must be greater 1")

        self.number = number
        self.area_code = number[:3]

def pretty(self):
    """
     Returns a "pretty" formated number in the format of (NXX)-NXX-XXXX.
     
    """
    pretty_number = "({}) {}-{}".format(
        self.number[:3],
        self.number[3:6],
        self.number[-4:])

    return pretty_number