from tools import qwen_turbo,gemini_api,copy_files,gpt35_zz
from Code_Generation import CodeGen_Simul,generated_code_integration

def gemini_pro_gen():

    # i = 20
    dataset_name = "Val"
    model_name = "gemini_pro"
    api = gemini_api
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,"./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i),0,955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "self_debug"
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
              # "./prompt_data/self-debug/val_selfdebug_prompt.json",291, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #           "./prompt_data/fewshot_prompt/val_dataset/17_shot_prompt.json",836, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 15
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name, doc_number, n_shot)
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #               "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,
    #                                                                                 doc_number, n_shot), 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # zero-shot
    # method_name = "direct_prompt"
    # CodeGen_Simul(api, dataset_name, model_name, method_name, "./prompt_data/direct_prompt/val_0_shot_prompt.json",
    #               0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


    # refine 1
    # method_name = "direct_prompt_refine1"
    # refile_prompt_name = "direct_prompt"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

   #  n_shot = 17
   #  doc_number = 15
   #  method_name = "RAG_few_shot_refine1/e5_{}/{}_shot".format(doc_number, n_shot)
   #  refile_prompt_name = "RAG_few_shot/e5_{}/{}_shot".format(doc_number, n_shot)
   #  copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
   #              dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
   #  CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
   # "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name,model_name, refile_prompt_name), 0, 955)
   #  generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


    # method_name = "few_shot_refine1/17_shot"
    # refile_prompt_name = "few_shot/17_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 1,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "doc_prompt_refine1/e5_20"
    # refile_prompt_name = "doc_prompt/e5_20"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 1,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)




    # refine2

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
    # refine_time = 3
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
    # refile_prompt_name = "few_shot_refine{}/17_shot".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "doc_prompt_refine{}/e5_20".format(refine_time)
    # refile_prompt_name = "doc_prompt_refine{}/e5_20".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    #self_debug refine
    # method_name = "self_debug_refine1"
    # refile_prompt_name = "self_debug"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 5,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


    # refine_time = 2
    # refine_time = 3
    # method_name = "self_debug_refine{}".format(refine_time)
    # refile_prompt_name = "self_debug"
    # last_method_name = "self_debug_refine{}".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

def qwen_turbo_gen():
    #qwen-turbo

    # i = 20
    dataset_name = "Val"
    model_name = "qwen_turbo"
    api = qwen_turbo
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(qwen_turbo, dataset_name, model_name, method_name,"./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i),0,955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "self_debug"
    # CodeGen_Simul(qwen_turbo, dataset_name, model_name, method_name,
    # "./prompt_data/self-debug/val_selfdebug_prompt.json",0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(qwen_turbo, dataset_name, model_name, method_name,
    #           "./prompt_data/fewshot_prompt/val_dataset/17_shot_prompt.json",0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 15
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name, doc_number, n_shot)
    # CodeGen_Simul(qwen_turbo, dataset_name, model_name, method_name,
    #               "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,
    #                                                                                 doc_number, n_shot),0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    # zero-shot
    # method_name = "direct_prompt"
    # CodeGen_Simul(api, dataset_name, model_name, method_name, "./prompt_data/direct_prompt/val_0_shot_prompt.json",
    #               0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


    # refine 1
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
    # CodeGen_Simul(qwen_turbo, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot_refine1/17_shot"
    # refile_prompt_name = "few_shot/17_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(qwen_turbo, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine1/e5_20"
    # refile_prompt_name = "doc_prompt/e5_20"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(qwen_turbo, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "self_debug_refine1"
    # refile_prompt_name = "self_debug"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(qwen_turbo, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)




    # refine2

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
    # n_shot = 17
    # doc_number = 15
    # method_name = "RAG_few_shot_refine2/e5_{}/{}_shot".format(doc_number, n_shot)
    # refile_prompt_name = "RAG_few_shot_refine1/e5_{}/{}_shot".format(doc_number, n_shot)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_2.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot_refine2/17_shot"
    # refile_prompt_name =  "few_shot_refine1/17_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_2.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine2/e5_20"
    # refile_prompt_name = "doc_prompt_refine1/e5_20"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_2.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    #refine 3
    # refine_time = 3
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
    # refile_prompt_name = "few_shot_refine{}/17_shot".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
               # dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "doc_prompt_refine{}/e5_20".format(refine_time)
    # refile_prompt_name = "doc_prompt_refine{}/e5_20".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # refine_time = 2
    # refine_time = 3
    # method_name = "self_debug_refine{}".format(refine_time)
    # refile_prompt_name = "self_debug"
    # last_method_name = "self_debug_refine{}".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

def gemini_pro_test_refine():

    dataset_name = 'Test'
    model_name = "gemini_pro"
    api = gemini_api

    # for i in [17,21]:
    #     method_name = "few_shot_refine1/{}_shot".format(i)
    #     refile_prompt_name = "few_shot/{}_shot".format(i)
    #     copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #                dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    #     CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #                   "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                        refile_prompt_name), 0,
    #                   955)
    #     generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    # refine1

    # method_name = "few_shot_refine1/13_shot"
    # refile_prompt_name = "few_shot/13_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 58,
    #               955)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


def gpt_shot_number_explore():
    dataset_name = "Test"
    model_name = "gpt35"
    api = gpt35_zz
    for i in [5]:
        method_name = "few_shot/{}_shot".format(i)
        CodeGen_Simul(api, dataset_name, model_name, method_name,
                      "./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i), 168, 956)
        generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
    # for i in [ 9, 13, 21]:
    #     method_name = "few_shot/{}_shot".format(i)
    #     CodeGen_Simul(api, dataset_name, model_name, method_name,
    #                   "./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i), 0, 956)
    #     generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


if __name__ == '__main__':
    pass

    #qwen_plus
    # i = 20
    # dataset_name = "Test"
    # model_name = "qwen_plus"
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(qwen_plus, dataset_name, model_name, method_name,
                  # "./prompt_data/recall_prompt/test_dataset/e5/e5_RAG_{}_whole.json".format(i), 784, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    # method_name = "self_debug"
    # CodeGen_Simul(qwen_plus, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/test_selfdebug_prompt.json",838, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(qwen_plus, dataset_name, model_name, method_name,
    #               "./prompt_data/fewshot_prompt/test_dataset/17_shot_prompt.json",0, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    # gemini_pro_gen()
    # qwen_turbo_gen()

    # gemini_pro_test_refine()

    gpt_shot_number_explore()