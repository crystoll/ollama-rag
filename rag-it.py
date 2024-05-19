import ollama
import chromadb
import feedparser

rss_feed_link = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
collection_name = "nyt_tech_feed"

feed = feedparser.parse(rss_feed_link)
entries = feed.entries

documents = []
metadatas = []
ids = []

for entry in entries:
    title = entry.title
    link = entry.link
    content = entry.summary
    tags = ", ".join([t["term"] for t in entry.tags])
    documents.append(f"# {title}\n{content}")
    metadatas.append({"title": title, "link": link, "tags": tags})
    ids.append(link)

client = chromadb.Client()

collection = client.get_or_create_collection(collection_name)

collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

prompt = "List top 3 most interesting AI related news with summaries and reference link"

query_result = collection.query(
    query_texts=[prompt]
)

context = query_result["documents"][0]


stream = ollama.chat(
    model='phi3',
    messages=[
        {
            "role": "system",
            "content": f"Answer the questions based on the news feed given here only. If you do not know the answer, say I do not know. The news feed content is here:\n\n------------------------------------------------\n\n{context}\n\n------------------------------------------------\n\n"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    stream=True
)

for chunk in stream:
    print(chunk["message"]["content"], end="")



# response = ollama.chat(
#     model='phi3',
#     messages=[
#         {
#             "role": "system",
#             "content": f"Answer the questions based on the news feed given here only. If you do not know the answer, say I do not know. The news feed content is here:\n\n------------------------------------------------\n\n{context}\n\n------------------------------------------------\n\n"
#         },
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
# )

# print(response["message"]["content"])

# response = ollama.generate(model='phi3',
#                            prompt=f'List top 3 best AI news from this information:\n\n{context}')
# print(response['response'])
