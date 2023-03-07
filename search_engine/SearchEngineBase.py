class SearchEngineBase(object):
    def __init__(self):
        pass

    # add_corpus() 函数负责读取文件内容，将文件路径作为 ID，连同内容一起送到 process_corpus 中。
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    # process_corpus 需要对内容进行处理，然后文件路径为 ID ，将处理后的内容存下来。处理后的内容，就叫做索引（index）。
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    # search 则给定一个询问，处理询问，再通过索引检索，然后返回
    def search(self, query):
        raise Exception('search not implemented.')


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', 'full_text.txt']:
        search_engine.add_corpus(file_path)

    while True:
        # 需要用户输入
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)
