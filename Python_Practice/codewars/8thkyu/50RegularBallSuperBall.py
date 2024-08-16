# Create a class Ball. Ball objects should accept 
# one argument for "ball type" when instantiated.

# If no arguments are given, ball objects should 
# instantiate with a "ball type" of "regular."

# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"

# -------------------------------------------------------------------------------------
# -----Solution 1-----Constructor & Default param-----
class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type
#   1. Create a class Ball
#   2. Create a constructor method that takes in a param type with a default value of "regular"
#   3. 'self.ball_type' assigns the provided 'type' to the instance variable 'ball_type'.
#   4. Return the ball_type attribute
#   This solution is the most efficient & concise way to solve the problem because 
#   it uses a default param value to set the ball_type attribute to "regular" if 
#   no type is provided. It is also easy to read & understand.
        

# -------------------------------------------------------------------------------------
# -----Solution 2-----Constructor & Additional Method-----
class Ball(object):
    def __init__(self,ball_type='regular'):
        self.ball_type = ball_type
    def __superball__(ball_type):
        self.ball_type = "super"
#   1. Create a class Ball
#   2. Create a constructor method that takes in a param ball_type with a default value of "regular"
#   3. Set the ball_type attribute to the ball_type param
#   4. Return the ball_type attribute
#   This solution is similar to the first solution, but it includes an additional method
#   __superball__ that sets the ball_type attribute to "super". This method is not necessary
#   for the problem, as the ball_type attribute can be set directly in the constructor method.
#   This solution is less efficient & more complex than the first solution because it includes
#   unnecessary code. It is also harder to read & understand.
        
# -------------------------------------------------------------------------------------
# -----Solution 3-----JavaScript Solution-----Constructor & Default Param-----     
# var Ball = function(ballType) {
#   this.ballType = ballType || 'regular';
# };
#   1. Create a constructor function Ball
#   2. Set the ballType attribute to the ballType param if it is provided, otherwise set it to 'regular'
#   This solution is similar to the first Python solution, using a default param value to set the ballType 
#   attribute to 'regular' if no type is provided. It is concise & easy to understand. With JavaScript,
#   `this` is used to refer to the current object, & the `||` operator is used to provide a default value
#   if the ballType param is not provided.

