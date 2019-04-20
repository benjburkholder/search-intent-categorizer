"""
This program categorizes queries by what SERP features are present for the query.
~ Informational
~ Navigational
~ Transactional
~ Commercial Investigation
"""

from lib.google_search_results import GoogleSearchResults

api_key = open('serp-api-key.txt').read()

downloadFile = 'serp-intent-results.csv'
file = open(downloadFile, 'w')

columnHead = 'Query,Search Intent Type,Paid Ad Companies,Top 5 Organic Results\n'
file.write(columnHead)

with open('serp_intent_queries.txt') as content:
    content = [line.rstrip('\n') for line in content]

# If user location can remain static, location field can be hardcoded with a specific location.
    for line in content:
        print(f'Analyzing {line}...')
        params = {
            "q": str(line),
            "location": "cleveland,ohio,United States",  # Location used in API query is static
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com",
            "api_key": api_key,
        }

        query = GoogleSearchResults(params)
        dictionary_results = query.get_dictionary()

    # Information Search Intent
        serpURLs = []
        orgRes = dictionary_results['organic_results']
        for url in orgRes:
            if url['position'] <= 5:
                serpURLs.append(url['link'])
                # print(url['link'])
        try:
            answerbox = dictionary_results['answer_box']
            paa = dictionary_results['related_questions']
        except KeyError:
            pass
        else:
            print(f'{line}, Information Search Intent, ,"{serpURLs}"')
            file.write(f'"{line}", Information Search Intent, ,"{serpURLs}"\n')

    # Navigational Search Intent
        try:
            knowledge_graph = dictionary_results['knowledge_graph']
            site_links = dictionary_results['organic_results'][0]['sitelinks']
        except KeyError:
            pass
        else:
            print(f'{line}, Navigational Search Intent')
            file.write(f'"{line}", Navigational Search Intent, ,"{serpURLs}"\n')

    # Transactional
        try:
            shopping_ads = dictionary_results['shopping_results']
        except KeyError:
            pass
        else:
            print(f'{line}, Transactional Search Intent, ,"{serpURLs}"')
            file.write(f'"{line}", Transactional Search Intent, ,"{serpURLs}"\n')

    # Paid Ads Present
        try:
            paid_ads = dictionary_results['ads']
        except (KeyError, NameError):
            pass
        else:
            competitors = []
            for data in paid_ads:
                competitors.append(str(data['link']))
            row = f'"{line}", Paid Search Ads Present,"{competitors}"\n'
            # print(row)

            file.write(row)

    # Commercial Investigation
        results = []
        bottom_ads = ''

        try:
            ads = dictionary_results['ads']
            answerbox = dictionary_results['answer_box']
            paa = dictionary_results['related_questions']
            organic_results = dictionary_results['organic_results']
            for pos in organic_results:
                results.append(1)

            if len(results) > 10:
                bottom_ads = True
        except KeyError:
            pass
        else:
            if bottom_ads != '':
                print(f'{line}, Commercial Investigation, ,"{serpURLs}"')
                file.write(f'"{line}", Commercial Investigation, ,"{serpURLs}"\n')
        print(f'Analyzing {line}...done.')
file.close()