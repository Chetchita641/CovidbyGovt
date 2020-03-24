import pandas as pd

HEADERS = ['Country name', 'Overall Score', 'Rank', 'Electoral process and pluralism', 'Functioning of government', 'Political participation', 'Political culture', 'Civil liberties']

def separate_words(word_list):
    country_words = []
    value_words = []
    for word in word_list:
        word = word.replace('=', '')
        if not word.replace('.', '', 1).isdigit():
            country_words.append(word)
        else:
            value_words.append(word)
    return country_words, value_words

def write_csv(countries, values, headers=HEADERS):
    filename = 'test.csv'
    with open(filename, 'w') as f:
        f.write(','.join(headers))
        f.write('\n')

        for i in range(len(countries)):
            f.write(countries[i] + ',')
            f.write(','.join(values[i]))
            f.write('\n')

    print('test.csv is written with {} lines'.format(len(countries)))
            

def main():
    with open('raw_data') as f:
        lines = f.readlines()
    
    countries = []
    values = []
    for line in lines:
        word_list = line.replace('\n', '').split(' ')
        country_words, value_words = separate_words(word_list)
        countries.append(' '.join(country_words))
        values.append(value_words)
    print('Num of countries: {}'.format(len(countries)))
    write_csv(countries, values)
        


if __name__ == "__main__":
    main()