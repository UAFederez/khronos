from jinja2 import Template
from pathlib import Path
import os

def read_faqs_file():
    faqFile = open('faqs.txt')
    text    = faqFile.read()

    faqsTxt = text.split('|')

    faqs = []
    
    for faq in faqsTxt:
        faqText  = faq.split("?")
        question = faqText[0].strip('\n') + "?"
        answer   = faqText[1].strip('\n')

        faqs.append((question, answer))

    return faqs

def read_pipeline_file():
    inFile = open('pipeline.txt')
    text    = inFile.read()

    pipeLinesTxt = text.split('%')

    pipe = []
    
    for pipeLine in pipeLinesTxt:
        pipeLineText  = pipeLine.split("$")
        question = pipeLineText[0].strip('\n')
        answer   = pipeLineText[1].strip('\n')

        answer  = "<strong>" + answer;
        firstSentence = answer.index('.');

        answer  = answer[:firstSentence + 1] + "</strong><br/>" + answer[firstSentence + 1:]

        pipe.append((question, answer))

    return pipe

pages = [ 'tmp_index.html', 'tmp_about.html', 'tmp_faq.html', 'tmp_perfbench.html',
          'tmp_pipeline.html', 'tmp_glut.html', 'tmp_news.html', 'tmp_contact.html']

navTmp    = open('templates/nav_template.html').read()
headerTmp = open('templates/header_template.html').read()
footerTmp = open('templates/footer_template.html').read()

faqs = read_faqs_file()
pipe = read_pipeline_file()

for page in pages:
    print(f"{page}...")
    pageSource = open(page)
    template = Template(pageSource.read())

    if page == 'tmp_faq.html':
        s = template.render(header_tmp = headerTmp, 
                            nav_tmp    = navTmp, 
                            footer_tmp = footerTmp, 
                            questions  = faqs)
    elif page == 'tmp_pipeline.html':
        s = template.render(header_tmp = headerTmp, 
                            nav_tmp    = navTmp, 
                            footer_tmp = footerTmp, 
                            pipeline   = pipe)
    elif page == "tmp_glut.html":
        files   = [ img for img in os.listdir(Path.cwd() / "../img/lightbox/") if '.' in img]
        images  = [ ]
        fileDir = "img/lightbox/"


        files.sort()

        descriptions = [
                "Open Inventor for Medicine", 
                "Open Inventor for Engineering", 
                "Open Inventor for Mining & Oil",
                "Open Inventor for Cloud Computing",
                "Open Scene Graph for Architecture", 
                "Open Scene Graph for Transportation", 
                "Open Scene Graph for Construction",
                "Open Scene Graph for Flight Simulation",
                "Quesa 3D Demo for Geometry",
        ]

        for img in files:
            filename  = os.path.splitext(img)
            thumbnail = filename[0] + "_thumb" + filename[1]
            # print((fileDir + img, fileDir + 'thumb/' + thumbnail))
            images.append((fileDir + img, fileDir + 'thumb/' + thumbnail))

        s = template.render(header_tmp = headerTmp, 
                            nav_tmp    = navTmp, 
                            footer_tmp = footerTmp, 
                            images     = images,
                            description = descriptions)
    else:
        s = template.render(header_tmp = headerTmp, nav_tmp = navTmp, footer_tmp = footerTmp)

    output = open(f'../{page[4:]}', 'w') # remove "tmp_" from output file name
    output.write(s)

