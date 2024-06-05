adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

string_task_01 = adwentures_of_tom_sawer.replace('\n', ' ')
print(string_task_01)

# task 02 ==
""" Замініть .... на пробіл
"""

string_task_02 = string_task_01.replace('....', ' ')
print(string_task_02)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

string_task_03 = string_task_02.replace('   ', ' ')
print(string_task_03)

print(f'Кількість подвійних пробілів: {string_task_03.count('  ')}')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(f'Літера "h" у тексті зустрічається {string_task_03.count('h')} разів')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

task_04 = string_task_03.split()
print(task_04)
task_05 = len([word for word in task_04
                      if word[0].isupper() or (len(word) > 1 and word[1].isupper())])
print('Кількість слів у тексті з першою заглавною літерою:', task_05)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_index = task_04.index("Tom")
second_index = task_04.index("Tom", first_index + 1)

print('Позиція, на якій слово Tom зустрічається вдруге:', second_index)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

task_07 = string_task_03.split('. ')
print('Кількість речень:', len(task_07))
adwentures_of_tom_sawer_sentences = task_07
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

task_08 = adwentures_of_tom_sawer_sentences[3]
print(task_08)
print(task_08.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

task_09 = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith('By the time'):
        task_09 = True
print("Є речення, що починається з 'By the time':", task_09)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
sentence_last = adwentures_of_tom_sawer_sentences[-1]
print(sentence_last)
sentence_last_words = sentence_last.split()
print('Кількість слів останнього речення:', len(sentence_last_words))