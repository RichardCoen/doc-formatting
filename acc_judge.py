from tools import read_json,copy_files

acc_rag_refine= read_json("./acc/Val/deepseek_v2/RAG_few_shot_refine3/e5_15/17_shot_acc.json")["acc_dict"]
acc_rag =read_json("./acc/Val/deepseek_v2/RAG_few_shot/e5_15/17_shot_acc.json")["acc_dict"]

dataset_name = "Val"
model_name = "llama3"

# refine_time =3
# n_shot = 17
# doc_number = 15
# method_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time,doc_number, n_shot)
# refile_prompt_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time-1,doc_number, n_shot)
# copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#                    dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))


for i in acc_rag.keys():
    if acc_rag[i] > acc_rag_refine[i]:
        print(i)


