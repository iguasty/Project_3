import array as arr

class Person:
    def __init__(self,
                 new_name: str = "unnamed person",
                 new_handidness: bool = 1,  # 0 for left handed, 1 for right hand
                 new_throw_speed: int = 0,  
                 new_throw_direction: int = 0): # in degrees   
        """Initialize a Person"""
        self.name = new_name
        self.handidness = self.handidness_set(new_handidness)
        self.throw_speed = self.throw_speed_set(new_throw_speed)
        self.throw_direction = self.throw_direction_set(new_throw_direction)

    def nameset(self, namey):
        """sets persons name"""
        self.name = namey
        return self.name
    
    def handidness_set(self, handidness):
        """sets handidness (either left or right handed)"""
        if handidness == 0:
                return "Left handed"
        elif handidness == 1:
                return "Right handed"
        else:
            raise ValueError("Handidness must be 0(left handed) or 1(right handed)")  
    
    def throw_speed_set(self, throw_speed):
        """sets throw speed"""
        if throw_speed < 0:
            raise ValueError("Throw speed must be a non-negative number")
        return throw_speed
    
    def throw_direction_set(self, throw_direction):
        """sets throw direction (in degrees 0-360)"""
        if not 0 <= throw_direction <= 360:
            raise ValueError("Throw direction must be between 0 and 360 degrees")
        return throw_direction
    
def person_error_test():
    """Test function for input error handling. Change person attributes to test. Outputs to console"""
    try: 
        person = Person("Jimmy", 12, -10, 600)
    except ValueError as e:
        print(e)