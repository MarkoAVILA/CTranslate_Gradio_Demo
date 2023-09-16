import json
import ctranslate2
import transformers
import gradio as gr
import fire 

def languages_to_code(langues):
    src_lang, tgt_lang = langues.split('-')
    dict_langues_code = json.load(open("langues_200.json"))
    del dict_langues_code['Language']
    src_code_language = dict_langues_code[src_lang+' ']
    tgt_code_language = dict_langues_code[tgt_lang+' ']
    return src_code_language, tgt_code_language


class Gradio_Translate:
    def __init__(self, model_ct2="nllb-200-distilled-600M-ct2", model_base="facebook/nllb-200-distilled-600M", lang="Sapnish-French"):
        self.model_ct2 = model_ct2
        self.model_base = model_base
        self.src_lang, self.tgt_lang = lang.split('-')
        self.translator = ctranslate2.Translator(model_ct2)
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_base, src_lang=self.src_lang)
        
    def inference(self, text):
        source = self.tokenizer.convert_ids_to_tokens(self.tokenizer.encode(text))
        target_prefix = [self.tgt_lang]
        results = self.translator.translate_batch([source], target_prefix=[target_prefix])
        target = results[0].hypotheses[0][1:]
        return self.tokenizer.decode(self.tokenizer.convert_tokens_to_ids(target))

    def translation(self,texts):
        texts_ = texts.split("\n")
        l = [self.inference(text) for text in texts_]
        return "\n".join(l)

    def demo(self):
        # textbox0 = gr.Textbox(label="Enter the languages that you want to translate:", placeholder="es_Latn->fra_Latn")
        textbox1 = gr.Textbox(label="Enter your phrase for translate it please:", placeholder="Mi nombre es  Marko", lines=5)
        textbox2 = gr.Textbox(label="Translating...:", placeholder="Je m'apelle Marko", lines=5)

        title = "Ask to Marko Translate"
        description = """<p align="center">
        The NLLB model from Meta AI was trained to translate 200 languages . Ask Mark Translate!
        <img src="https://eu-images.contentstack.com/v3/assets/blt6b0f74e5591baa03/blt7b0e00d62e2f7c8f/63197b5f4966f91f58465f23/643.jpg?width=850&auto=webp&quality=95&format=jpg&disable=upscale" width=250px>
        </p>
        """
        article = "Check out [https://github.com/facebookresearch/fairseq/tree/nllb/]"

        gr.Interface(fn=self.translation, inputs=[textbox1], 
        outputs=textbox2,
        title=title, 
        description=description, 
        article=article
        ).launch(share=True)

if __name__=='__main__':
    fire.Fire(Gradio_Translate)

# python3 gradio_nllb.py demo --lang "Spanish-French" 