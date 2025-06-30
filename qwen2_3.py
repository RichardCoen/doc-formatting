from tools import copy_files,qwen2
from Code_Generation import CodeGen_Simul,generated_code_integration
import requests
def qwen2_rsh(prompt):
    # 定义服务器的地址和端口号
    server_address = "http://192.168.200.218:8028"
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


def qwen2_another_fewshot():
    api = qwen2_rsh
    #random_time
    dataset_name = "Test"
    model_name = 'Qwen2'
    for shot_number in [5,13,17]:
        method_name = "another_fewshot/{}_shot/".format(shot_number)
        CodeGen_Simul(api, dataset_name, model_name, method_name,"./prompt_data/another_fewshot/Test/{}shot_another_prompt.json".format(shot_number), 0,955)
        generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


if __name__ == '__main__':
    pass
    # tes_gen()
    # val_gen()
    qwen2_another_fewshot()