class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for char in punctuation:
                    text = text.replace(char, '')
                words = text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        result = {}

        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1

        return result

    def count(self, word):
        word = word.lower()
        result = {}

        for name, words in self.get_all_words().items():
            result[name] = words.count(word)

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

