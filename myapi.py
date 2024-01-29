import paralleldots


class API:
    def __init__(self):
        paralleldots.set_api_key("ZZCwyYGC8Cqg6D3hrPhKQ1K1VKhm0UL9CAhOETthS5s")

    def sen_analysis(self, input):
        response = paralleldots.sentiment(input)
        return response

    def n_analysis(self, input):
        response = paralleldots.ner(input)
        return response

    def em_analysis(self, input):
        response = paralleldots.abuse(input)
        return response
