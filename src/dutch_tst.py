
import requests
import re
import random
import numpy as np
from pprint import pprint
from bs4 import BeautifulSoup

def main():
    page_url = "http://mylanguages.org/dutch_vocabulary.php"

    r = requests.get(page_url)

    soup = BeautifulSoup(r.text, features="html.parser")
    # print(soup)

    td_list = soup.find_all("td")
    # print(td_list)

    td_values = [x.text for x in td_list]
    # print(td_values)

    arrDutchWords      = []
    arrEnglishWords    = []

    for index in range(0, len(td_values), 2):
        # print(index)
        a = td_values[index: index + 2]
        isCapital = re.match('^[A-Z]+', a[0])

        if a[0] == '' or a[1] == '':
            continue

        if isCapital:
            continue
        arrDutchWords.append(a[0])
        arrEnglishWords.append(a[1])

    arrWordsDictionary = dict(zip(arrDutchWords, arrEnglishWords))
    # print(arrWordsDictionary)
    # exit()

    # pythonの関数
    # with open('dutch_vocabs.txt', 'w') as f:
    #     for value in splited_list:
    #         f.write(value[0] + ' ' + value[1] + "\n")

    n_tests     = 2
    n_questions = 50

    for test_num in range(n_tests):
        with open('dutch_vocab_tst_{:02d}.txt'.format(test_num + 1), 'w') as f:
            f.write(
                'no{} Dutch Vocaburary Test\n\n'.format(test_num + 1))

            for question_num in range(n_questions):
                question_word  = random.choice(arrDutchWords)
                correct_answer = arrWordsDictionary[question_word]

                arrEnglishWords_copy = arrEnglishWords.copy()
                arrEnglishWords_copy.remove(correct_answer)
                wrong_answers = random.sample(arrEnglishWords, 3)

                answer_options = [correct_answer] + wrong_answers
                random.shuffle(answer_options)

                f.write('Q{}. {}\n\n'.format(question_num + 1, question_word))

                for i in range(4):
                    f.write('{}. {}\n'.format(i + 1, answer_options[i]))
                f.write('\n\n')





if __name__ == "__main__":
    main()