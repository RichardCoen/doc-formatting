from tools import copy_files,qwen2
from Code_Generation import CodeGen_Simul,generated_code_integration
import requests
def qwen2_rsh(prompt):
    # 定义服务器的地址和端口号
    server_address = "http://192.168.200.218:8025"
    # 定义调用的端点 URL
    endpoint_url = server_address + "/generate"
    # 定义要发送的数据（prompt）
    data = {
        "prompt": prompt
    }
    # 发送 POST 请求到服务器
    response = requests.post(endpoint_url, json=data)
    # 获取服务器返回的响应
    if response.status_code == 200:
        response_data = response.json()
        generated_response = response_data['response']
        input_tokens = response_data['input_tokens']
        output_tokens = response_data['output_tokens']
        return generated_response, input_tokens, output_tokens
    else:
        print("Failed to generate response. Status code:", response.status_code)

def val_gen():
    pass
    i = 20
    dataset_name = "Val"
    model_name = "qwen2"
    api = qwen2
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i), 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "self_debug"
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/val_selfdebug_prompt.json",0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/fewshot_prompt/val_dataset/17_shot_prompt.json", 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 15
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name, doc_number, n_shot)
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,doc_number, n_shot), 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "direct_prompt"
    # CodeGen_Simul(api, dataset_name, model_name, method_name, "./prompt_data/direct_prompt/val_0_shot_prompt.json", 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # # refine1
    # method_name = "direct_prompt_refine1"
    # refile_prompt_name = "direct_prompt"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # n_shot = 17
    # doc_number = 15
    # method_name = "RAG_few_shot_refine1/e5_{}/{}_shot".format(doc_number, n_shot)
    # refile_prompt_name = "RAG_few_shot/e5_{}/{}_shot".format(doc_number, n_shot)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot_refine1/17_shot"
    # refile_prompt_name = "few_shot/17_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine1/e5_20"
    # refile_prompt_name = "doc_prompt/e5_20"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    #
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    # method_name = "self_debug_refine1"
    # refile_prompt_name = "self_debug"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


    # refine 2
    # refine_time = 2

    # refine 3
    refine_time = 3
    # method_name = "self_debug_refine{}".format(refine_time)
    # last_method_name = "self_debug_refine{}".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     last_method_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    method_name = "direct_prompt_refine{}".format(refine_time)
    last_method_name = "direct_prompt_refine{}".format(refine_time - 1)
    copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
               dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    CodeGen_Simul(api, dataset_name, model_name, method_name,
                  "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
                                                                        last_method_name, refine_time), 0,
                  955)
    generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # n_shot = 17
    # doc_number = 15
    # method_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time, doc_number, n_shot)
    # refile_prompt_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time - 1, doc_number, n_shot)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot_refine{}/17_shot".format(refine_time)
    # refile_prompt_name = "few_shot_refine{}/17_shot".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine{}/e5_20".format(refine_time)
    # refile_prompt_name = "doc_prompt_refine{}/e5_20".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


def tes_gen():
    dataset_name = "Test"
    model_name = "qwen2"
    api = qwen2
    for i in [17]:
        method_name = "few_shot/{}_shot".format(i)
        CodeGen_Simul(api, dataset_name, model_name, method_name,
                      "./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i), 423, 956)
        generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
    for i in [1]:
        method_name = "few_shot/{}_shot".format(i)
        CodeGen_Simul(api, dataset_name, model_name, method_name,
                      "./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i), 0, 34)
        generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

def qwen2_random_fewshot():
    api = qwen2_rsh
    #random_time
    dataset_name = "Test"
    model_name = 'Qwen2'
    for shot_number in [1,9,21]:
        method_name = "random_fewshot/{}_shot/".format(shot_number)
        CodeGen_Simul(api, dataset_name, model_name, method_name,"./prompt_data/random_shot_fewshot/Test/{}shot_random_prompt.json".format(shot_number), 0,955)
        generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


if __name__ == '__main__':
    pass
    # tes_gen()
    # val_gen()
    qwen2_random_fewshot()

    # print(qwen2_rsh("请介绍你自己"))