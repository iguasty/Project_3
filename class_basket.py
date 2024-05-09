import array as arr
import random
class Basket:
    def __init__(self,
                 new_basket_num: int = 0,
                 new_coordinates = arr.array('i', [0,0])):   # initial x,y coordinates of blank basket
        """Initialize a Basket"""
        self.basket_num = new_basket_num
        self.coordinates = new_coordinates

    def basket_num_set(self, basket_numy):
        """Set basket number

        Args: 
            basket_numy (int)
        Returns:
            _type_: basket number
        """
        self.basket_num = basket_numy
        return self.basket_num
    
    def coordinate_set(self):
        """Assigns random coordinates to basket

        Returns:
            _type_: coordinates (array)
        """
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        self.coordinates = arr.array('i',[x,y])
        return self.coordinates