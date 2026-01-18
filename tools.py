import json
# import google.generativeai as genai
from openai import OpenAI
import requests
import os
import time
from http import HTTPStatus
# import dashscope
import shutil
# from dashscope import Generation
def read_txt(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content+"\n"
    except FileNotFoundError:
        print("File not found.")


def write_dict_to_json(data, json_file_path):
    # 将字典写入 JSON 文件
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def read_json(file_path):
    """
    读取 JSON 文件并返回其内容
    """
    with open(file_path, 'r', encoding='utf-8') as file:
    #     data = json.load(file)
    # return data
        content = file.read()
    content = content.lstrip("\ufeff")
    try:
        return json.loads(content)
    except json.JSONDecodeError as error:
        trimmed = content.lstrip()
        if trimmed.startswith("{{") or trimmed.startswith("{\n{"):
            try:
                return json.loads(trimmed[1:])
            except json.JSONDecodeError:
                pass
        raise ValueError(f"JSON 解析失败: {file_path} ({error})") from error

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Directory '{}' created.".format(directory))
    else:
        print("Directory '{}' already exists.".format(directory))

def copy_files(src_dir, dst_dir):
    # 检查目标目录是否存在，如果不存在则创建
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    # 获取源目录下的所有文件名
    files = os.listdir(src_dir)
    for file in files:
        # 源文件的完整路径
        src_file_path = os.path.join(src_dir, file)
        # 目标文件的完整路径，保持文件名不变
        dst_file_path = os.path.join(dst_dir, file)
        # 如果是文件，则进行复制操作
        if os.path.isfile(src_file_path):
            shutil.copy(src_file_path, dst_file_path)


def gemini_api(prompt):
    import google.generativeai as genai
    generation_config = {"temperature": 0.0, "top_p": 0.0, "top_k": None}
    api_key = ''
    genai.configure(api_key=api_key, transport='rest')
    model = genai.GenerativeModel('models/gemini-pro', generation_config = generation_config)
    processed_flag = False
    while not processed_flag:
        try:
            response = model.generate_content(prompt)
            input_tokens = model.count_tokens(prompt).total_tokens
            # print(response)
            output_tokens = model.count_tokens(response.text).total_tokens
            return response.text,input_tokens,output_tokens
        except Exception as e:
            processed_flag = False
            print(e)
            print('Error! Sleep for 5s.')
            time.sleep(5)

def gpt35_zz(prompt,tempetature=0.0):
    from openai import OpenAI
    client = OpenAI(
        api_key="",
        base_url=''
    )
    processed_flag = False
    while not processed_flag:
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                temperature=tempetature,
                top_p=0.0,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )
            # print(completion.usage)
            input_tokens = completion.usage.prompt_tokens
            output_tokens = completion.usage.completion_tokens
            response = completion.choices[0].message.content
            return  response,input_tokens,output_tokens
        except Exception as e:
            processed_flag = False
            print(e)
            print('Error! Sleep for 5s.')
            time.sleep(5)

def gpt4_zz(prompt,tempetature=0.0):
    api_key = os.getenv("OPENAI_API_KEY", "")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    base_url = base_url.strip().strip('"').strip("'")
    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY environment variable.")
    if not base_url.startswith(("http://", "https://")):
        raise ValueError(f"OPENAI_BASE_URL must include http:// or https:// (got: {base_url!r})")
    client = OpenAI(
    #     api_key="",
    #     base_url = ''
        api_key = api_key,
        base_url = base_url
    )
    processed_flag = False
    while not processed_flag:
        try:
            completion = client.chat.completions.create(
                # model="gpt-4-turbo-2024-04-09",
                model="openai/gpt-4o",
                temperature=tempetature,
                top_p=0.0,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )
            input_tokens = completion.usage.prompt_tokens
            output_tokens = completion.usage.completion_tokens
            response = completion.choices[0].message.content
            return response, input_tokens, output_tokens
        except Exception as e:
            processed_flag = False
            print(e)
            print('Error! Sleep')


def gpt4_preview(prompt,tempetature=0.0):
    from openai import OpenAI
    client = OpenAI(
        api_key="",
        base_url = ''
    )
    processed_flag = False
    while not processed_flag:
        try:
            completion = client.chat.completions.create(
                # model="gpt-4-1106-preview",
                model="gpt-4o",
                temperature=tempetature,
                top_p=0.0,
                messages=[
                    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
                    {"role": "user", "content": prompt},
                ],
            )
            input_tokens = completion.usage.prompt_tokens
            output_tokens = completion.usage.completion_tokens
            response = completion.choices[0].message.content
            return response, input_tokens, output_tokens
        except Exception as e:
            processed_flag = False
            print(e)
            print('Error! Sleep')

