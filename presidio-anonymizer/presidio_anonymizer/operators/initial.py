from presidio_anonymizer.operators.operator import Operator, OperatorType
import re

class Initial(Operator):
    def operator_name(self):
        return "initial"
    
    def operator_type(self):
        return "Anonymize"
    
    '''
    def operator_type(self):
    return OperatorType.Anonymize
    '''
    
    def validate(self, params: dict):
        pass

    def operate(self, text: str) -> str:
        text = ' '.join(text.split())
        anonymized_text = []
        for word in text.split():
                non_alpha_prefix = ''
                while word and not word[0].isalnum():
                    non_alpha_prefix += word[0]
                    word = word[1:]

                if word.isalpha():
                    anonymized_text.append(non_alpha_prefix + word[0].upper() + ".")
                
                else:
                    anonymized_text.append(non_alpha_prefix + word)

        return " ".join(anonymized_text)
