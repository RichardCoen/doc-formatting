from tools import gemini_api,read_json,write_dict_to_json,create_directory,gpt35_zz,gpt4_zz,qwen_turbo,read_txt,deepseek_v2
from tools import code_qwen,llama3,copy_files
import re
import os

def WordRun_Get(output):
    # 定义正则表达式模式
    pattern = r'Word\.run\(async function \(context\) {.*?await context\.sync\(\);\n}\);'
    # 使用正则表达式进行匹配
    match = re.search(pattern, output, re.DOTALL)
    catch_code = """.catch(function(error) {
        // send_json({id:item_id,paragraphs_attributions:"Code Hallucination",code_type:code_type,task_name:task_name});
        console.log("Here is an Error: " + error.message);
});"""
    # 提取匹配的内容
    if match:
        word_run_function = match.group()
        return word_run_function[:-1]+catch_code
    else:
        print("Word.run() function not found in the input string.")

def WordRun_Get_GPT4(output):
    if output == None:
        output = "```"

    if "```" in output:
        output_list = output.split("```")
        # print(output_list)
        code = ""
        for op in output_list:
            if "Word.run(async" in op:
                code = op
                break
        # print(code)
        code = code.replace("javascript", "")
        code = code.replace("typescript", "")
        if code:
            return code.replace("Word.run","await Word.run")
        else:
            print("code not found!")
    else:
        return output

def generated_code_integration(original_file,data_name,model_name,method_name):
    result_folder = "./code_generation/{}/{}/{}".format(data_name,model_name,method_name)
    task_name = "{}/{}/{}".format(data_name,model_name,method_name)
    codes_list = []
    atomic_data_list = read_json(original_file,)["data_list"]
    for root, dirs, files in os.walk(result_folder):
        for file in files:
            file_name = os.path.join(root, file)
            data = read_json(file_name)
            init_code = atomic_data_list[int(data["id"])]["init_code"]
            print(data["id"]+" get code successfully!")
            code_result = {"id":data["id"],"code": WordRun_Get_GPT4(data["output"]),"initialized_code":init_code.replace("Word.run","await Word.run")}
            codes_list.append(code_result)

    codes_list = sorted(codes_list, key=lambda x: int(x["id"]))
    save_file = "./code_generation/{}_code.json".format(task_name)
    write_dict_to_json({"description": task_name+" generated code integration",
    "task_name": task_name, "list": codes_list}, save_file)

def CodeGen_Simul(api,data_name,model_name,method_name,file_name,start =0,end = 1):
    task_name = "{}/{}/{}".format(data_name,model_name,method_name)
    save_dir = "./code_generation/{}".format(task_name)
    create_directory(save_dir)
    data_list = read_json(file_name)["data_list"]
    if len(data_list) >= end:
        data_list = data_list[start:end]
    else:
        data_list = data_list[start:]
    for data in data_list:
        prompt = data["prompt"]

        code_generation, input_tokens, output_tokens = api(prompt)
        result = {"id":data["id"],"output":code_generation,"input_tokens":input_tokens, "output_tokens":output_tokens}
        save_path = "./code_generation/{}/{}.json".format(task_name,data["id"])
        print(save_path+" already successful")
        write_dict_to_json(result,save_path)



def codeqwen_gen():
    # codeqwen
    # i = 20
    dataset_name = "Val"
    model_name = "codeqwen"
    api = code_qwen
    #
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
    #               "./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i), 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "self_debug"
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/val_selfdebug_prompt.json", 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
    #               "./prompt_data/fewshot_prompt/val_dataset/17_shot_prompt.json", 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 15
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name, doc_number, n_shot)
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
    #               "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,doc_number, n_shot), 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    #refine 1
    # n_shot = 17
    # doc_number = 15
    # method_name = "RAG_few_shot_refine1/e5_{}/{}_shot".format(doc_number, n_shot)
    # refile_prompt_name = "RAG_few_shot/e5_{}/{}_shot".format(doc_number, n_shot)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "few_shot_refine1/17_shot"
    # refile_prompt_name = "few_shot/17_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine1/e5_20"
    # refile_prompt_name = "doc_prompt/e5_20"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "self_debug_refine1"
    # refile_prompt_name = "self_debug"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    for apis in [(code_qwen,"codeqwen")]:
        api = apis[0]
        model_name = apis[1]
        # refine2
        # refine 3
        refine_time = 3
        n_shot = 17
        doc_number = 15
        method_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time,doc_number, n_shot)
        refile_prompt_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time-1,doc_number, n_shot)
        copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
                   dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
        CodeGen_Simul(api, dataset_name, model_name, method_name,
                      "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
                                                                           refile_prompt_name,refine_time), 0,
                      955)
        generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

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
        #                                                                    refile_prompt_name,refine_time), 6,
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




