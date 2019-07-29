#Author : Roche Christopher
#File created on 29 Jul 2019 9:14 PM

class SIMPLE_LPF:
    #implementation of simple IIR filter in https://zipcpu.com/dsp/2017/08/19/simple-filter.html
    #y[n] = ( y[n -1] ) + ( beta * (x[n] - y[n-1] ) )

    def __init__(self, beta, initial_data):
        self.beta = beta
        self.output = initial_data
        self.round = 2
        
    def update(self, input):
        self.output = self.output + ( self.beta * (input - self.output))

    def get_output(self):
        return round(self.output, self.round)
