from search_engine.SearchEngineBase import main, SearchEngineBase


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


def simple_engine_main():
    search_engine = SimpleEngine()
    main(search_engine)


if __name__ == '__main__':
    simple_engine_main()
