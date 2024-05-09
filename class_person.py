
class Person:
    def __init__(self,
                 new_name: str = "unnamed person",
                 new_handidness: bool = 1):   # 0 for left handed, 1 for right hand
        """Initialize a Person"""
        self.name = new_name
        self.handidness = new_handidness

    def nameset(self, namey):
        """Set persons name

        Returns:
            _type_: name
        """
        self.name = namey
        return self.name
    
    def handidness(self, handidness):
        """Assigns handidness

        Args:
            handidness (bool): 0 for left handed, 1 for right handed

        Returns:
            _type_: handidness
        """
        # match case for determining ability type
        if handidness == 0:
                return "Left handed"
        elif handidness == 1:
                return "Right handed"