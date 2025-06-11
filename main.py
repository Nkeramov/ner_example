from natasha import (
    Segmenter,
    NewsNERTagger,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    MorphVocab,
    Doc)
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    original_text = ""
    text_with_ner = ""
    if request.method == "POST":
        original_text = request.form["text"]
        text_with_ner = analyze_text(original_text)
    return render_template("index.html", title='NER analyse example',
                                original=original_text,
                                text_with_ner=text_with_ner)


def analyze_text(text: str) -> str:
    segmenter = Segmenter()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)
    ner_tagger = NewsNERTagger(emb)
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)
    morph_vocab = MorphVocab()
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
        # print(f"{token.text}  : {token.lemma}")
    # print(doc.spans)
    text_with_ner_info = text
    for span in doc.spans:
        span.normalize(morph_vocab)
        if span.type == "PER":
            text_with_ner_info = text_with_ner_info.replace(span.text, f'<span class=\"per\">{span.text}</span>')
        elif span.type == "LOC":
            text_with_ner_info = text_with_ner_info.replace(span.text, f'<span class=\"loc\">{span.text}</span>')
        elif span.type == "ORG":
            text_with_ner_info = text_with_ner_info.replace(span.text, f'<span class=\"org\">{span.text}</span>')
    return text_with_ner_info


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
