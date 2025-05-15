from django.conf import settings
import torch
from huggingface_hub import InferenceClient
from storage.models import Product
from transformers import pipeline
from transformers import GPT2LMHeadModel, GPT2Tokenizer

classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
chat_model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(chat_model_name)
chat_model = GPT2LMHeadModel.from_pretrained(chat_model_name)

HUGGINGFACE_MODEL_ID = "tiiuae/falcon-rw-1b"
HUGGINGFACE_CLIENT = InferenceClient(
    model=HUGGINGFACE_MODEL_ID,
    token=settings.HUGGINGFACE_TOKEN
)


def get_product_context():
    products = Product.objects.all()[:3]
    context = "\n".join([f"{p.name}: {p.description}" for p in products])
    return context


def basic_interaction(user_input):
    user_input = user_input.lower()

    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"

    if any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"

    if "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How can I help you?"

    return None


def detect_product_query(user_input):
    labels = ["product", "order", "general inquiry", "other"]
    result = classifier(user_input, candidate_labels=labels)

    if result['labels'][0] == 'product' and result['scores'][0] > 0.6:
        return True
    return False


def search_products(user_input):
    query = user_input.lower()
    query_type = "general search"

    if "best selling" in query:
        products = Product.objects.order_by('-sales')[:3]
        query_type = "best-selling"
    elif "on sale" in query or "discount" in query:
        products = Product.objects.filter(is_on_sale=True)[:3]
        query_type = "on sale"
    else:
        products = Product.objects.filter(name__icontains=query)[:3]

    if not products:
        return "Sorry, I couldn't find any products that match your query."

    product_info = "\n\n".join([
        f"Product: {p.name}\n"
        f"Price: ${p.price}\n"
        f"{'✅ On Sale!' if p.is_on_sale else '— Regular Price'}"
        for p in products
    ])

    return f"Here are some {query_type} products I found:\n\n{product_info}"


def chat_with_bot(user_input, conversation_history=None):
    basic_response = basic_interaction(user_input)
    if basic_response:
        return basic_response

    if detect_product_query(user_input):
        return search_products(user_input)

    context = get_product_context()
    conversation_history = conversation_history or []
    conversation_history.append(user_input)

    prompt = f"""
    You are a helpful assistant for an online store selling phones, tablets, and accessories.
    Here is some product information:
    {context}
    Previous conversation: {conversation_history}
    User: {user_input}
    Assistant:
    """

    inputs = tokenizer.encode(prompt, return_tensors='pt')
    attention_mask = torch.ones_like(inputs)

    outputs = chat_model.generate(
        inputs,
        attention_mask=attention_mask,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id
    )

    tokenizer.decode(outputs[0], skip_special_tokens=True)