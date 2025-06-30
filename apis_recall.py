import re
from tools import read_json,write_dict_to_json
import pandas as pd
import numpy as np
from sklearn.metrics import recall_score
def recall_at_k(y_true, y_pred, k):
    """
    计算 R@k
    y_true: list of lists, 每个子列表包含该查询的所有相关文档的ID
    y_pred: list of lists, 每个子列表包含该查询的检索结果的文档ID（按相关性排序）
    k: int, 计算 R@k 时考虑的前 k 个检索结果
    """
    recalls = []
    for true_docs, pred_docs in zip(y_true, y_pred):
        # 取前 k 个检索结果
        pred_at_k = pred_docs[:k]
        # 计算召回率
        num_relevant = len(set(pred_at_k) & set(true_docs))
        recall = num_relevant / len(true_docs) if len(true_docs) > 0 else 0
        recalls.append(recall)

    return np.mean(recalls)





def groundtruth_docs_get(dataset_file, save_file):
    unit_data = pd.read_excel("./property.xlsx",sheet_name="whole")
    unit_dir = {"pt":"point","cm":"centimeter","ch":"character","lines":"lines"}

    data_list = read_json(dataset_file)["data_list"]
    results = []
    for data in data_list:
        property_docs = []
        unit_docs = []
        for para_key, para_value in data["paragraphs"].items():
            property_docs += para_value["property_read"]
            unit_id_list = [i[2] for i in para_value["property_adjust"]]
            for unit_id in unit_id_list:
                unit_index = int(unit_id)
                unit_key = unit_data["unit"][unit_index]
                if unit_key in unit_dir.keys():
                    unit_docs.append(unit_dir[unit_key])

        docs = list(set(property_docs+unit_docs))
        results.append({"id":data["id"],"docs":docs})

    y_true = [result["docs"] for result in results]
    write_dict_to_json({"description":"api docs for groundtruth","data_list":results,"y_true":y_true},save_file)

def RAG_source_get(RAG_file,save_file):
    rag_list = read_json(RAG_file)["data_list"]
    results = []
    y_rag = []
    for rag in rag_list:
        # 原始字符串
        data = rag["docs"]
        # 使用正则表达式提取source部分和数字部分
        pattern = re.compile(r"'source': '([^']+)'.*?(\d+\.\d+)")
        matches = pattern.findall(data)
        result = [(source.split("/")[-1].replace(".txt",""),score) for source,score in matches]
        y = []
        for r in result:
            y.append(r[0])
        y_rag.append(y)
        results.append({"id":rag["id"],"rag":result})

    write_dict_to_json({"description":"RAG docs name and score, top 20","data_list":results,"y_rag":y_rag},save_file)



if __name__ == '__main__':
    # 示例数据
    # groundtruth_docs_get(dataset_file="./dataset/test_data.json", save_file="./RAG_result/test_grountruth.json")
    y_true = read_json("./RAG_result/test_grountruth.json")["y_true"]

    for embedding_name in ["bge","e5","gte","mxbai"]:
        rag_file = "./prompt_data/recall_prompt/test_dataset/{}/{}_RAG_20_whole.json".format(embedding_name,embedding_name)
        save_file = "./RAG_result/{}_20.json".format(embedding_name)
        RAG_source_get(RAG_file=rag_file,save_file=save_file)
        y_pred = read_json(save_file)["y_rag"]

        r1 = recall_at_k(y_true, y_pred, 1)
        r5 = recall_at_k(y_true, y_pred, 5)
        r10 = recall_at_k(y_true, y_pred, 10)
        r15 = recall_at_k(y_true, y_pred, 15)
        r20 = recall_at_k(y_true, y_pred, 20)
        print(embedding_name)
        print(f'R@1: {r1:.4f}')
        print(f'R@5: {r5:.4f}')
        print(f'R@10: {r10:.4f}')
        print(f'R@15: {r15:.4f}')
        print(f'R@20: {r20:.4f}')
        print("-"*20)