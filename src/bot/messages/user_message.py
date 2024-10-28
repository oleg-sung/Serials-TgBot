import re
from typing import Any


def make_serial_preview(data: dict[str, Any]) -> str:
    show_info = data['show']
    show_name = show_info['name']
    show_genres = ' ,'.join(show_info['genres']) if show_info['genres'] else ' unknown.'
    show_stared = show_info['premiered'] if show_info['premiered'] else 'The serial has not been released yet.'
    show_ended = show_info['ended'] if show_info['ended'] else 'until now'
    show_status = show_info['status']
    show_description = remove_html_tags(show_info['summary']) if show_info['summary'] else ' unknown.'
    if show_info.get('image', False):
        show_preview = show_info['image']['medium']
    else:
        show_preview = ''

    serial_message_preview = (
        f'<b>{show_name}</b>\n\n'
        f'Genres: {show_genres}\n\n'
        f'Start - {show_stared} end - {show_ended}\n\n'
        f'Status: <b>{show_status}</b>\n\n'
        f'<b>Description</b>:\n{show_description}\n'
        f'\n{show_preview}'
    )

    return serial_message_preview


def remove_html_tags(text: str) -> str:
    if text is None:
        return ''
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
