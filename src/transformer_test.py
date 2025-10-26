from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("I've been waiting for a huggingface course my whole life"))


classifier = pipeline("zero-shot-classification")
print(
    classifier(
        """This is s course about the transformer library""",
        candidate_labels=["education", "politics", "business"],
    )
)

generator = pipeline("text-generation")
print(
    generator(
        "In this course, we will teach you how to",
    )
)
