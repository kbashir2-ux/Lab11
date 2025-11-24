from presidio_anonymizer.operators.operator import Operator

class Initial(Operator):
    def operator_name(self):
        return "initial"
    
    def operate(self, text: str) -> str:
        # 
        return text
