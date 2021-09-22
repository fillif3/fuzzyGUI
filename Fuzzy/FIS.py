from utlis import centroid

MAMDANI=0
SUGENO=1

class Rule:
    def __init__(self, inputs, output,input_connection_func=min):
        self.inputs = inputs
        self.input_connection_func = input_connection_func
        self.output = output


class FIS:
    def __init__(self,input_universes,output,rules,type=MAMDANI,defuzzfication=None):
        self.input_universes=input_universes
        self.outputs=outputs
        self.rules=rules
        self.type=type
        self.defuzzfication=defuzzfication

    def getOutput(self,inputs):
        weights,output_indexes= self.getWeightsOutputTuple(inputs)
        sum_weights=sum(weights)
        final_output=0
        if self.type==SUGENO:
            for w,oi in zip(output_indexes):
                final_output+=w*self.outputs[oi](inputs)
            return final_output/sum_weights
        if self.type==MAMDANI:
            return centroid(self.outputs[output_indexes],weights)



