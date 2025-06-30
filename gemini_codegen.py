from tools import llama3,copy_files,gemini_api,deepseek_v2,code_qwen
from Code_Generation import CodeGen_Simul,generated_code_integration


def llama3_gen():
    # llama3
    i = 20
    dataset_name = "Val"
    model_name = "llama3"
    api = llama3
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(llama3, dataset_name, model_name, method_name,
    #               "./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i), 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "self_debug"
    # CodeGen_Simul(llama3, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/val_selfdebug_prompt.json", 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(llama3, dataset_name, model_name, method_name,
    #               "./prompt_data/fewshot_prompt/val_dataset/17_shot_prompt.json", 667, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 15
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name, doc_number, n_shot)
    # CodeGen_Simul(llama3, dataset_name, model_name, method_name,
    #               "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,doc_number, n_shot), 864, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "direct_prompt"
    # CodeGen_Simul(api, dataset_name, model_name, method_name, "./prompt_data/direct_prompt/val_0_shot_prompt.json", 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # api = llama3
    # # refine1
    # n_shot = 17
    # doc_number = 15
    # method_name = "RAG_few_shot_refine1/e5_{}/{}_shot".format(doc_number, n_shot)
    # refile_prompt_name = "RAG_few_shot/e5_{}/{}_shot".format(doc_number, n_shot)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "direct_prompt_refine1"
    # refile_prompt_name = "direct_prompt"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "few_shot_refine1/17_shot"
    # refile_prompt_name = "few_shot/17_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine1/e5_20"
    # refile_prompt_name = "doc_prompt/e5_20"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "self_debug_refine1"
    # refile_prompt_name = "self_debug"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # refine2
    # refine 3
    refine_time = 3
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

    # method_name = "few_shot_refine{}/17_shot".format(refine_time)
    # refile_prompt_name = "few_shot_refine{}/17_shot".format(refine_time-1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name,refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine{}/e5_20".format(refine_time)
    # refile_prompt_name = "doc_prompt_refine{}/e5_20".format(refine_time-1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name,refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "self_debug_refine{}".format(refine_time)
    # refile_prompt_name = "self_debug"
    # last_method_name = "self_debug_refine{}".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     last_method_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # refine2
    refine_time = 2
    # refine 3
    refine_time = 3
    method_name = "direct_prompt_refine{}".format(refine_time)
    last_method_name = "direct_prompt_refine{}".format(refine_time - 1)
    copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
               dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    CodeGen_Simul(api, dataset_name, model_name, method_name,
                  "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
                                                                        last_method_name, refine_time), 0,
                  955)
    generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

def gemini_test_explore_refine2_5():
    dataset_name = "Test"
    model_name = "gemini_pro"
    api = gemini_api
    # refine_time = 2
    refine_time = 5
    for n_shot in [13,17,21]:
        for doc_number in [5,10,15,20]:
            method_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time, doc_number, n_shot)
            refile_prompt_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time - 1, doc_number, n_shot)
            copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
                       dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
            CodeGen_Simul(api, dataset_name, model_name, method_name,
                          "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
                                                                                refile_prompt_name, refine_time), 0,
                          955)
            generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


def codeqwen_gen():
    dataset_name = "Val"
    model_name = "codeqwen"
    api = code_qwen
    # method_name = "direct_prompt"
    # CodeGen_Simul(api, dataset_name, model_name, method_name, "./prompt_data/direct_prompt/val_0_shot_prompt.json", 915,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "direct_prompt_refine1"
    # refile_prompt_name = "direct_prompt"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # refine2
    # refine_time = 2
    # refine 3
    refine_time = 3
    method_name = "direct_prompt_refine{}".format(refine_time)
    last_method_name = "direct_prompt_refine{}".format(refine_time - 1)
    copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
               dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    CodeGen_Simul(api, dataset_name, model_name, method_name,
                  "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
                                                                        last_method_name, refine_time), 0,
                  955)
    generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


def gemini_pro_random_fewshot():
    api = gemini_api
    #random_time
    dataset_name = "Test"
    model_name = 'gemini_pro'
    # for random_time in [1,2,3]:
    #     method_name = "random_fewshot/random_{}".format(random_time)
    #     CodeGen_Simul(api, dataset_name, model_name, method_name,"./prompt_data/random_shot_fewshot/Test/random{}_prompt.json".format(random_time), 1,955)
    #     generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
    for random_time in [2]:
        method_name = "random_fewshot/random_{}".format(random_time)
        CodeGen_Simul(api, dataset_name, model_name, method_name,"./prompt_data/random_shot_fewshot/Test/random{}_prompt.json".format(random_time), 934,955)
        generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
    for random_time in [3]:
        method_name = "random_fewshot/random_{}".format(random_time)
        CodeGen_Simul(api, dataset_name, model_name, method_name,"./prompt_data/random_shot_fewshot/Test/random{}_prompt.json".format(random_time), 1,955)
        generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
if __name__ == '__main__':
    pass
    # llama3_gen()
    # codeqwen_gen()
    # gemini_test_explore_refine2_5()
    # deepseek_shot_n()
    gemini_pro_random_fewshot()