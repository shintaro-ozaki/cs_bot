import arxiv
import random


def search_arxiv(query, num_papers):
    search = arxiv.Search(
        query=query,
        max_results=100,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    result_list = [ result for result in search.results()]

    results = random.sample(result_list, k=num_papers)

    for result in results:
        message = result.entry_id + "\n" + result.title + "\n" + result.summary + "\n"
        add_text = '<br>' + message
        with open("README.md", "r") as file:
            txt = file.read()
            txt = txt + add_text
            print(txt)

        with open("README.md", 'w') as file:
            file.write(txt)

def llm_commonsense():
    query ='ti:LLM AND ti:Commonsense'
    num_papers = 1
    search_arxiv(query, num_papers)

if __name__ == '__main__':
    llm_commonsense()

