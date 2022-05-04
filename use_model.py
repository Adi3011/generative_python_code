from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config, GPT2LMHeadModel,GPT2Tokenizer, DataCollatorForLanguageModeling

paths = ['python_data.txt']
tokenizer = GPT2Tokenizer.from_pretrained('tokenizer')
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

config = GPT2Config(
    vocab_size = tokenizer.vocab_size,
    bos_token = tokenizer.bos_token_id,
    eos_token = tokenizer.eos_token_id
)

model = GPT2LMHeadModel.from_pretrained("GPyT").to("cuda")

def encode_newlines(inp):
    return inp.replace("\n","<N>")

def decode_newlines(inp):
    return inp.replace("<N>","\n")



while True:
    inp = input(">>> ")
    inp = inp.replace('\n','<N>')
    input_ids = tokenizer.encode(inp, return_tensors ="pt").to("cuda")
    beam_output = model.generate(
        input_ids,
        max_length = 512,
        num_beams = 10, 
        temperature = 0.7,
        no_repeat_ngram_size = 5,
        num_returned_sequences = 3,
        return_dict_in_generate = True,
        output_scores= True
    ) # these parameters basically helps to generate variety of tokens from the token reached or selected

    # for beam in beam_output:
    #     out = tokenizer.decode(beam)
    #     fout = out.replace("<N>", "\n")

    #     print(str(fout))

    for beam in beam_output:
        print(beam)

    for seqscore in beam_output['sequences_scores']:
        print(seqscore)    

 
    for seq in beam_output['sequences']:
        print(decode_newlines(tokenizer.decode(seq)))    

