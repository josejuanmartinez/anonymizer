from io import BytesIO

from aiohttp import web

# from anonymizers.FlairAnonymizer import FlairAnonymizer
from anonymizers.FlairAnonymizer import FlairAnonymizer
from anonymizers.RegexAnonymizer import RegexAnonymizer
from cleanser.Cleanser import Cleanser
from processors.PDFProcessor import PDFProcessor
from sentencizers.SpacySentencizer import SpacySentencizer

routes = web.RouteTableDef()


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

    return web.Response(text=pdf_processor.get_text(BytesIO(pdf_content)))


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

    text = pdf_processor.get_text(BytesIO(pdf_content))

    sents = []
    for sent in sentencizer.sentencize(text):
        clean_sent = cleanser.clean(str(sent))
        clean_sent_flair = flair_anonymizer.anonymize(clean_sent)
        clean_sent_flair_regex = regex_anonymizer.anonymize(clean_sent_flair)
        sents.append(clean_sent_flair_regex)

    return web.Response(text="\n".join(sents))


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
