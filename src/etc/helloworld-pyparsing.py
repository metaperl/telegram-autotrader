from pyparsing import Word, alphas

greet = Word(alphas) + "," + Word(alphas) + "!"
greeting = greet.parseString("Hello, World!")
print(greeting)
