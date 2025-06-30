from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain_text_splitters import CharacterTextSplitter
import os
from tools import read_json,write_dict_to_json
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

def db_create(embeddings, folder_path, save_path):
    file_names = os.listdir(folder_path)
    first_file_path = os.path.join(folder_path, file_names[0])
    loader = TextLoader(first_file_path )
    docs = loader.load()
    db = FAISS.from_documents(docs, embeddings)
    for file in file_names[1:]:
        file_path = os.path.join(folder_path, file)
        loader = TextLoader(file_path)
        docs = loader.load()
        db.add_documents(docs)

    db.save_local(save_path)



def step_db(embeddings,api_docs = "./step_apis/property.txt",save_dir = "./step_apis/property_list_index"):
    # This is a long document we can split up.
    with open(api_docs) as f:
        properties = f.read()

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    property_list = properties.split("\n")
    docs = text_splitter.create_documents(property_list)

    #print(docs)
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(save_dir)

def api_recall(embeddings,query="adjust paragraph's alignment to 'Justified'",index_dir = "./apis/property_w_unit_index",recall_k = 5):
    vec_database_path = index_dir
    property_db = FAISS.load_local(vec_database_path, embeddings, allow_dangerous_deserialization=True)
    recall_docs = property_db.similarity_search_with_score(query,k=recall_k)
    return recall_docs


def atomic_recall():
    atomic_data = read_json("./simulation_data/atomic_simulation.json")["data_list"]
    recall_results = []
    acc = 0
    for data in atomic_data:
        query = data["best_input"]
        apis_need = data["apis"]
        apis_recall = "Api documentation apis you may need:\n" + api_recall(query)
        if_right = apis_recall in apis_need
        recall_results.append({"id": data["id"], "query": query, "apis_need": apis_need, "apis_recall": apis_recall,
                               "prompt": data["prompt"], "if_right": if_right})
        if if_right:
            acc += 1

    write_dict_to_json({"accuracy": acc / 137, "data_list": recall_results}, "./apis/query_test.json")
    print(acc)


def api_name_recall(query,db):
    result = db.similarity_search_with_score(query)
    return result[0][0].page_content,float(result[0][1])


def test_embedding():
    # sentences = ['That is a happy person', 'That is a very happy person']
    # model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
    # embeddings = model.encode(sentences)
    # print(cos_sim(embeddings[0], embeddings[1]))


    model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1", trust_remote_code=True)
    sentences = ['That is a happy person', 'That is a very happy person']
    embeddings = model.encode(sentences)
    print(cos_sim(embeddings[0], embeddings[1]))




if __name__ == '__main__':

    # model_name = "BAAI/bge-large-en-v1.5"
    # model_kwargs = {'device': 'cpu'}
    # encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity
    # model = HuggingFaceBgeEmbeddings(
    #     model_name=model_name,
    #     model_kwargs=model_kwargs,
    #     encode_kwargs=encode_kwargs,
    #     query_instruction="为这个句子生成表示以用于检索相关文章："
    # )
    # # db_create(embeddings=model, folder_path="./apis/property_w_unit/",save_path="./apis/property_w_unit_index")

    model_name = "mixedbread-ai/mxbai-embed-large-v1"
    model_kwargs = {'device': 'cpu',"trust_remote_code":True}
    encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity
    model = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
        query_instruction="为这个句子生成表示以用于检索相关文章："
    )
    db_create(embeddings=model, folder_path="./apis/property_w_unit/",save_path="./apis/MXBAI/property_w_unit_index")
    # model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
    #
    # result = api_recall(embeddings=model,query="""{'debug_Info': {'code': 'InvalidArgument', 'message': 'InvalidArgument', 'errorLocation': '', 'statement': 'v.alignment = ...;', 'surroundingStatements': ['var v = context.root._getObjectByReferenceId("024!00000141");', 'v.outlineLevel = ...;', '// >>>>>', 'v.alignment = ...;', '// <<<<<'], 'fullStatements': ['Please enable config.extendedErrorLogging to see full statements.']}""",recall_k=3)
    # s = str(result)
    # print(s)
