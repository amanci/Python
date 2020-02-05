import unittest #NOQA

def index_palavra(palavra): #NOQA
    palavra_dic = {}
    for i in range(len(palavra)):
        palavra_dic[i] = palavra[i]
    print(palavra_dic)
    return palavra_dic


index_palavra('ALLAN')


class TestSum(unittest.TestCase): #NOQA

    def test_index_palavra(self): #NOQA
        palavra_dicionario = {
            0: 'p',
            1: 'a',
            2: 'l',
            3: 'a',
            4: 'v',
            5: 'r',
            6: 'a'
        }
        self.assertEqual(index_palavra('palavra'),
                         palavra_dicionario,
                         )


if __name__ == '__main__':
    unittest.main()
