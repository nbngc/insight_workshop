def add_tags(tag, html_string):
    wrapped_html = f"<{tag}>{html_string}</{tag}>"
    print(wrapped_html)


add_tags('i', 'python')
add_tags('b', 'Python Tutorial')
