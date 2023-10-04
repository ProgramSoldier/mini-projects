import tkinter

import flet
import time




def add_zero(num: int) -> str:
    if num < 10:
        return '0' + str(num)
    return str(num)

def time_change(texts: list[flet.Text], value: int, max_size: int):
    if value > max_size:
        value = 0
    elif value < 0:
        value = max_size
    texts[1].current.value = add_zero(value)

    if value < max_size:
        texts[2].current.value = add_zero(value + 1)
    elif value == max_size:
        texts[2].current.value = '00'

    if value > 0:
        texts[0].current.value = add_zero(value - 1)
    else:
        texts[0].current.value = add_zero(max_size)
    return value



def main(page: flet.Page):
    button_up_hours =  flet.Ref[flet.IconButton]()
    text_up_hours = flet.Ref[flet.Text]()
    text_hours = flet.Ref[flet.TextField]()
    text_down_hours = flet.Ref[flet.Text]()
    button_down_hours = flet.Ref[flet.IconButton]()

    button_up_min = flet.Ref[flet.IconButton]()
    text_up_min = flet.Ref[flet.Text]()
    text_min = flet.Ref[flet.TextField]()
    text_down_min = flet.Ref[flet.Text]()
    button_down_min = flet.Ref[flet.IconButton]()

    button_up_sec = flet.Ref[flet.IconButton]()
    text_up_sec = flet.Ref[flet.Text]()
    text_sec = flet.Ref[flet.TextField]()
    text_down_sec = flet.Ref[flet.Text]()
    button_down_sec = flet.Ref[flet.IconButton]()

    times = [0, 0, 0]
    run_timer = False
    is_not_stop = True

    page.window_width = 1200
    page.window_height = 600
    page.window_resizable = False

    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    def text_field_on_blur(text_f: flet.Ref[flet.TextField], idx, max_value: int):
        def wrapper(e):
            text = text_f.current.value
            old_value = times[idx]
            if text.isdigit():
                num = int(text)
                if 0 <= num < max_value:
                    times[idx] = num
                    text_f.current.value = add_zero(num)
                else:
                    text_f.current.value = add_zero(old_value)
            else:
                text_f.current.value = add_zero(old_value)
            page.update()
        return wrapper



    def button_click_times(texts: list[flet.Text], is_add: bool, max_size: int, idx: int):
        def wrapper(e):
            if is_add:
                value = int(texts[1].current.value) + 1
            else:
                value = int(texts[1].current.value) - 1
            times[idx] = time_change(texts, value, max_size)
            page.update()
        return wrapper

    def button_stop_timer(e):
        nonlocal run_timer, is_not_stop
        run_timer = False
        is_not_stop = False



    def button_start_timer(e):
        nonlocal run_timer, is_not_stop
        hours, minutes, seconds = times
        button_up_hours.current.visible = False
        button_down_hours.current.visible = False
        button_up_min.current.visible = False
        button_down_min.current.visible = False
        button_up_sec.current.visible = False
        button_down_sec.current.visible = False
        run_timer = True
        while run_timer:
            seconds -= 1
            if seconds < 0:
                seconds = 59
                minutes -= 1
                if minutes < 0:
                    minutes = 59
                    hours -=1
                    if hours < 0:
                        run_timer = False
                        break
            print(hours,minutes,seconds)

            time_change([text_down_hours, text_hours, text_up_hours], hours, 99)
            time_change([text_down_min, text_min, text_up_min], minutes, 59)
            time_change([text_down_sec, text_sec, text_up_sec], seconds, 59)
            page.update()
            time.sleep(1)


        if is_not_stop:
            window = tkinter.Tk()
            window.title("Новое окно")
            window.geometry('1200x800')
            label = tkinter.Label(window, text="Время вышло!!!!!!!!!!", font='Times 60')
            label.pack(anchor='center', expand=1)
            window.wm_attributes("-topmost", 1)
            window.mainloop()
        is_not_stop = True
        
        times[0], times[1], times[2] = 0, 0, 0
        button_up_hours.current.visible = True
        button_down_hours.current.visible = True
        button_up_min.current.visible = True
        button_down_min.current.visible = True
        button_up_sec.current.visible = True
        button_down_sec.current.visible = True
        page.update()




    page.add(
        flet.Row(
            [
                flet.Column(
                    [
                        flet.IconButton( flet.icons.ADD, ref= button_up_hours, on_click=button_click_times([text_down_hours, text_hours, text_up_hours], True, 99, 0)),
                        flet.Text(ref=text_up_hours, value='01', width=page.window_width / 10, text_align='Center'),
                        flet.TextField(ref=text_hours, label='Часы', value=add_zero(times[0]), width=page.window_width / 10, text_align='Center', on_blur=text_field_on_blur(text_hours, 0, max_value=100)),
                        flet.Text(ref=text_down_hours, value='99', width=page.window_width / 10, text_align='Center'),
                        flet.IconButton( flet.icons.REMOVE, ref= button_down_hours, on_click=button_click_times([text_down_hours, text_hours, text_up_hours], False, 99, 0)),
                    ],
                    alignment=flet.alignment.center

                ),
                flet.Text(value=':'),
                flet.Column(
                    [
                        flet.IconButton( flet.icons.ADD, ref=button_up_min, on_click=button_click_times([text_down_min, text_min, text_up_min], True, 59, 1)),
                        flet.Text(ref=text_up_min, value='01', width=page.window_width / 10, text_align='Center'),
                        flet.TextField(ref=text_min, label='Минуты', value=add_zero(times[1]), width=page.window_width / 10, text_align='Center', on_blur=text_field_on_blur(text_min, 1,  max_value=60)),
                        flet.Text(ref=text_down_min, value='59', width=page.window_width / 10, text_align='Center'),
                        flet.IconButton(flet.icons.REMOVE, ref=button_down_min, on_click=button_click_times([text_down_min, text_min, text_up_min], False, 59, 1)),
                    ],


                ),
                flet.Text(value=':'),
                flet.Column(
                    [
                        flet.IconButton(flet.icons.ADD, ref= button_up_sec, on_click=button_click_times([text_down_sec, text_sec, text_up_sec], True, 59, 2)),
                        flet.Text(ref=text_up_sec, value='01', width=page.window_width / 10, text_align='Center'),
                        flet.TextField(ref=text_sec, label='Секунды', value=add_zero(times[2]), width=page.window_width / 10, text_align='Center', on_blur=text_field_on_blur(text_sec, 2, max_value=60)),
                        flet.Text(ref=text_down_sec, value='59', width=page.window_width / 10, text_align='Center'),
                        flet.IconButton(flet.icons.REMOVE, ref= button_down_sec, on_click=button_click_times([text_down_sec, text_sec, text_up_sec], False, 59, 2)),
                    ],

                )
            ],
            alignment=flet.MainAxisAlignment.CENTER
        ),
        flet.TextButton('Запустить таймер', on_click=button_start_timer),
        flet.TextButton('Остановить', on_click=button_stop_timer)

    )




flet.app(target=main)
