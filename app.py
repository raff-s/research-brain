import sys
from langchain.chains import RetrievalQA
from vector_db import VectorDb
from open_ai import OpenAi

def process_llm_response(llm_response):
    print('\nAnswer:')
    print(llm_response['result'])
    print('\n\nSources:')
    for source in llm_response["source_documents"]:
        print(f"{source.metadata['source']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please ask a question")
        sys.exit(1)

    query = sys.argv[1]
    open_ai = OpenAi()
    vector_db = VectorDb()

    llm = open_ai.gpt3_5()
    retriever = vector_db.db_retriever()

    qa_chain = RetrievalQA.from_chain_type(llm=llm, 
                                    chain_type="stuff", 
                                    retriever=retriever, 
                                    return_source_documents=True)

    llm_response = qa_chain(query)

    process_llm_response(llm_response)