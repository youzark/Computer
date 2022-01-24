from prompt_toolkit import prompt, print_formatted_text, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import FormattedText

style = Style.from_dict(
        {
            "aaa": '#ff0066',
            "bbb": '#44ff00 italic'
            }
        )

text = FormattedText(
        [
            ('#ff0066','hello'),
            ('',' '),
            ('#44ff00 italic','World')
            ]
        )

same_text = FormattedText(
        [
            ('class:aaa','hello'),
            ('',' '),
            ('class:bbb','World')
            ]
        )
if __name__ == '__main__':
    answer = prompt("Give me some input:")
    print_formatted_text(f"you just said {answer}")
    print_formatted_text(HTML('<b><ansiblue>This is bold</ansiblue></b>'))
    print_formatted_text(HTML('<aaa fg="ansired" bg="ansiwhite">This has background_color</aaa>'))
    print_formatted_text(HTML('<aaa>customized color</aaa> <bbb>customized color and italic</bbb>'),style=style)
    print_formatted_text(text)
    print_formatted_text(same_text,style=style)
    

