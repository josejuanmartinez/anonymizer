import logging
import os
from io import BytesIO

from aiohttp import web

from anonymizers.FlairAnonymizer import FlairAnonymizer
from anonymizers.RegexAnonymizer import RegexAnonymizer
from cleanser.Cleanser import Cleanser
from constants import INPUT_DIR, OUTPUT_DIR
from processors.PDFProcessor import PDFProcessor
from sentencizers.SpacySentencizer import SpacySentencizer
from translators.Translator import Translator

routes = web.RouteTableDef()

logging.basicConfig(level=logging.INFO)


@routes.post('/anonymizer/pdf/extract')
async def pdf_extract(request):
    files = {}
    post = await request.post()
    for field_name, field_value in post.items():
        files[field_name] = field_value

    if 'file' not in files:
        raise web.HTTPBadRequest()

    pdf = files['file'].file

    pdf_content = pdf.read()

    pdf_processor = PDFProcessor()

    return web.Response(text=pdf_processor.get_text_from_file(BytesIO(pdf_content)))


@routes.post('/anonymizer/pdf/extract/bulk')
async def pdf_extract_bulk(request):
    pdf_processor = PDFProcessor()
    for filename in os.listdir(INPUT_DIR):
        ext = os.path.splitext(filename)[-1].lower()
        if ext.lower() != '.pdf':
            continue
        text = pdf_processor.get_text_from_filename(os.path.join(INPUT_DIR, filename))
        with open(os.path.join(OUTPUT_DIR, filename + '.extracted.txt'), encoding='utf-8', mode='w') as f2:
            f2.write(text)

    return web.Response(text="{\"status\": \"OK\"}")


@routes.post('/anonymizer/pdf/extract/anonymize')
async def pdf_extract_anonymize(request):
    files = {}
    post = await request.post()
    for field_name, field_value in post.items():
        files[field_name] = field_value

    if 'file' not in files:
        raise web.HTTPBadRequest()

    pdf = files['file'].file

    pdf_content = pdf.read()

    pdf_processor = PDFProcessor()
    cleanser = Cleanser()
    sentencizer = SpacySentencizer()
    flair_anonymizer = FlairAnonymizer()
    regex_anonymizer = RegexAnonymizer()

    text = pdf_processor.get_text_from_file(BytesIO(pdf_content))

    sents = []
    for sent in sentencizer.sentencize(text):
        clean_sent = cleanser.clean(str(sent))
        clean_sent_flair = flair_anonymizer.anonymize(clean_sent)
        clean_sent_flair_regex = regex_anonymizer.anonymize(clean_sent_flair)
        sents.append(clean_sent_flair_regex)

    return web.Response(text="\n".join(sents))


@routes.post('/anonymizer/pdf/extract/anonymize/bulk')
async def pdf_extract_anonymize_bulk(request):
    pdf_processor = PDFProcessor()
    sentencizer = SpacySentencizer()
    flair_anonymizer = FlairAnonymizer()
    regex_anonymizer = RegexAnonymizer()

    for filename in os.listdir(INPUT_DIR):
        ext = os.path.splitext(filename)[-1].lower()
        if ext.lower() != '.pdf':
            continue
        text = pdf_processor.get_text_from_filename(os.path.join(INPUT_DIR, filename))
        sents = []
        for sent in sentencizer.sentencize(text):
            clean_sent = Cleanser.clean(str(sent))
            clean_sent_flair = flair_anonymizer.anonymize(clean_sent)
            clean_sent_flair_regex = regex_anonymizer.anonymize(clean_sent_flair)
            sents.append(clean_sent_flair_regex)
        with open(os.path.join(OUTPUT_DIR, filename + '.extracted.anonymized.txt'), encoding='utf-8', mode='w') as f2:
            f2.write("\n".join(sents))

    return web.Response(text="{\"status\": \"OK\"}")


@routes.get('/anonymizer/pdf/extract/translate/anonymize/bulk')
async def pdf_extract_anonymize_translate_bulk(request):
    host = None
    if 'host' in request.rel_url.query:
        host = request.rel_url.query['host']

    port = None
    if 'port' in request.rel_url.query:
        port = request.rel_url.query['port']

    from_lang = None
    if 'from_lang' in request.rel_url.query:
        from_lang = request.rel_url.query['from_lang']

    to_lang = None
    if 'to_lang' in request.rel_url.query:
        to_lang = request.rel_url.query['to_lang']

    if from_lang is None or to_lang is None:
        return web.HTTPBadRequest()

    logging.info(f"Will translate from {from_lang} to {to_lang}")
    pdf_processor = PDFProcessor()
    sentencizer = SpacySentencizer()
    flair_anonymizer = FlairAnonymizer()
    regex_anonymizer = RegexAnonymizer()
    translator = Translator(from_lang, to_lang, host=host, port=port)

    for filename in os.listdir(INPUT_DIR):
        ext = os.path.splitext(filename)[-1].lower()
        if ext.lower() != '.pdf':
            continue
        text = pdf_processor.get_text_from_filename(os.path.join(INPUT_DIR, filename))
        sents = []
        for sent in sentencizer.sentencize(text):
            trans_sent = translator.translate(str(sent))
            clean_trans_sent = Cleanser.clean(trans_sent)
            clean_trans_sent_flair = flair_anonymizer.anonymize(clean_trans_sent)
            clean_trans_sent_flair_regex = regex_anonymizer.anonymize(clean_trans_sent_flair)
            sents.append(clean_trans_sent_flair_regex)
        with open(os.path.join(OUTPUT_DIR, filename + '.extracted.anonymized.translated_' + from_lang + '_' +
                                           to_lang + '.txt'), encoding='utf-8', mode='w') as f2:
            f2.write("\n".join(sents))

    return web.Response(text="{\"status\": \"OK\"}")


@routes.post('/anonymizer/txt/anonymize')
async def txt_anonymize(request):
    files = {}
    post = await request.post()
    for field_name, field_value in post.items():
        files[field_name] = field_value

    if 'text' not in files:
        raise web.HTTPBadRequest()

    text = files['text']

    sentencizer = SpacySentencizer()
    flair_anonymizer = FlairAnonymizer()
    regex_anonymizer = RegexAnonymizer()

    sents = []
    for sent in sentencizer.sentencize(text):
        clean_sent = Cleanser.clean(str(sent))
        clean_sent_flair = flair_anonymizer.anonymize(clean_sent)
        clean_sent_flair_regex = regex_anonymizer.anonymize(clean_sent_flair)
        sents.append(clean_sent_flair_regex)

    return web.Response(text="\n".join(sents))


@routes.post('/anonymizer/txt/regexanonymize')
async def txt_anonymize(request):
    files = {}
    post = await request.post()
    for field_name, field_value in post.items():
        files[field_name] = field_value

    if 'text' not in files:
        raise web.HTTPBadRequest()

    text = files['text']

    sentencizer = SpacySentencizer()
    regex_anonymizer = RegexAnonymizer()

    sents = []
    for sent in sentencizer.sentencize(text):
        clean_sent = Cleanser.clean(str(sent))
        clean_sent_flair_regex = regex_anonymizer.anonymize(clean_sent)
        sents.append(clean_sent_flair_regex)

    return web.Response(text="\n".join(sents))


@routes.get("/anonymizer/heartbeat")
async def heartbeat(request):
    return web.Response(text="{\"status\": \"OK\"}")
