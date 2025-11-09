import secrets
import logging
from markupsafe import escape
from flask import Flask, render_template, request, flash
from natasha import Segmenter, NewsNERTagger, NewsEmbedding, MorphVocab, Doc

PAGE_TITLE = "NER analyzer"

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s : %(levelname)s : %(funcName)s : %(lineno)s : %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

app.logger.handlers = logger.handlers
app.logger.setLevel(logger.level)

segmenter = Segmenter()
emb = NewsEmbedding()
ner_tagger = NewsNERTagger(emb)
morph_vocab = MorphVocab()


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':
        source_text = request.form.get('source_text', '')
        if not source_text.strip():
            error_message = 'Empty input. Please enter some text to analyze'
            flash(error_message, 'error')
            logger.error(error_message)
            return render_template('index.html',
                                 title=PAGE_TITLE,
                                 source_text=source_text)
        try:
            text_with_ner = process_ner(source_text)
            return render_template('index.html',
                                 title=PAGE_TITLE,
                                 source_text=source_text,
                                 text_with_ner=text_with_ner)
        except Exception as e:
            error_message = f'Analysis error: {e}'
            flash(error_message, 'error')
            logger.error(error_message)
            return render_template('index.html',
                                 title=PAGE_TITLE,
                                 source_text=source_text)
    return render_template('index.html', title=PAGE_TITLE)


def process_ner(text: str) -> str:
    """Analyzes text and marks named entities"""
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_ner(ner_tagger)
    return markup_ner_text(text, doc)


def markup_ner_text(text: str, doc: Doc) -> str:
    """Marks up named entities in text with HTML tags"""
    spans = doc.spans
    spans_sorted = sorted(spans, key=lambda x: x.start, reverse=True)
    result_text = list(text)
    for span in spans_sorted:
        span.normalize(morph_vocab)
        if span.type in ["PER", "LOC", "ORG"]:
            start, stop = span.start, span.stop
            entity_text = escape(text[start:stop])
            replacement = f'<span class="ner-{span.type.lower()}" title="{span.type}">{entity_text}</span>'
            result_text[start:stop] = replacement
    return ''.join(result_text)


if __name__ == '__main__':
    logger.info("Started...")
    app.run(host="0.0.0.0", port=5000)
