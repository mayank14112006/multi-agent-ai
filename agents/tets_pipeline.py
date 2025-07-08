# test_pipeline.py

from search_agent import search
from answer_agent import generate_answer

if __name__ == "__main__":
    query = input("Ask a question: ")
    chunks = search(query)

    print("\nTop matching chunks:\n")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk[:200]}...\n")  # Preview

    response = generate_answer(query, chunks)

    print("\n💬 AI Assistant Response:")
    print(response)
