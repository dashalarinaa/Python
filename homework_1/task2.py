#  Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

S = int(input())
P = int(input())
X = int(0)
Y = int(0)
for X in range (1001): 
    for Y in range (1001):
        if S == X + Y and P == X * Y:
            print(X, Y)
        else:
            X += 1
            Y += 1
