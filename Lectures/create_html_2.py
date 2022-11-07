from dominate.tags import html, body, div, table, tbody, tr, td, h1, p


h = html()
with h.add(body()).add(div(id='content')):
    h1('Hello World!')
    p('Lorem ipsum ...')
    with table().add(tbody()):
        l = tr()
        l += td('One')
        l.add(td('Two'))
        with l:
            td('Three')

print(h)