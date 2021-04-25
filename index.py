# -*- coding: utf-8 -*-
import web
urls = (
    '/', 'index'
)

### Templates
render = web.template.render("templates", base="base")

class index:

    form = web.form.Form(
        web.form.Textbox("url", web.form.notnull,size=80, description="输入需要URL:"),
        web.form.Button("清理缓存"),
    )

    

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
