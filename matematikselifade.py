class PDA:
    def _init_(self):
        self.stack = ['Z0']
    def transition(self, durum, symbol):
        if durum == 'q0':
            if symbol.isdigit():
                return 'q1'
            elif symbol == '(':
                self.stack.append(symbol)
                return 'q0'
            else:
                return False
        elif durum == 'q1':
            if symbol in '+-*/':
                return 'q2'
            elif symbol == ')':
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
                    return 'q1'
                else:
                    return False
            else:
                return False
        elif durum == 'q2':
            if symbol.isdigit():
                return 'q1'
            elif symbol == '(':
                self.stack.append(symbol)
                return 'q0'
            else:
                return False
        return False

    def validate_expression(self, expression):
        durum = 'q0'
        for symbol in expression:   
            durum = self.transition(durum, symbol)
            if durum is False:
                return False
        return durum == 'q1' and self.stack == ['Z0']

if _name_ == "_main_":
    pda = PDA() 
    while True:
        expr = input("Kontrol etmek istediğiniz matematiksel ifadeyi girin (çıkmak için 'exit' yazın): ")
        if expr.lower() == 'exit':
            break
        if pda.validate_expression(expr):
            print(f"'{expr}' geçerli bir ifade.")
        else:
            print(f"'{expr}' geçersiz bir ifade.")