def qwen_turbo(prompt):
    import dashscope
    dashscope.api_key = ""
    processed_flag = False
    while not processed_flag:
        try:
            response = dashscope.Generation.call(
                model=dashscope.Generation.Models.qwen_turbo,
                prompt=prompt,
                temperature = 0.0,
                repetition_penalty = 1,
                top_p = 0.0001,
                top_k = None,
                seed=1234,
            )
            if response.status_code == HTTPStatus.OK:
                # print(response.output)  # The output text
                # print(response.usage)  # The usage information
                input_tokens = response.usage.input_tokens
                output_tokens = response.usage.output_tokens
                response = response.output.text
                return response, input_tokens, output_tokens

            else:
                print(response.code)  # The error code.
                print(response.message)  # The error message.
        except Exception as e:
            processed_flag = False
            print(e)
            print('Error! Sleep for 5s.')
            time.sleep(5)

def code_qwen(prompt):
    # 定义服务器的地址和端口号
    server_address = ""
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
        return generated_response,input_tokens,output_tokens
    else:
        print("Failed to generate response. Status code:", response.status_code)


def llama3(prompt):
    data = {'prompt': prompt}
    response = requests.post('', json=data)
    # 获取服务器返回的响应
    if response.status_code == 200:
        response_data = response.json()
        generated_response = response_data['response']
        input_tokens = response_data['input_tokens']
        output_tokens = response_data['output_tokens']
        return generated_response, input_tokens, output_tokens
    else:
        print("Failed to generate response. Status code:", response.status_code)


def deepseek_v2(prompt):
    # for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
    client = OpenAI(api_key="", base_url="https://api.deepseek.com")
    completion = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        max_tokens=512,
        temperature=0.0,
        stream=False
    )
    # print(response.choices[0].message.content)
    input_tokens = completion.usage.prompt_tokens
    output_tokens = completion.usage.completion_tokens
    response = completion.choices[0].message.content
    return response, input_tokens, output_tokens

def deepseek_v2_l(prompt):
    # for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
    client = OpenAI(api_key="", base_url="https://api.deepseek.com")
    completion = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        max_tokens=512,
        temperature=0.0,
        stream=False
    )
    # print(response.choices[0].message.content)
    input_tokens = completion.usage.prompt_tokens
    output_tokens = completion.usage.completion_tokens
    response = completion.choices[0].message.content
    return response, input_tokens, output_tokens

def deepseek_coder(prompt):
    # for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
    client = OpenAI(api_key="", base_url="https://api.deepseek.com")
    completion = client.chat.completions.create(
        model="deepseek-coder",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        max_tokens=512,
        temperature=0.0,
        stream=False
    )
    # print(response.choices[0].message.content)
    input_tokens = completion.usage.prompt_tokens
    output_tokens = completion.usage.completion_tokens
    response = completion.choices[0].message.content
    return response, input_tokens, output_tokens



def qwen2(prompt):
    # 定义服务器的地址和端口号
    server_address = ""
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

