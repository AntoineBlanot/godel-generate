import argparse
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

DEFAULT_INSTRUCTION = 'given a dialog context and related knowledge, you need to response safely based on the knowledge.'


def generate(instruction, knowledge, dialog, model, tokenizer):
    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids.to(model.device), max_length=30, min_length=1, top_p=0.9, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output


def main(args):
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(args.model_name).to(args.device)

    instruction = 'Instruction: {}'.format(args.instruction)
    knowledge = 'Knowledge: {}'.format(args.knowledge)
    dialog = [args.dialog]

    outputs = []
    for _ in tqdm(range(args.n)):
        output = generate(instruction, knowledge, dialog, model, tokenizer)
        outputs.append(output + '\n')
    
    with open(args.out, 'w') as f:
        f.writelines(outputs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, default='microsoft/GODEL-v1_1-base-seq2seq')
    parser.add_argument('--n', type=int, default=10)
    parser.add_argument('--out', type=str, default='outputs.txt')
    parser.add_argument('--device', type=str, default='cpu')
    parser.add_argument('--instruction', type=str, default=DEFAULT_INSTRUCTION)
    parser.add_argument('--knowledge', type=str)
    parser.add_argument('--dialog', type=str)
    args = parser.parse_args()

    main(args)