class Controller:
    def __innit__(self, KP:float, KD:float):

        self.KP=KP
        self.KD=KD
        self.previous_error = 0.0

    def compute_input(self, output_depth:float, reference_depth:float) -> float:
        error = reference_depth - output_depth
        derivative = error - self.previous_error
        input = (self.KP*error)+(self.KD*derivative)
        self.previous_error=error
        return input
    
