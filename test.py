

from tools import gemini_api,code_qwen,deepseek_v2,deepseek_coder
from Code_Generation import CodeGen_Simul,generated_code_integration
from tools import copy_files

def deep_seek_gen():
    dataset_name = "Val"
    # i = 20
    # model_name = "deepseek_v2"
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(deepseek_v2, dataset_name, model_name, method_name,"./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i),0,955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    # method_name = "self_debug"
    # CodeGen_Simul(deepseek_v2, dataset_name, model_name, method_name,
              # "./prompt_data/self-debug/val_selfdebug_prompt.json",0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(deepseek_v2, dataset_name, model_name, method_name,
    #           "./prompt_data/fewshot_prompt/val_dataset/17_shot_prompt.json",0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 15
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name, doc_number, n_shot)
    # CodeGen_Simul(deepseek_v2, dataset_name, model_name, method_name,
    #               "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,
    #                                                                                 doc_number, n_shot), 35, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


    # model_name = "deepseek_coder"
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(deepseek_coder, dataset_name, model_name, method_name,"./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i),0,955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "self_debug"
    # CodeGen_Simul(deepseek_coder, dataset_name, model_name, method_name,
    #           "./prompt_data/self-debug/val_selfdebug_prompt.json",0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(deepseek_coder, dataset_name, model_name, method_name,
    #           "./prompt_data/fewshot_prompt/val_dataset/17_shot_prompt.json",776, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 15
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name, doc_number, n_shot)
    # # CodeGen_Simul(deepseek_coder, dataset_name, model_name, method_name,
    # #               "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,
    # #                                                                                 doc_number, n_shot), 2,5)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)




    for apis in [(deepseek_coder,"deepseek_coder"),(deepseek_v2,"deepseek_v2")]:
        api = apis[0]
        model_name = apis[1]
    #
    #     #zero-shot
    #     method_name = "direct_prompt"
    #     CodeGen_Simul(api, dataset_name, model_name, method_name, "./prompt_data/direct_prompt/val_0_shot_prompt.json",
    #                   0, 955)
    #     generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

        # refine1
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
        # refine_time = 3
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
        # method_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time,doc_number, n_shot)
        # refile_prompt_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time-1,doc_number, n_shot)
        # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
        #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
        # CodeGen_Simul(api, dataset_name, model_name, method_name,
        #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
        #                                                                    refile_prompt_name,refine_time), 0,
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

        # method_name = "doc_prompt_refine{}/e5_20".format(refine_time)
        # refile_prompt_name = "doc_prompt_refine{}/e5_20".format(refine_time-1)
        # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
        #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
        # CodeGen_Simul(api, dataset_name, model_name, method_name,
        #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
        #                                                                    refile_prompt_name,refine_time), 0,
        #               955)
        # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

        # refine2
        # refine_time = 2
        # refine2
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