if __name__ == '__main__':
    pass
    # few-shot
    # for i in [1, 5, 9, 13, 17, 21]:
    #     dataset_name = "Test"
    #     model_name = "gemini_pro"
    #     method_name = "few_shot/{}_shot".format(i)

        #gemini
        # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
        #               "./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i), 0, 956)
        # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    # for i in [ 5, 9, 13, 17, 21]:
    #     dataset_name = "Test"
    #     model_name = "gemini_pro"
    #     method_name = "few_shot/{}_shot".format(i)
    #
    #     #gemini
    #     CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,"./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i),243, 305)
    #     generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

        # model_name = "code_qwen"
        # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,"./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i),243, 305)
        # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


    # RAG
    # for i in [5,10,15,20 ]:
    #     dataset_name = "Test"
    #     model_name = "gemini_pro"

        # method_name = "doc_prompt/bge_{}".format(i)
        # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,"./prompt_data/recall_prompt/test_dataset/bge/bge_RAG_{}_whole.json".format(i), 243, 305)
        # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
        #
        # method_name = "doc_prompt/gte_{}".format(i)
        # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
        #               "./prompt_data/recall_prompt/test_dataset/gte/gte_RAG_{}_whole.json".format(i), 243, 305)
        # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
        #
        # method_name = "doc_prompt/e5_{}".format(i)
        # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
        #               "./prompt_data/recall_prompt/test_dataset/e5/e5_RAG_{}_whole.json".format(i),243, 305)
        # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
        #
        # method_name = "doc_prompt/mxbai_{}".format(i)
        # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
        #               "./prompt_data/recall_prompt/test_dataset/mxbai/MXBAI_RAG_{}_whole.json".format(i), 243, 305)
        # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


    i = 20
    dataset_name = "Test"
    # model_name = "llama3"
    method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(llama3, dataset_name, model_name, method_name,
    #               "./prompt_data/recall_prompt/test_dataset/e5/e5_RAG_{}_whole.json".format(i), 839, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    model_name = "code_qwen"
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
                  # "./prompt_data/recall_prompt/test_dataset/e5/e5_RAG_{}_whole.json".format(i), 1, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


    #directly
    # CodeGen_Simul(gemini_api,"gemini_whole_directly","./prompt_data/direct_prompt/whole_direct.json",0,1)
    # generated_code_integration_GPT4("./code_generation/gemini_whole_directly","./original_data/whole_data.json", "gemini_whole_directly", "gemini_whole_directly")


    # self_debug
    dataset_name = "Test"
    # generated_code_integration("./dataset/test_data.json",dataset_name,model_name,method_name)

    model_name = "llama3"
    method_name = "self_debug"
    # CodeGen_Simul(llama3, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/test_selfdebug_prompt.json",950, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    model_name = "code_qwen"
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
                  # "./prompt_data/self-debug/test_selfdebug_prompt.json",1, 956)

    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    #refine 1

    # refine 1
    # dataset_name = 'Test'
    # refile_prompt_name = "few_shot/13_shot"
    # method_name = "few_shot_refine_1/13_shot"
    #
    # model_name = "gemini_pro"
    # copy_files(src_dir="./code_generation/{}/{}/{}".format(dataset_name,model_name,refile_prompt_name),
    #            dst_dir="code_generation/{}/{}/{}".format(dataset_name,model_name,method_name))
    #
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/Test/{}/{}/refine_1.json".format(model_name, refile_prompt_name), 0, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    # method_name = "doc_prompt_refine/e5_20"
    # refile_prompt_name = "doc_prompt/e5_20"
    # copy_files(src_dir="./code_generation/{}/{}/{}".format(dataset_name,model_name,refile_prompt_name),
    #            dst_dir="code_generation/{}/{}/{}".format(dataset_name,model_name,method_name))
    # CodeGen_Simul(code_qwen, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name, refile_prompt_name), 0, 956)

    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)



    #RAG+Few-shot

    # model_name = "gemini_pro"
    # n_shot = 21
    # embedding_name = "e5"
    # doc_number = 20
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name,doc_number,n_shot)
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #               "./prompt_data/RAG_with_fewshot/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,doc_number, n_shot),40, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


    # model_name = "gemini_pro"
    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 10
    # method_name = "RAG_few_shot_refine/e5_{}/{}_shot".format(doc_number,n_shot)
    # refile_prompt_name = "RAG_few_shot/e5_{}/{}_shot".format(doc_number,n_shot)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name,model_name,refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name,model_name,method_name))
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name, refile_prompt_name), 0, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
    #
    # for doc_number in [5,10,15,20]:
    #     for n_shot in [13,21]:
    #         method_name = "RAG_few_shot_refine/e5_{}/{}_shot".format(doc_number, n_shot)
    #         refile_prompt_name = "RAG_few_shot/e5_{}/{}_shot".format(doc_number, n_shot)
    #         copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #                    dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    #         CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #                       "./prompt_data/refine/{}/{}/refine_1.json".format(model_name, refile_prompt_name), 0, 956)
    #         generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


    codeqwen_gen()