if __name__ == '__main__':
    pass
    # gpt35_zz("tell me a joke")
    # print(qwen_turbo("tell me a joke"))
    # print(gpt4_zz("tell me a joke"))
    # prompt = "Task Description:\nDevelop a Node.js plugin for Microsoft Word that dynamically generates and executes the Word.run() function based on user input to modify document formatting. Ensure the solution uses JavaScript Word API 1.1 for all interactions with the Word document. Use the provided APIs Knowlegde and API documentations for guidance. Read the API documentation thoroughly to generate the required code according to user input.\n\nAPIs Knowlegde:\nApi documentation apis you may need, each api structure may inclued [api_name], TypeScript and Example code. Detailed instructions are as follows :\n[api_name]: This tag represents the API's name and description. It describes the primary function and purpose of the API.\n```TypeScript```: This tag describes the TypeScript data type of the API. This part may not be present under the respective API if this api is a method.\nExample: provides example code that demonstrates how to use the API.\nEach API is separated by a line of dashes (----------------) to clearly distinguish between different APIs.\n\nApi documentation apis:\n[Word.Font]: Gets the text format of the region. Use this object to get and set the font name, size, color, and other properties.\nExample:\n```javascript\nconst font = range.font;\n```\n----------------\n[Word.Paragraph]: Represents a selection, range, content control, or individual paragraph in the document body.\nExample:\n```javascript\n//Get the first paragraph\nconst paragraph = paragraphs.getFirst();\n```\n----------------\n[paragraphs.items]: Gets the loaded children in this collection. Must be called before reading properties context.sync().\nExample:\n```javascript\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[1];\n```\n----------------\n[getSelection()]: Gets the current selection of the document. Multiple selections are not supported.\n```TypeScript\nreturn:Word.Range;\n```\nExample:\n```javascript\nconst range = context.document.getSelection();\nvar paragraphs = range.paragraphs;\nvar first_paragraph = range.paragraphs.getFirst();\nvar font = range.font;\n```\n----------------\n[outlineLevel]: Specifies the paragraph's outline level,1-10,10 is body text.\n```TypeScript\noutlineLevel: number;\n```\nExample:\n```javascript\nparagraph.outlineLevel = 6\n```\n----------------\n[lineSpacing]: Specifies the line spacing (in points) for the specified paragraph. In the Word UI, this value should be divided by 12 per time.\n```TypeScript\nlineSpacing: number;\n```\nExample:\n```javascript\nparagraph.lineSpacing = 10;\n```\n----------------\n[character]: 1 character width is one font size in points. Read the size of the character as the default unit\nExample:\n```javascript\n// make spaceAfter as 1 character\nfont.load(\\\"size\\\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.spaceAfter = fontsize;\n```\n----------------\n\n[lines]: 1 line width is 1 font size in points. Read the size of the character as a line spacing\nExample:\n```javascript\n// make spaceAfter as 1 line\nfont.load(\\\"size\\\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.spaceAfter = fontsize;\n```\n----------------\n[firstLineIndent]: Specifies the value of the first line or hanging indent in points. Use positive numbers to set the size of the first line indent, and use negative numbers to set the size of the hanging indent.\n```TypeScript\nfirstLineIndent: number;\n```\nExample:\n```javascript\nparagraph.firstLineIndent = 10; // first line 10 point\nparagraph.firstLineIndent = -10; // hanging 10 point\n```\n----------------\n[spaceBefore]: Specifies the spacing before paragraphs in points.\n```TypeScript\nspaceBefore: number;\n```\nExample:\n```javascript\nparagraph.spaceBefore = 10;\n```\n----------------\n[spaceAfter]: Specifies the spacing after a paragraph in points.\n```TypeScript\nspaceAfter: number;\n```\nExample:\n```javascript\nparagraph.spaceAfter = 10;\n```\n----------------\n[alignment]: Specify the paragraph alignment. Possible values are \"left\", \"centered\", \"right\", or \"justified\".\nExample:\n```javascript\nparagraph.alignment = \"Centered\";\n```\n----------------\nleftIndent: Specifies the left indent value of the paragraph in points.\n```TypeScript\nleftIndent: number;\n```\nExample:\n```javascript\nparagraph.leftIndent = 10;\n```\n----------------\n[rightIndent]: Specifies the right indent value of the paragraph in points.\n```TypeScript\nrightIndent: number;\n```\nExample:\n```javascript\nparagraph.rightIndent = 10;\n```\n----------------\n[centimeter]: 1cm = 28.35 points\nExample:\n```javascript\nlingScaping = 28.35;//make lingScaping 1 cm\n```\n----------------\n[points]: Default length unit\nExample:\n```javascript\n// make font size 16 points\nfont.size = 16;\n```\n----------------\n[underline]: | \"Mixed\" | \"None\" | \"Hidden\" | \"DotLine\" | \"Single\" | \"Word\" | \"Double\" | \"Thick\" | \"Dotted\" | \"DottedHeavy\" | \"DashLine\" | \"DashLineHeavy\" | \"DashLineLong\" | \"DashLineLongHeavy\" | \"DotDashLine\" | \"DotDashLineHeavy\" | \"TwoDotDashLine\" | \"TwoDotDashLineHeavy\" | \"Wave\" | \"WaveHeavy\" | \"WaveDouble\";Specifies a value that indicates the underline type of the font. \"None\" if the font has no underlines.\n```TypeScript\nunderline: Word.UnderlineType\n```\nExample:\n```javascript\nfont.underline = 'Single';\n```\n----------------\n[size]: Specifies a value that represents the font size in points.\n```TypeScript\nsize: number;\n```\nExample:\n```javascript\nfont.size = 15;\n```\n----------------\n[bold]: Specifies a value that indicates whether the font is bold. true if the font format is bold, false otherwise.\n```TypeScript\nbold: boolean;\n```\nExample:\n```javascript\nfont.bold = true;\n```\n----------------\n[highlightColor]: Specify the highlight color. To set it, use a value of the format \"#RRGGBB\" or a color name. To remove the highlight color, set it to null.\n```TypeScript\nhighlightColor: string;\n```\nExample:\n```javascript\nfont.highlightColor = 'red';\n```\n----------------\n[color]: Specifies the color of the specified font. Values can be provided in the format \"#RRGGBB\" or as color names.\n```TypeScript\ncolor: boolean;\n```\nExample:\n```javascript\nexample:font.color = 'red';\n```\n----------------\n[name]: Specifies a value representing the font name.\n```TypeScript\nname: string;\n```\nExample:\n```javascript\nfont.name = 'Arial';\n```\n----------------\n[strikeThrough]: Specifies a value that indicates whether the font has strikethrough. True if the font is formatted as strikethrough text, false otherwise.\n```TypeScript\nstrikeThrough: boolean;\n```\nExample:\n```javascript\nfont.strikeThrough = true;\n```\n----------------\n[italic]: Specifies a value that indicates whether the font is italic. true if the font is italic, false otherwise.\n```TypeScript\nitalic: boolean;\n```\nExample:\n```javascript\nfont.italic = true;\n```\n----------------\n\nUser Input:\nPlease adjust the formatting for the seventh paragraph by adding a 0.5 line space preceding it, and set it to a Level 1 Outline.\n\nFunction Structure:\n```javascript\nWord.run(async function (context) {\n// Code to be implemented here\nawait context.sync();\n});\n```\n\nOutput: \nComplete the Word.run() above to perform the user's formatting requests. The code should include proper loading of the paragraph properties, application of the desired styles, and any necessary synchronization with the Word document context. Please provide a complete and executable Word.run() function:"

    # prompt = "Task Description:\nDevelop a Node.js plugin for Microsoft Word that dynamically generates and executes the Word.run() function based on user input to modify document formatting. Ensure the solution uses JavaScript Word API 1.1 for all interactions with the Word document. Use the provided APIs Knowlegde and API documentations for guidance. Read the API documentation thoroughly to generate the required code according to user input.\n\nAPIs Knowlegde:\nApi documentation apis you may need, each api structure may inclued [api_name], TypeScript and Example code. Detailed instructions are as follows :\n[api_name]: This tag represents the API's name and description. It describes the primary function and purpose of the API.\n```TypeScript```: This tag describes the TypeScript data type of the API. This part may not be present under the respective API if this api is a method.\nExample: provides example code that demonstrates how to use the API.\nEach API is separated by a line of dashes (----------------) to clearly distinguish between different APIs.\n\nApi documentation apis:\n[Word.Font]: Gets the text format of the region. Use this object to get and set the font name, size, color, and other properties.\nExample:\n```javascript\nconst font = range.font;\n```\n----------------\n[Word.Paragraph]: Represents a selection, range, content control, or individual paragraph in the document body.\nExample:\n```javascript\n//Get the first paragraph\nconst paragraph = paragraphs.getFirst();\n```\n----------------\n[paragraphs.items]: Gets the loaded children in this collection. Must be called before reading properties context.sync().\nExample:\n```javascript\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[1];\n```\n----------------\n[getSelection()]: Gets the current selection of the document. Multiple selections are not supported.\n```TypeScript\nreturn:Word.Range;\n```\nExample:\n```javascript\nconst range = context.document.getSelection();\nvar paragraphs = range.paragraphs;\nvar first_paragraph = range.paragraphs.getFirst();\nvar font = range.font;\n```\n----------------\n[outlineLevel]: Specifies the paragraph's outline level,1-10,10 is body text.\n```TypeScript\noutlineLevel: number;\n```\nExample:\n```javascript\nparagraph.outlineLevel = 6\n```\n----------------\n[color]: Specifies the color of the specified font. Values can be provided in the format \"#RRGGBB\" or as color names.\n```TypeScript\ncolor: boolean;\n```\nExample:\n```javascript\nexample:font.color = 'red';\n```\n----------------\n[character]: 1 character width is one font size in points. Read the size of the character as the default unit\nExample:\n```javascript\n// make spaceAfter as 1 character\nfont.load(\\\"size\\\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.spaceAfter = fontsize;\n```\n----------------\n\n[highlightColor]: Specify the highlight color. To set it, use a value of the format \"#RRGGBB\" or a color name. To remove the highlight color, set it to null.\n```TypeScript\nhighlightColor: string;\n```\nExample:\n```javascript\nfont.highlightColor = 'red';\n```\n----------------\n[lines]: 1 line width is 1 font size in points. Read the size of the character as a line spacing\nExample:\n```javascript\n// make spaceAfter as 1 line\nfont.load(\\\"size\\\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.spaceAfter = fontsize;\n```\n----------------\n[lineSpacing]: Specifies the line spacing (in points) for the specified paragraph. In the Word UI, this value should be divided by 12 per time.\n```TypeScript\nlineSpacing: number;\n```\nExample:\n```javascript\nparagraph.lineSpacing = 10;\n```\n----------------\n[size]: Specifies a value that represents the font size in points.\n```TypeScript\nsize: number;\n```\nExample:\n```javascript\nfont.size = 15;\n```\n----------------\n[firstLineIndent]: Specifies the value of the first line or hanging indent in points. Use positive numbers to set the size of the first line indent, and use negative numbers to set the size of the hanging indent.\n```TypeScript\nfirstLineIndent: number;\n```\nExample:\n```javascript\nparagraph.firstLineIndent = 10; // first line 10 point\nparagraph.firstLineIndent = -10; // hanging 10 point\n```\n----------------\n[alignment]: Specify the paragraph alignment. Possible values are \"left\", \"centered\", \"right\", or \"justified\".\nExample:\n```javascript\nparagraph.alignment = \"Centered\";\n```\n----------------\n[name]: Specifies a value representing the font name.\n```TypeScript\nname: string;\n```\nExample:\n```javascript\nfont.name = 'Arial';\n```\n----------------\n[bold]: Specifies a value that indicates whether the font is bold. true if the font format is bold, false otherwise.\n```TypeScript\nbold: boolean;\n```\nExample:\n```javascript\nfont.bold = true;\n```\n----------------\n[underline]: | \"Mixed\" | \"None\" | \"Hidden\" | \"DotLine\" | \"Single\" | \"Word\" | \"Double\" | \"Thick\" | \"Dotted\" | \"DottedHeavy\" | \"DashLine\" | \"DashLineHeavy\" | \"DashLineLong\" | \"DashLineLongHeavy\" | \"DotDashLine\" | \"DotDashLineHeavy\" | \"TwoDotDashLine\" | \"TwoDotDashLineHeavy\" | \"Wave\" | \"WaveHeavy\" | \"WaveDouble\";Specifies a value that indicates the underline type of the font. \"None\" if the font has no underlines.\n```TypeScript\nunderline: Word.UnderlineType\n```\nExample:\n```javascript\nfont.underline = 'Single';\n```\n----------------\n[points]: Default length unit\nExample:\n```javascript\n// make font size 16 points\nfont.size = 16;\n```\n----------------\nleftIndent: Specifies the left indent value of the paragraph in points.\n```TypeScript\nleftIndent: number;\n```\nExample:\n```javascript\nparagraph.leftIndent = 10;\n```\n----------------\n[spaceAfter]: Specifies the spacing after a paragraph in points.\n```TypeScript\nspaceAfter: number;\n```\nExample:\n```javascript\nparagraph.spaceAfter = 10;\n```\n----------------\n[italic]: Specifies a value that indicates whether the font is italic. true if the font is italic, false otherwise.\n```TypeScript\nitalic: boolean;\n```\nExample:\n```javascript\nfont.italic = true;\n```\n----------------\n[subscript]: Specifies a value indicating whether the font is subscripted. true if the font format is subscript, false otherwise.\n```TypeScript\nsubscript: boolean;\n```\nExample:\n```javascript\nfont.subscript = true;\n```\n----------------\n[centimeter]: 1cm = 28.35 points\nExample:\n```javascript\nlingScaping = 28.35;//make lingScaping 1 cm\n```\n----------------\n[rightIndent]: Specifies the right indent value of the paragraph in points.\n```TypeScript\nrightIndent: number;\n```\nExample:\n```javascript\nparagraph.rightIndent = 10;\n```\n----------------\n[spaceBefore]: Specifies the spacing before paragraphs in points.\n```TypeScript\nspaceBefore: number;\n```\nExample:\n```javascript\nparagraph.spaceBefore = 10;\n```\n----------------\n\nUser Input:\nPlease format the selected section by changing the font color to Indigo and setting the outline level as 'Body Text'.\n\nFunction Structure:\n```javascript\nWord.run(async function (context) {\n// Code to be implemented here\nawait context.sync();\n});\n```\n\nOutput: \nComplete the Word.run() above to perform the user's formatting requests. The code should include proper loading of the paragraph properties, application of the desired styles, and any necessary synchronization with the Word document context. Please provide a complete and executable Word.run() function:"
    # code, input_count,output_count = qwen2(prompt)
    # print((input_count,output_count))