def deepseek_shot_n():
    dataset_name = "Test"
    model_name = "deepseek_v2"
    api = deepseek_v2
    for i in [9]:
        method_name = "few_shot/{}_shot".format(i)
        CodeGen_Simul(api, dataset_name, model_name, method_name,
                      "./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i), 410, 680)
        # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

if __name__ == '__main__':
    pass
    # s ="Task Description:\nDevelop a Node.js plugin for Microsoft Word that dynamically generates and executes the Word.run() function based on user input to modify document formatting. Ensure the solution uses JavaScript Word API 1.1 for all interactions with the Word document. Read the input-output samples below to generate code based on user input.\n\nInput Sample:\nInput 1:\nFor the ninth paragraph: change the Outline Level to Level 2, set line spacing to Muliple at 3 lines.\nOutput 1:\n```javascript\nWord.run(async function (context) {\n  // Get the ninth paragraph\n  const paragraphs = context.document.body.paragraphs;\n  paragraphs.load(\"$none\");\n  await context.sync();\n  const ninthParagraph = paragraphs.items[8];\n  // Set the outline level to 2\n  ninthParagraph.outlineLevel = 2;\n  // Set the line spacing to multiple, 3 lines\n  font.load(\"size\");\n  await context.sync();\n  var font = paragraph.font;\n  var fontsize =font.size;\n  ninthParagraph.lineSpacing = 3*fontsize;\n  await context.sync();\n});\n```\n\nInput 2:\nFor the selected part: add a 10 pt space after the paragraph, change the text color to hexadecimal code #FAFAD2.\nOutput 2:\n```javascript\nWord.run(async function (context) {\nvar paragraph = context.document.getSelection().paragraphs.getFirst();\nvar font =context.document.getSelection().font;\nparagraph.spaceAfter = 10;\nfont.color = \"#FAFAD2\";\nawait context.sync();\n});\n```\n\nInput 3:\nFor the tenth paragraph: increase the paragraph spacing after to 1 cm, modify the left indentation to 2 cm.\nOutput 3:\n```javascript\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[9];\nvar font = paragraph.font;\nparagraph.spaceAfter = 28.35;\nparagraph.leftIndent = 2*28.35;\nawait context.sync();\n});\n```\n\nInput 4:\nFor the first paragraph: apply blue color to font, highlight the text in hex code #FF00FF.\nOutput 4:\n```javascript\nWord.run(async function (context) {\nconst paragraph = context.document.body.paragraphs.getFirst();\nvar font = paragraph.font;\nfont.color = \"Blue\";\nfont.highlightColor = \"#FF00FF\";\nawait context.sync();\n});\n```\n\nInput 5:\nFor the eighth paragraph: apply 1cm Hanging, disable italic style, modify line spacing to 1 character, select a wave underline style.\nOutput 5:\n```javascript\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[7];\nvar font = paragraph.font;\n// set the first line to 1cm Hanging\nparagraph.firstLineIndent = -1*28.35;\nfont.italic = false;\n// 1 character ling spacing\nparagraph.load(\"font/size\");\nawait context.sync();\nparagraph.lineSpacing = font.size;\nfont.underline = \"Wave\";\nawait context.sync();\n});\n\n```\nInput 6:\nFor the tenth paragraph: adjust the right indent to -12 pt, Use a Double underline, format Outline level to 'Body Text', set First Line to 1 ch.\nOutput 6:\n```javascript\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[9];\nvar font = paragraph.font;\nparagraph.rightIndent = -12;\nfont.underline = \"Double\";\nparagraph.outlineLevel = 10;\nfont.load(\"size\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.firstLineIndent = 1*fontsize;\nawait context.sync();\n});\n```\n\nInput 7:\nFor the selected part: apply Purple as the font color, have a right indent of 16 points, adjust Hanging to 2 character, bold the text.\nOutput 7:\n```javascript\nWord.run(async function (context) {\nvar paragraph = context.document.getSelection().paragraphs.getFirst();\nvar font =context.document.getSelection().font;\nfont.color = \"Purple\";\nparagraph.rightIndent = 16;\nfont.load(\"size\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.firstLineIndent = -2*fontsize;\nfont.bold = true;\nawait context.sync();\n});\n```\n\nInput 8:\nFor the first paragraph: format the font with the hex color #FFFF00, adjust the text to a 36-point font size.\\nFor the third paragraph: modify line spacing at Double lines, apply 1cm First Line, clear the highlight formatting, set a 2 centimeter right indent.\nOutput 8:\n```javascript\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst firstparagraph = paragraphs.items[0];\nvar firstparagraph_font = firstparagraph.font;\nfirstparagraph_font.color = \"#DEB887\";\nfirstparagraph_font.size = 36;\n\nconst secoundparagraph = paragraphs.items[2];\nvar secoundparagraph_font = secoundparagraph.font;\nsecoundparagraph_font.load(\"size\");\nawait context.sync();\nvar fontsize =secoundparagraph_font.size;\nsecoundparagraph.lineSpacing = 2*fontsize;\nparagraph.firstLineIndent = 1*28.35;\nsecoundparagraph_font.highlightColor = null;\nsecoundparagraph.rightIndent = 2*28.35;\nawait context.sync();\n});\n```\n\nInput 9:\nFor the seventh paragraph: change the Outline Level to Level 2, set line spacing to Muliple at 3 lines.\\nFor the first paragraph: set Hanging to 1 ch, modify a 1.5 cm space after.\nOutput 9:\n```javascript\n// adjust the seventh paragraph\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[6];\nvar font = paragraph.font;\nparagraph.outlineLevel = 2;\nfont.load(\"size\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.lineSpacing = 3*fontsize;\nawait context.sync();\n});\n\n// adjust the first paragraph\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[0];\nvar font = paragraph.font;\nfont.load(\"size\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.firstLineIndent = -1*fontsize;\nparagraph.spaceAfter = 1.5*28.35;\nawait context.sync();\n});\n```\n\nInput 10:\nFor the fifth paragraph: format Outline level to Level 5, increase the paragraph spacing after to 1 cm, apply an underline.\nOutput 10:\n```javascript\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[4];\nvar font = paragraph.font;\nparagraph.outlineLevel = 5;\nparagraph.spaceAfter = 28.35;\nfont.underline = \"Single\";\nawait context.sync();\n});\n```\n\nInput 11:\nFor the selected part: change the text color to Black, change the font size to 8 point.\\nFor the first paragraph: apply the Arial font, modify the Hanging to be 8 points, set its font size to 10.5 points, remove italic formatting.\nOutput 11:\n```javascript\n//adjust the selected part\nWord.run(async function (context) {\nvar paragraph = context.document.getSelection().paragraphs.getFirst();\nvar font =context.document.getSelection().font;\nfont.color = \"Black\";\nfont.size = 8;\nawait context.sync();\n});\n\n// adjust the first paragraph\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[0];\nvar font = paragraph.font;\nfont.name = \"Arial\";\nparagraph.firstLineIndent = -8;\nfont.size = 10.5;\nfont.italic = false;\nawait context.sync();\n});\n```\n\nInput 12:\nFor the first paragraph: modify line spacing at Double lines, apply Level 1 Outline, set Hanging to 1 ch.\nOutput 12:\n```javascript\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[0];\nvar font = paragraph.font;\nfont.load(\"size\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.lineSpacing = 2*fontsize;\nparagraph.outlineLevel = 1;\nparagraph.firstLineIndent = -1*fontsize;\nawait context.sync();\n});\n```\n\nInput 13:\nFor the sixth paragraph: Adjust the line spacing to Single line, apply Outline Level 6, adjust the font size to 16 points.\nOutput 13:\n```javascript\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[5];\nvar font = paragraph.font;\nfont.load(\"size\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.lineSpacing = 1*fontsize;\nparagraph.outlineLevel = 6;\nfont.size = 16;\nawait context.sync();\n});\n```\n\nInput 14:\nFor the third paragraph: increase the paragraph spacing after to 1 cm, set the right indet to 0.5 ch, adjust the text to a 36-point font size.\nOutput 14:\n```javascript\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[2];\nvar font = paragraph.font;\nparagraph.spaceAfter = 28.35;\nfont.load(\"size\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.rightIndent = 0.5*fontsize;\nfont.size = 36;\nawait context.sync();\n});\n```\n\nInput 15:\nFor the selected part: with a 2.5 line space after, select a heavy wave underline style, set a negative 1.5 centimeter left indent.\nOutput 15:\n```javascript\nWord.run(async function (context) {\nvar paragraph = context.document.getSelection().paragraphs.getFirst();\nvar font =context.document.getSelection().font;\nfont.load(\"size\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.spaceAfter = 2.5*fontsize;\nfont.underline = \"WaveHeavy\";\nparagraph.leftIndent = -1.5*28.35;\nawait context.sync();\n});\n```\n\nInput 16:\nFor the third paragraph: make the text italicized, justify the text alignment.\nOutput 16:\n```javascript\nWord.run(async function (context) {\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[2];\nvar font = paragraph.font;\nfont.italic = true;\nparagraph.alignment = \"Justified\";\nawait context.sync();\n});\n```\n\nInput 17:\nFor the selected part: apply center alignment, modify the left indentation to 2 cm, set the right indent to 0.5 ch.\nOutput 17:\n```javascript\nWord.run(async function (context) {\nvar paragraph = context.document.getSelection().paragraphs.getFirst();\nvar font =context.document.getSelection().font;\nparagraph.alignment = \"Centered\";\nparagraph.leftIndent = 2*28.35;\nfont.load(\"size\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.rightIndent = 0.5*fontsize;\nawait context.sync();\n});\n```\nInput 18: For the initial paragraph, please remove the bold formatting and set the outline level to Level 5.\nOutput 18:"
    # print(s)
    # s = "Task Description:\nDevelop a Node.js plugin for Microsoft Word that dynamically generates and executes the Word.run() function based on user input to modify document formatting. Ensure the solution uses JavaScript Word API 1.1 for all interactions with the Word document. Use the provided APIs Knowlegde and API documentations for guidance. Read the API documentation thoroughly to generate the required code according to user input.\n\nAPIs Knowlegde:\nApi documentation apis you may need, each api structure may inclued [api_name], TypeScript and Example code. Detailed instructions are as follows :\n[api_name]: This tag represents the API's name and description. It describes the primary function and purpose of the API.\n```TypeScript```: This tag describes the TypeScript data type of the API. This part may not be present under the respective API if this api is a method.\nExample: provides example code that demonstrates how to use the API.\nEach API is separated by a line of dashes (----------------) to clearly distinguish between different APIs.\n\nApi documentation apis:\n[Word.Font]: Gets the text format of the region. Use this object to get and set the font name, size, color, and other properties.\nExample:\n```javascript\nconst font = range.font;\n```\n----------------\n[Word.Paragraph]: Represents a selection, range, content control, or individual paragraph in the document body.\nExample:\n```javascript\n//Get the first paragraph\nconst paragraph = paragraphs.getFirst();\n```\n----------------\n[paragraphs.items]: Gets the loaded children in this collection. Must be called before reading properties context.sync().\nExample:\n```javascript\nconst paragraphs = context.document.body.paragraphs;\nparagraphs.load(\"$none\");\nawait context.sync();\nconst paragraph = paragraphs.items[1];\n```\n----------------\n[getSelection()]: Gets the current selection of the document. Multiple selections are not supported.\n```TypeScript\nreturn:Word.Range;\n```\nExample:\n```javascript\nconst range = context.document.getSelection();\nvar paragraphs = range.paragraphs;\nvar first_paragraph = range.paragraphs.getFirst();\nvar font = range.font;\n```\n----------------\n[outlineLevel]: Specifies the paragraph's outline level,1-10,10 is body text.\n```TypeScript\noutlineLevel: number;\n```\nExample:\n```javascript\nparagraph.outlineLevel = 6\n```\n----------------\n[lineSpacing]: Specifies the line spacing (in points) for the specified paragraph. In the Word UI, this value should be divided by 12 per time.\n```TypeScript\nlineSpacing: number;\n```\nExample:\n```javascript\nparagraph.lineSpacing = 10;\n```\n----------------\n[spaceAfter]: Specifies the spacing after a paragraph in points.\n```TypeScript\nspaceAfter: number;\n```\nExample:\n```javascript\nparagraph.spaceAfter = 10;\n```\n----------------\n[lines]: 1 line width is 1 font size in points. Read the size of the character as a line spacing\nExample:\n```javascript\n// make spaceAfter as 1 line\nfont.load(\\\"size\\\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.spaceAfter = fontsize;\n```\n----------------\n[spaceBefore]: Specifies the spacing before paragraphs in points.\n```TypeScript\nspaceBefore: number;\n```\nExample:\n```javascript\nparagraph.spaceBefore = 10;\n```\n----------------\n[firstLineIndent]: Specifies the value of the first line or hanging indent in points. Use positive numbers to set the size of the first line indent, and use negative numbers to set the size of the hanging indent.\n```TypeScript\nfirstLineIndent: number;\n```\nExample:\n```javascript\nparagraph.firstLineIndent = 10; // first line 10 point\nparagraph.firstLineIndent = -10; // hanging 10 point\n```\n----------------\n[alignment]: Specify the paragraph alignment. Possible values are \"left\", \"centered\", \"right\", or \"justified\".\nExample:\n```javascript\nparagraph.alignment = \"Centered\";\n```\n----------------\nleftIndent: Specifies the left indent value of the paragraph in points.\n```TypeScript\nleftIndent: number;\n```\nExample:\n```javascript\nparagraph.leftIndent = 10;\n```\n----------------\n[rightIndent]: Specifies the right indent value of the paragraph in points.\n```TypeScript\nrightIndent: number;\n```\nExample:\n```javascript\nparagraph.rightIndent = 10;\n```\n----------------\n[character]: 1 character width is one font size in points. Read the size of the character as the default unit\nExample:\n```javascript\n// make spaceAfter as 1 character\nfont.load(\\\"size\\\");\nawait context.sync();\nvar fontsize =font.size;\nparagraph.spaceAfter = fontsize;\n```\n----------------\n\n[underline]: | \"Mixed\" | \"None\" | \"Hidden\" | \"DotLine\" | \"Single\" | \"Word\" | \"Double\" | \"Thick\" | \"Dotted\" | \"DottedHeavy\" | \"DashLine\" | \"DashLineHeavy\" | \"DashLineLong\" | \"DashLineLongHeavy\" | \"DotDashLine\" | \"DotDashLineHeavy\" | \"TwoDotDashLine\" | \"TwoDotDashLineHeavy\" | \"Wave\" | \"WaveHeavy\" | \"WaveDouble\";Specifies a value that indicates the underline type of the font. \"None\" if the font has no underlines.\n```TypeScript\nunderline: Word.UnderlineType\n```\nExample:\n```javascript\nfont.underline = 'Single';\n```\n----------------\n[centimeter]: 1cm = 28.35 points\nExample:\n```javascript\nlingScaping = 28.35;//make lingScaping 1 cm\n```\n----------------\n[size]: Specifies a value that represents the font size in points.\n```TypeScript\nsize: number;\n```\nExample:\n```javascript\nfont.size = 15;\n```\n----------------\n[points]: Default length unit\nExample:\n```javascript\n// make font size 16 points\nfont.size = 16;\n```\n----------------\n[doubleStrikeThrough]: Specifies a value that indicates whether the font has double strikethrough. True if the font format is set to double strikethrough text, false otherwise.\n```TypeScript\ndoubleStrikeThrough: boolean;\n```\nExample:\n```javascript\nfont.doubleStrikeThrough=true;\n```\n----------------\n[name]: Specifies a value representing the font name.\n```TypeScript\nname: string;\n```\nExample:\n```javascript\nfont.name = 'Arial';\n```\n----------------\n[strikeThrough]: Specifies a value that indicates whether the font has strikethrough. True if the font is formatted as strikethrough text, false otherwise.\n```TypeScript\nstrikeThrough: boolean;\n```\nExample:\n```javascript\nfont.strikeThrough = true;\n```\n----------------\n[highlightColor]: Specify the highlight color. To set it, use a value of the format \"#RRGGBB\" or a color name. To remove the highlight color, set it to null.\n```TypeScript\nhighlightColor: string;\n```\nExample:\n```javascript\nfont.highlightColor = 'red';\n```\n----------------\n[bold]: Specifies a value that indicates whether the font is bold. true if the font format is bold, false otherwise.\n```TypeScript\nbold: boolean;\n```\nExample:\n```javascript\nfont.bold = true;\n```\n----------------\n[italic]: Specifies a value that indicates whether the font is italic. true if the font is italic, false otherwise.\n```TypeScript\nitalic: boolean;\n```\nExample:\n```javascript\nfont.italic = true;\n```\n----------------\n\nUser Input:\nIn the ninth paragraph, adjust the Outline Level to Level 2 and modify the line spacing to Multiple, setting it at 3 lines.\n\nFunction Structure:\n```javascript\nWord.run(async function (context) {\n// Code to be implemented here\nawait context.sync();\n});\n```\n\nOutput: \nComplete the Word.run() above to perform the user's formatting requests. The code should include proper loading of the paragraph properties, application of the desired styles, and any necessary synchronization with the Word document context. Please provide a complete and executable Word.run() function:"
    # print(s)


    dataset_name = "Test"
    model_name = "deepseek_v2"
    method_name = "few_shot/17_shot"
    # CodeGen_Simul(deepseek_v2, dataset_name, model_name, method_name,
    #               "./prompt_data/fewshot_prompt/test_dataset/17_shot_prompt.json",243, 305)

    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
    model_name = "deepseek_coder"
    # CodeGen_Simul(deepseek_coder, dataset_name, model_name, method_name,
    #               "./prompt_data/fewshot_prompt/test_dataset/17_shot_prompt.json",792, 956)

    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


    #self debug
    method_name = "self_debug"

    model_name = "deepseek_v2"
    # CodeGen_Simul(deepseek_v2, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/test_selfdebug_prompt.json",0, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    model_name = "deepseek_coder"
    # CodeGen_Simul(deepseek_coder, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/test_selfdebug_prompt.json", 0, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

    model_name = "gemini_pro"

    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/test_selfdebug_prompt.json",0, 956)
    # generated_code_integration("./dataset/test_data.json",dataset_name,model_name,method_name)



    # Doc Prompt

    i = 20
    dataset_name = "Test"
    method_name = "doc_prompt/e5_{}".format(i)


    # model_name = "deepseek_v2"
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #               "./prompt_data/recall_prompt/test_dataset/e5/e5_RAG_{}_whole.json".format(i),0, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
    #
    # model_name = "deepseek_coder"
    # CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
    #               "./prompt_data/recall_prompt/test_dataset/e5/e5_RAG_{}_whole.json".format(i),0, 956)
    # generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


    # deep_seek_gen()

    deepseek_shot_n()
