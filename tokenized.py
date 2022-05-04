from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config, GPT2LMHeadModel,GPT2Tokenizer


# We choose to train a byte-level Byte-pair encoding tokenizer (the same as GPT-2), 
# with the same special tokens as RoBERTa. Let’s arbitrarily pick its size to be 52,000.

# We recommend training a byte-level BPE (rather than let’s say, a WordPiece tokenizer like BERT) 
# because it will start building its vocabulary from an alphabet of single bytes, so all 
# words will be decomposable into tokens (no more <unk> tokens!).
TRAIN_BASE = False
paths = ["python_data.txt"]

if TRAIN_BASE:
    tokenizer = ByteLevelBPETokenizer()

    tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ])

    # Save files to disk
    tokenizer.save_model("tokenizer")


#--------------------------------------------------------------#

# test your model
# from tokenizers.implementations import ByteLevelBPETokenizer
# from tokenizers.processors import BertProcessing

# tokenizer = ByteLevelBPETokenizer(
#     "tokenizer/vocab.json",
#     "tokenizer/merges.txt",
# )

inp = "print('Hello world!')"

# t = tokenizer.encode(inp)

# print(t.ids) # numbers...
# print(t.tokens) # corresponding subword

#-----------------------------------------------------#

#model that we are gonna use it with import

tokenizer = GPT2Tokenizer.from_pretrained('tokenizer')
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

t = tokenizer.encode(inp)
print(t) # [290, 460, 12934, 306, 18633]

print(tokenizer.decode(t)) # print('Hello world!')

