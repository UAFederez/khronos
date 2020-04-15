from jinja2 import Template

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
          'tmp_pipeline.html', 'tmp_glut.html', 'tmp_news.html', 'tmp_res.html',
          'tmp_contact.html']

navTmp    = open('templates/nav_template.html').read()
headerTmp = open('templates/header_template.html').read()
footerTmp = open('templates/footer_template.html').read()

faqs = read_faqs_file()
pipe = read_pipeline_file()

for page in pages[:5]:
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
    else:
        s = template.render(header_tmp = headerTmp, nav_tmp = navTmp, footer_tmp = footerTmp)

    output = open(f'../{page[4:]}', 'w') # remove "tmp_" from output file name
    output.write(s)

