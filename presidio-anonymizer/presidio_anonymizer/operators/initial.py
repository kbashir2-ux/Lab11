from presidio_anonymizer.operators.operator import Operator
import re

class Initial(Operator):
    def operator_name(self):
        return "initial"
    
    def operator_type(self):
        return "Anonymize"
    
    def validate(self, params: dict):
        pass

    def operate(self, text: str) -> str:
        anonymized_text = []
        for word in text.split():
            if word.isalpha():
                anonymized_text.append(word[0].upper() + ".")
            else:
                anonymized_text.append(word)

        return " ".join(anonymized_text)
