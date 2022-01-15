from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import CalcForm

operators = ['+', '-', '/', '*']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
history = []


class Calc:
    @staticmethod
    def add(x, y): return float(x) + float(y)

    @staticmethod
    def odd(x, y): return float(x) - float(y)

    @staticmethod
    def div(x, y): return float(x) / float(y)

    @staticmethod
    def mul(x, y): return float(x) * float(y)


class Solve(object):
    def __init__(self):
        self.input_string = None
        self.value_el = []

    @staticmethod
    def index_of(val, in_list):

        try:
            return in_list.index(val)
        except ValueError:
            return -1

    @property
    def result(self):
        return self.value_el[0]

    @result.setter
    def result(self, input_string):
        self.value_el = input_string.split(' ')
        while True:
            mul_index = self.index_of('*', self.value_el)
            print(mul_index)
            if mul_index != -1:
                index_a = int(mul_index - 1)
                index_b = int(mul_index + 1)
                result = Calc.mul(self.value_el[index_a], self.value_el[index_b])
                del self.value_el[index_a:index_b + 1]
                self.value_el.insert(index_a, result)
                continue
            div_index = self.index_of('/', self.value_el)
            if div_index != -1:
                index_a = int(div_index - 1)
                index_b = int(div_index + 1)
                result = Calc.div(self.value_el[index_a], self.value_el[index_b])
                del self.value_el[index_a:index_b + 1]
                self.value_el.insert(index_a, result)
                continue
            add_index = self.index_of('+', self.value_el)
            if add_index != -1:
                index_a = int(add_index - 1)
                index_b = int(add_index + 1)
                result = Calc.add(self.value_el[index_a], self.value_el[index_b])
                del self.value_el[index_a:index_b + 1]
                self.value_el.insert(index_a, result)
                continue
            odd_index = self.index_of('-', self.value_el)
            if odd_index != -1:
                index_a = int(odd_index - 1)
                index_b = int(odd_index + 1)
                result = Calc.odd(self.value_el[index_a], self.value_el[index_b])
                del self.value_el[index_a:index_b + 1]
                self.value_el.insert(index_a, result)
                continue
            break


class SolveCalc(object):
    def __init__(self):
        self.new_calc = None
        self.is_valid = False
        self.result = None

    def get_result(self):
        return self.result

    @staticmethod
    def is_valid_new_calc(new_calc):
        print(new_calc)
        if new_calc == '':
            return False
        elif new_calc[-1] == ' ':
            return False
        elif new_calc.find(' ') == -1:
            return False
        else:
            return True

    @property
    def init_calc(self):
        return self.is_valid

    @init_calc.setter
    def init_calc(self, new_calc):
        if self.is_valid_new_calc(new_calc):
            self.new_calc = new_calc
            self.is_valid = True
            new_solve = Solve()
            new_solve.result = new_calc
            self.result = new_solve.result

        else:
            self.is_valid = False
            print(self.is_valid)


def calc_view(request):
    form = CalcForm()
    is_valid = None

    if request.method == 'POST':
        value = request.POST['calc']
        new_calc = SolveCalc()
        new_calc.init_calc = value
        is_valid = new_calc.init_calc
        if is_valid:
            history.append(value + ' = ' + str(new_calc.get_result()))

        form = CalcForm(initial={'calc': str(new_calc.get_result()) if is_valid else value})

    return render(request, 'calc/calc.html',
                  {'form': form, 'operators': operators, 'numbers': numbers, 'is_valid': is_valid,
                   'history': history})
